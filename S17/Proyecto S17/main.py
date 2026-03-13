import FreeSimpleGUI as sg
from Logic_main import FinancialManager
from interfaces import *
from manage_docs import *
from validation import *

manage = FinancialManager()
manage.categories = charge_categories()
manage.movements = charge_movements()

window = main_window(manage.get_table())

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, "Salir"):
        break

    if event == "Add Category":
        w_cat = category_window()
        e, w = w_cat.read()
        if e == "Save" and text_validation(w["-NAME-"]):
            manage.add_category(w["-NAME-"])
            save_categories(manage.categories)
        w_cat.close()

    if event in ("Add Expense", "Add Income"):
        if not manage.categories:
            sg.popup_error("You Must create a category firstly")
            continue

        type_ = "Expense" if event == "Add Expense" else "Add Income"
        categories = [c.name for c in manage.categories]
        w_mov = movement_window(type_, categories)
        e, w = w_mov.read()

        if e == "Save":
            if not text_validation(w["-TITLE-"]):
                sg.popup_error("Invalid Title")
            elif not amount_validation(w["-AMOUNT-"]):
                sg.popup_error("Invalid amount")
            else:
                print(values)
                manage.add_movements(
                    w["-TITLE-"],
                    float(w["-AMOUNT-"]),
                    w["-CATEGORY-"],
                    type_
                )
                save_movements(manage.movements)

        w_mov.close()
        window["-TABLE-"].update(manage.get_table())

window.close()