from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
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


# def search_results(request, page=1):
#     if request.method == "POST":
#         searched = request.POST['searched']
#         recipes = Recipe.objects.filter(
#             Q(title__contains=searched) |
#             Q(content__contains=searched) |
#             Q(ingredients__contains=searched))   
#         paginator = Paginator(recipes, 2)
#         try:
#             recipes = paginator.page(page)
#         except EmptyPage:
#             recipes = paginator.page(paginator.num_pages)
#         return render(
#             request, 'search_results.html', {
#                 'searched': searched, 'recipes': recipes
#                 })


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 4


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
