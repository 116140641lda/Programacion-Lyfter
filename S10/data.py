import csv
import os
import actions

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DOC = os.path.join(BASE_DIR, 'students.csv')

def export_csv():
    print("Iniciando exportación...")
    if not actions.total_info:
        print("Archivo vacio")
        return
    print(actions.total_info)
    with open(DOC, mode='w', newline='', encoding='utf-8') as file:
        campos = ['name', 'section', 'spanish', 'english', 'social', 'science', 'prom_total']
        writer = csv.DictWriter(file, fieldnames=campos)
        writer.writeheader()
        writer.writerows(actions.total_info)
        print('Proceso exportación finalizado')


def import_file ():
    if not os.path.exists(DOC):
        print('No existe archivo a importar')
        return
    with open(DOC, mode='r', encoding='utf-8',) as file:
        reader = csv.DictReader(file)
        actions.total_info.clear()
        for row in reader:
            student = {
                'name': row["name"],
                "section": row["section"],
                "spanish": float(row["spanish"]),
                "english": float(row["english"]),
                "social": float(row["social"]),
                "science": float(row["science"]),
                "prom_total": float(row["prom_total"])

            }
            actions.total_info.append(student)
        
        print ("Proceso importación finalizado")