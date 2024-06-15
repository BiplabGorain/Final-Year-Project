# Import necessary modules
import base64
import string
import os
from django.shortcuts import render
from django.conf import settings
from .forms import ImageUploadForm
from PIL import Image
from .encoder import get_recipes
import json

# Get the directory of the current script (views.py)
current_dir = os.path.dirname(__file__)

# Define the view function for the home page


def home_page(request):
    raw_image = None
    uploaded_image = None
    recipe_list_to_return = []

    # Check if the request method is POST
    if request.method == 'POST':
        # Create a form instance with the submitted data
        form = ImageUploadForm(request.POST, request.FILES)
        # Check if the form is valid
        if form.is_valid():
            # Retrieve the raw image data from the form
            raw_image = form.cleaned_data['image']
            # Encode the raw image data to base64 format
            uploaded_image = base64.b64encode(
                raw_image.file.read()).decode('ascii')
            # Open the raw image using PIL
            raw_image = Image.open(raw_image)
            # Get recipes from the uploaded image
            recipe_list = get_recipes(raw_image)

            # Adjust the path to indian_recipes.json
            json_file_path = os.path.join(
                current_dir, 'static', 'main', 'indian_recipes.json')
            # Load JSON data from the file
            recipes_data = json.load(open(json_file_path))

            # Iterate through the recipe list
            for i in range(len(recipe_list)):
                name = recipe_list[i]
                # Filter the recipes data to find matching recipe by name
                matching_recipes = list(
                    filter(lambda x: x["name"] == name, recipes_data))
                if len(matching_recipes) != 0:
                    # Extract recipe details if a match is found
                    matching_recipe = matching_recipes[0]
                    calories = matching_recipe['calories']
                    cooking_time = matching_recipe['cooking_time']
                    ingredients = matching_recipe['ingredients']
                    directions = matching_recipe['directions']
                    # Prepare a list of recipe details to return
                    list_to_append = [string.capwords(
                        name), calories, cooking_time, ingredients, directions]
                    recipe_list_to_return.append(list_to_append)

    else:
        # If request method is not POST, create an empty form
        form = ImageUploadForm()

    # Render the home page template with necessary data
    return render(request, 'main/home.html', {'form': form, 'uploaded_image': uploaded_image,
                                                'recipe_list_to_return': recipe_list_to_return[:4],
                                                'similar_recipe_list': recipe_list_to_return[4:10]})
