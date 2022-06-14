from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic, View
from .models import Recipe
from .forms import RecipeForm
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
        #     liked = TrueS

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                # "liked": liked
            }
        )

class CreateRecipe(View):
    
    def get(self, request, *args, **kwargs):
        form = RecipeForm()
        if request.method == 'POST':
            form = RecipeForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')

        context = {'form': form}
        return render(request, 'create_recipe.html', context)

    def post(self, slug, request, *args, **kwargs):
        form = RecipeForm()
        if request.method == 'POST':
            form = RecipeForm(request.POST)
            if form.is_valid():
                form.instance.name = request.user.username
                recipe = form.save(commit=False)
                recipe.author = request.user
                recipe.save()
                return redirect('home')

        context = {'form': form}
        return render(request, 'create_recipe.html', context)
        