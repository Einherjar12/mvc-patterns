class Shoe:
    def __init__(self, gender, kind, color, price, manufacturer, size):
        self.gender = gender  # 'мужская' или 'женская'
        self.kind = kind  # вид обуви (кроссовки, сапоги и т.д.)
        self.color = color
        self.price = price
        self.manufacturer = manufacturer
        self.size = size

    def __str__(self):
        return (f"Обувь: {self.kind}, Пол: {self.gender}, Цвет: {self.color}, "
                f"Размер: {self.size}, Цена: {self.price} руб., Производитель: {self.manufacturer}")

    def update_price(self, new_price):
        self.price = new_price