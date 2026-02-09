class RecipeView:
    @staticmethod
    def display_recipe(recipe):
        print("-------------------------------------")
        print(f"🍽️ Рецепт: {recipe.title}")
        print(f"👨‍🍳 Автор: {recipe.author}")
        print(f"📂 Тип: {recipe.recipe_type}")
        print(f"🌍 Кухня: {recipe.cuisine}")
        print(f"📄 Описание:\n{recipe.description}")
        print("🧾 Ингредиенты:")
        for i, ingredient in enumerate(recipe.ingredients, 1):
            print(f"   {i}. {ingredient}")
        print(f"🎥 Видео: {recipe.video_link}")
        print("--------------------------------------------------\n")


