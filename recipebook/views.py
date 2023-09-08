from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import TemplateView
from .models import Recipe, Diet
from .forms import CommentForm
from django.contrib.auth.models import User
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def search_results(request):
    recipes_list = Recipe.objects.all()
    searched = request.GET.get('searched')
    if searched:
        recipes_list = Recipe.objects.filter(
            Q(title__contains=searched) |
            Q(content__contains=searched) |
            Q(ingredients__contains=searched))
    paginator = Paginator(recipes_list, 2)
    page = request.GET.get('page')

    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    context = {
        'searched': searched, 'recipes': recipes
    }

    return render(request, 'search_results.html', context)


class IndexView(TemplateView):
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Recipe.objects.all()
        diets = Diet.objects.all()
        paginator = Paginator(recipes, self.paginate_by)
        page = self.request.GET.get('page')
        recipes_page = paginator.get_page(page)

        context['recipes'] = recipes_page
        context['diets'] = diets
        return context


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


class DietList(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        diets = Diet.objects.all()
        diet_recipes = {}

        for diet in diets:
            recipes = Recipe.objects.filter(diet=diet)
            diet_recipes[diet] = recipes

        context['diet_recipes'] = diet_recipes
        return context


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")
        fav = bool
        if recipe.favourites.filter(id=request.user.id).exists():
            fav = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": False,
                "comment_form": CommentForm(),
                'fav': fav
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.filter(
            approved=True).order_by("-created_on")

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
            },
        )
