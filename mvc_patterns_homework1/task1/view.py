class ShoeView:
    @staticmethod
    def show_shoe_info(shoe):
        print("Информация об обуви:")
        print(shoe)
        print("===========================")

    @staticmethod
    def show_price_update(old_price, new_price):
        print(f"Цена обновлена: была {old_price} руб., стала {new_price} руб.")


