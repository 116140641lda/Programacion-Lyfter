import FreeSimpleGUI as sg
from validation import text_validation, amount_validation


def main_window(data):
    layout = [
        [sg.Table(
            values=data,
            headings=["Date", "Type", "Title", "Category", "Amount"],
            key="-TABLE-",
            auto_size_columns=True,
            expand_x=True,
            expand_y=True
        )],
        [
            sg.Button("Add Category"),
            sg.Button("Add Expense"),
            sg.Button("Add Income"),
            sg.Button("Salir")
        ]
    ]
    return sg.Window("Financial Manager", layout, finalize=True)


def category_window():
    layout = [
        [sg.Text("Category name")],
        [sg.Input(key="-NAME-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    return sg.Window("New Category", layout)


def movement_window(type_, categories):
    layout = [
        [sg.Text("Title"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category"),
         sg.Combo(categories, key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]
    return sg.Window(f"New {type_}", layout)