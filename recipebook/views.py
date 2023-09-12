from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponseRedirect
from .models import Recipe, Diet, Rating, Comment
from .forms import CommentForm, RecipeForm


@login_required
def update_recipe(request, recipe_id):  # Code inspired by Codemy.com
    recipe = Recipe.objects.get(pk=recipe_id)
    form = RecipeForm(request.POST or None, instance=recipe)
    if form.is_valid():
        form.save()
        return redirect('profile')
    return render(request, 'update_recipe.html', {
        'recipe': recipe, 'form': form})


@login_required
def delete_recipe(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    return redirect('profile')


@login_required
def add_recipe(request):  # Code inspired by Codemy.com
    submitted = False
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.status = 0
            recipe.author = request.user
            form.save()
            return HttpResponseRedirect(
                '/recipebook/add_recipe?submitted=True')
        else:
            messages.error(request, "Error")
    else:
        form = RecipeForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'add_recipe.html', {
        'form': form, 'submitted': submitted})


def search_results(request):
    recipes_list = Recipe.objects.filter(status=1)
    searched = request.GET.get('searched')
    if searched:
        recipes_list = Recipe.objects.filter(
            Q(title__icontains=searched) |
            Q(content__icontains=searched) |
            Q(author__username__icontains=searched) |
            Q(ingredients__contains=searched) |
            Q(diet__name__icontains=searched) |
            Q(season__name__icontains=searched))
    paginator = Paginator(recipes_list, 8)
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


@login_required
def rate(request, recipe_id, rating):  # Code adapted from https://medium.com/
    user = request.user
    recipe = get_object_or_404(Recipe, id=recipe_id)
    rating_instance, created = Rating.objects.get_or_create(
        user=user, recipe=recipe)
    rating_instance.rating = rating
    rating_instance.save()
    return JsonResponse({'message': 'Rating updated successfully'})


class IndexView(TemplateView):
    template_name = 'index.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipes = Recipe.objects.filter(status=1)
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
            comment_form.instance.name = request.user
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
