import csv
import os
from actions import Student

class CsvAdmin:
    def __init__(self, total_info=None):
        self.total_info = total_info if total_info is not None else []
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.DOC = os.path.join(self.BASE_DIR, 'students.csv')


    def export_csv(self):
        if not self.total_info:
            print("Archivo vacío, nada que exportar.")
            return

        campos = ["code", "name", "section", "spanish", "english", "social", "science", "prom_total"]

        with open(self.DOC, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=campos)
            writer.writeheader()


            data = [student.__dict__ for student in self.total_info]
            writer.writerows(data)

        print(f"Proceso exportación finalizado. {len(self.total_info)} estudiantes guardados en '{self.DOC}'.")

   
    def import_file(self):
        if not os.path.exists(self.DOC):
            print('No existe archivo a importar')
            return []

        self.total_info.clear()

        with open(self.DOC, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            for row in reader:
                
                if not row["code"].strip():
                    continue

               
                try:
                    spanish = float(row["spanish"])
                    english = float(row["english"])
                    social = float(row["social"])
                    science = float(row["science"])
                except ValueError:
                    print(f"Fila inválida ignorada: {row}")
                    continue

        
                student = Student(
                    code=row["code"].strip(),
                    name=row["name"].strip(),
                    section=row["section"].strip(),
                    spanish=spanish,
                    english=english,
                    social=social,
                    science=science
                )

                self.total_info.append(student)

        print(f"Proceso importación finalizado. {len(self.total_info)} estudiantes cargados.")
        return self.total_info
