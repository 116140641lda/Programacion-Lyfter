from datetime import datetime


class Category:
    def __init__(self, name: str):
        self.name = name

    def to_dict(self):
        return {"name": self.name}


class Movement:
    def __init__(self, title: str, amount: float, category: str, type_: str):
        self.title = title
        self.amount = amount
        self.category = category
        self.type_ = type_  # "Ingreso" o "Gasto"
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def to_dict(self):
        return {
            "title": self.title,
            "amount": self.amount,
            "category": self.category,
            "type": self.type_,
            "date": self.date
        }


class FinancialManager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def add_category(self, name):
        if name in [c.name for c in self.categories]:
            raise ValueError("La categoría ya existe")
        category = Category(name)
        self.categories.append(category)

    def add_movements(self, title, amount, category, type_):

        if not self.categories:
            raise ValueError("No hay categorías disponibles")

        if category not in [c.name for c in self.categories]:
            raise ValueError("La categoría no existe")

        movement = Movement(title, amount, category, type_)
        self.movements.append(movement)

    def get_table(self):
        return [
            [m.date, m.type_, m.title, m.category, m.amount]
            for m in self.movements
        ]


