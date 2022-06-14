from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe
# Create your views here.

class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'
    paginate_by = 12

class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        # liked = False
        # if recipe.likes.filter(id=self.request.user.id).exists():
        #     liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                # "liked": liked
            }
        )