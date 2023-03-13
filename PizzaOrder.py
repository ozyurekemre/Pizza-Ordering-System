####################################################
#PIZZA ORDERING SYSTEM#
####################################################

class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 0.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost

class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Klasik pizza, domates sosu ve peynirle kaplıdır."
        self.cost = 100.0

class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Margarita pizza, domates sosu, mozzarella peyniri ve taze fesleğenle kaplıdır."
        self.cost = 115.0

class TurkishPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Türk pizza, sucuk, domates, yeşil biber ve kaşar peyniriyle kaplıdır."
        self.cost = 120.0

class DominosPizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Dominos pizza, pepperoni, sosis, yeşil biber ve mantarlarla kaplıdır."
        self.cost = 135.0

class Decorator(Pizza):
    def __init__(self, pizza):
        super().__init__()
        self.component = pizza

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


class OliveSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Zeytin Sos"
        self.price = 3.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class MushroomSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mantar Sos"
        self.price = 2.5

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class GoatCheeseSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Keçi Peyniri Sos"
        self.price = 4.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class MeatSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Et Sos"
        self.price = 5.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class OnionSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Soğan Sos"
        self.price = 2.0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


class CornSauce(Decorator):
    def __init__(self, pizza):
        super().__init__(pizza)
        self.description = "Mısır Sos"
        self.price = 2.5

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.price


def main():
    # Menu.txt dosyasını okuyun ve menüyü yazdırın
    with open("datasets/Menu.txt", "r") as f:
        print(f.read())

    # Kullanıcıdan pizza ve sos seçimlerini alın
    pizza_choice = int(input("Lütfen pizza seçiniz (1-4): "))
    sauce_choice = int(input("Lütfen sos seçiniz (11-16): "))

    # Seçilen pizza ve sosu oluşturun
    if pizza_choice == 1:
        pizza = ClassicPizza()
    elif pizza_choice == 2:
        pizza = MargheritaPizza()
    elif pizza_choice == 3:
        pizza = TurkishPizza()
    elif pizza_choice == 4:
        pizza = DominosPizza()

    if sauce_choice == 11:
        sauce = OliveSauce(pizza)
    elif sauce_choice == 12:
        sauce = MushroomSauce(pizza)
    elif sauce_choice == 13:
        sauce = GoatCheeseSauce(pizza)
    elif sauce_choice == 14:
        sauce = MeatSauce(pizza)
    elif sauce_choice == 15:
        sauce = OnionSauce(pizza)
    elif sauce_choice == 16:
        sauce = CornSauce(pizza)

    # Toplam fiyatı hesapla
    total_cost = sauce.get_cost() + pizza.get_cost()

    # Kullanıcı bilgilerini alın
    print("\nMüşteri Bilgileri(Customer Information):")
    print(''.center(100, "*"))
    name = input("İsim: ")
    tc = input("TC Kimlik Numarası: ")
    cc_number = input("Kredi Kartı Numarası: ")
    cc_cvv = input("Kredi Kartı Güvenlik Kodu: ")

    # Sipariş özetini yazdırın
    print("\nSipariş Özeti(Order Summary):")
    print(''.center(100, "*"))
    print("Pizza: ", pizza.get_description())
    print("Sos: ", sauce.get_description())
    print("Toplam Fiyat: ", total_cost)
    print("Müşteri Bilgileri:")
    print("İsim: ", name)
    print("TC Kimlik Numarası: ", tc)
    print("Kredi Kartı Numarası: ", cc_number)
    print("Kredi Kartı Güvenlik Kodu: ", cc_cvv)

    import csv
    from datetime import datetime

    # Sipariş bilgilerini veritabanına kaydet
    with open("Orders_Database.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([name, tc, cc_number, pizza.get_description(), sauce.get_description(), total_cost, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), cc_cvv])



if __name__ == '__main__':
    main()




























