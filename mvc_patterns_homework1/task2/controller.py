class RecipeController:
    def __init__(self, recipe, view):
        self.recipe = recipe
        self.view = view

    def add_ingredient(self, ingredient):
        self.recipe.add_ingredient(ingredient)

    def remove_ingredient(self, ingredient):
        self.recipe.remove_ingredient(ingredient)

    def change_description(self, new_description):
        self.recipe.update_description(new_description)

    def change_video_url(self, new_url):
        self.recipe.update_video_url(new_url)

    def show_recipe(self):
        self.view.display_recipe(self.recipe)

