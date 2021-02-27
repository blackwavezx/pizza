from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any

# интерфейс строителя со всеми возможными конфигурациями продукта
class Builder(ABC):

    @property
    @abstractmethod
    def pizza(self):
        pass

    @abstractmethod
    def add_dough(self):
        pass

    @abstractmethod
    def add_sauce(self):
        pass

    @abstractmethod
    def add_cheese(self):
        pass

    @abstractmethod
    def add_mushroom(self):
        pass

    @abstractmethod
    def add_pepperoni(self):
        pass

    @abstractmethod
    def add_ham(self):
        pass

    @abstractmethod
    def add_olives(self):
        pass


class PizzaBuilder(Builder):

    # создает пустой объект
    def __init__(self):

        self.reset() # обнуляет значения атрибутов

    # пустой обект = продукт
    def reset(self):
        self._pizza = Pizza1()

    @property
    def pizza(self) -> Pizza1:

        pizza = self._pizza
        self.reset()
        return pizza

    def add_dough(self):
        self._pizza.add("dough")

    def add_sauce(self):
        self._pizza.add("sauce")

    def add_cheese(self):
        self._pizza.add("cheese")

    def add_mushroom(self):
        self._pizza.add("mushrooms")

    def add_pepperoni(self):
        self._pizza.add("pepperoni")

    def add_ham(self):
        self._pizza.add("ham")

    def add_olives(self):
        self._pizza.add("olives")


class Pizza1:

    def __init__(self):
        self.ingredients = []

    def add(self, part: Any):
        self.ingredients.append(part)

    def list_ingredients(self):
        print(f"Pizza ingredients: {', '.join(self.ingredients)}", end="")


class Director:

    def __init__(self):
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def bake_pepperoni(self):
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_pepperoni()

    def bake_prosciutto(self):
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_ham()

    def bake_capricciosa(self):
        self.builder.add_dough()
        self.builder.add_sauce()
        self.builder.add_cheese()
        self.builder.add_ham()
        self.builder.add_mushroom()
        self.builder.add_olives()


if __name__ == "__main__":

    director = Director()
    builder = PizzaBuilder()
    director.builder = builder

    print("Capricciosa: ")
    director.bake_capricciosa()
    builder.pizza.list_ingredients()

    print("\n")

    print("Prosciutto: ")
    director.bake_prosciutto()
    builder.pizza.list_ingredients()

    print("\n")

    # Строитель без использования Директора
    print("Custom pizza, bon appetit!: ")
    builder.add_dough()
    builder.add_sauce()
    builder.add_cheese()
    builder.pizza.list_ingredients()