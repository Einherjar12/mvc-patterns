from model import Shoe
from view import ShoeView


class ShoeController:
    def __init__(self):
        self.shoe = None

    def create_shoe(self, gender, kind, color, price, manufacturer, size):
        self.shoe = Shoe(gender, kind, color, price, manufacturer, size)

    def show_shoe(self):
        if self.shoe:
            ShoeView.show_shoe_info(self.shoe)
        else:
            print("Обувь не создана.")

    def update_price(self, new_price):
        if self.shoe:
            old_price = self.shoe.price
            self.shoe.update_price(new_price)
            ShoeView.show_price_update(old_price, new_price)
        else:
            print("Обувь не создана.")
