# Задание 1. Создайте класс Обувь. Необходимо хранить следующую информацию:
# ■ тип обуви;
# ✓мужская,
# ✓женская;
# ■ вид обуви (кроссовки, сапоги, сандалии, туфли и т.д.);
# ■ цвет;
# ■ цена;
# ■ производитель;
# ■ размер.
# Создайте необходимые методы для этого класса. Реализуйте паттерн MVC
# для класса Обувь и код для использования модели, контроллера и представления.


from controller import ShoeController


def main():
    controller = ShoeController()

    # Создание обуви
    controller.create_shoe(
        gender="Женская",
        kind="Кроссовки",
        color="Белый",
        price=8500,
        manufacturer="Nike",
        size=38
    )

    # Показ информации
    controller.show_shoe()

    # Обновление цены
    controller.update_price(7900)

    # Повторный вывод
    controller.show_shoe()


if __name__ == "__main__":
    main()
