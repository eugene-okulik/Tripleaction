class Flower:
    # general Class
    def __init__(self, name, color, price, fresh, length):
        self.name = name
        self.color = color
        self.price = price
        self.fresh = fresh
        self.length = length

    def __repr__(self):
        return f"{self.name} {self.color} - {self.price} руб - {self.fresh} срок годности - {self.length} длина стебля"


class Rose(Flower):
    def __init__(self, name, color, price, fresh, length):
        super().__init__(name, color, price, fresh, length)


class Violet(Flower):
    def __init__(self, name, color, price, fresh, length):
        super().__init__(name, color, price, fresh, length)


class Lily(Flower):
    def __init__(self, name, color, price, fresh, length):
        super().__init__(name, color, price, fresh, length)


class Aster(Flower):
    def __init__(self, name, color, price, fresh, length):
        super().__init__(name, color, price, fresh, length)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def calculate_cost(self):
        return sum(flower.price for flower in self.flowers)

    def time_of_life(self):
        if not self.flowers:
            return 0
        return sum(flower.fresh for flower in self.flowers) / len(self.flowers)

    def sort_by_freshness(self):
        self.flowers.sort(key=lambda flower: flower.fresh)

    def sort_by_color(self):
        self.flowers.sort(key=lambda flower: flower.color)

    def sort_by_length(self):
        self.flowers.sort(key=lambda flower: flower.length)

    def sort_by_price(self):
        self.flowers.sort(key=lambda flower: flower.price)

    def search_by_time(self, value):
        return [flower for flower in self.flowers if flower.fresh > value]

    def __repr__(self):
        flowers_list = ", ".join([str(flower) for flower in self.flowers])
        total_cost = self.calculate_cost()
        avg_life = self.time_of_life()
        return (f"Bouquet: {flowers_list}\n"
                f"Total cost: {total_cost} руб\n"
                f"Average time of life: {avg_life} дней")


if __name__ == "__main__":
    # Создание цветов
    rose1 = Rose("Rose", "black", 100, 14, 33)
    violet1 = Violet("Violet", "purple", 50, 5, 15)
    lily1 = Lily("Lily", "yellow", 160, 1, 19)
    aster1 = Aster("Aster", "pink", 300, 12, 13)

    bouquet = Bouquet()
    bouquet.add_flower(rose1)
    bouquet.add_flower(violet1)
    bouquet.add_flower(lily1)
    bouquet.add_flower(aster1)

    bouquet.sort_by_freshness()
    print(bouquet)

    bouquet.sort_by_length()
    print(bouquet)

    bouquet.sort_by_color()
    print(bouquet)

    bouquet.sort_by_price()
    #сортировка по цене
    print(bouquet)

    value = 3
    fresh_flowers = bouquet.search_by_time(value)
    for flower in fresh_flowers:
        print(flower)
