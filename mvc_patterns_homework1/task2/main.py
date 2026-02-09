# Задание 2. Создайте класс Рецепт. Необходимо хранить следующую информацию:
# ■ название рецепта;
# ■ автор рецепта;
# ■ тип рецепта (первое, второе блюдо и т.д.);
# ■ текстовое описание рецепта;
# ■ ссылка на видео с рецептом;
# ■ список ингредиентов;
# ■ название кухни (итальянская, французская, украинская и т.д.).
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC для класса Рецепт и
# код для использования модели, контроллера и представления.

from model import Recipe
from view import RecipeView
from controller import RecipeController

def main():
    # Создаем три рецепта
    recipe1 = Recipe(
        title="Паста Карбонара",
        author="Иван Иванов",
        recipe_type="Второе блюдо",
        description="Классическая итальянская паста с беконом, яйцом и сыром Пармезан.",
        video_link="https://example.com/carbonara-video",
        ingredients=["Паста", "Бекон", "Яйцо", "Сыр Пармезан", "Соль", "Перец"],
        cuisine="Итальянская"
    )

    recipe2 = Recipe(
        title="Салат Цезарь",
        author="Мария Петрова",
        recipe_type="Салат",
        description="Свежий салат с курицей, сухариками и фирменным соусом Цезарь.",
        video_link="https://example.com/caesar-video",
        ingredients=["Курица", "Салат Романо", "Сухарики", "Сыр Пармезан", "Соус Цезарь"],
        cuisine="Американская"
    )

    recipe3 = Recipe(
        title="Рататуй",
        author="Пьер Дюпон",
        recipe_type="Гарнир",
        description="Французское овощное рагу с баклажанами, кабачками и томатами.",
        video_link="https://example.com/ratatouille-video",
        ingredients=["Баклажан", "Кабачок", "Перец", "Помидоры", "Лук", "Чеснок", "Оливковое масло", "Соль", "Перец"],
        cuisine="Французская"
    )

    # Создаем контроллеры
    view = RecipeView()
    controller1 = RecipeController(recipe1, view)
    controller2 = RecipeController(recipe2, view)
    controller3 = RecipeController(recipe3, view)

    # Показываем рецепты
    controller1.show_recipe()
    controller2.show_recipe()
    controller3.show_recipe()

    # Пример изменений
    controller1.add_ingredient("Чеснок")
    controller1.change_description("Паста Карбонара с добавлением чеснока.")
    controller1.show_recipe()

if __name__ == "__main__":
    main()

