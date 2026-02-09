class Recipe:
    def __init__(self, title, author, recipe_type, description, video_link, ingredients, cuisine):
        self.title = title
        self.author = author
        self.recipe_type = recipe_type
        self.description = description
        self.video_link = video_link
        self.ingredients = ingredients
        self.cuisine = cuisine

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)

    def update_description(self, new_description):
        self.description = new_description

    def update_video_url(self, new_url):
        self.video_link = new_url


