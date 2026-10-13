
note_counter = 1
approved_notes = 0
disapproved_notes = 0
prom_approved_notes = 0
prom_disapproved_notes = 0
prom_notes = 0
total_notes = int(input("ingrese la cantidad de notas"))
while note_counter <= total_notes :
        actual_note = int(input(f"ingrese la nota numero {note_counter}"))
        if actual_note < 70 :
            disapproved_notes = disapproved_notes + 1
            prom_disapproved_notes = actual_note + prom_disapproved_notes
            note_counter = note_counter + 1
        else :
            approved_notes = approved_notes + 1
            prom_approved_notes = actual_note + prom_approved_notes
            note_counter = note_counter + 1
prom_notes = ( prom_approved_notes + prom_disapproved_notes ) / total_notes
if disapproved_notes != 0 :
    prom_disapproved_notes = prom_disapproved_notes / disapproved_notes
else:
    prom_disapproved_notes = 0

if approved_notes != 0 :
    prom_approved_notes = prom_approved_notes / approved_notes
else:
    prom_approved_notes = 0
print (f"el estudiante tiene {approved_notes} notas aprobadas")
print (f"el promedio de notas aprobadas es de {prom_approved_notes}")
print (f"el estudiante tiene {disapproved_notes} notas no aprobadas")
print (f"el promedio de notas no aprobadas es de {prom_disapproved_notes}") 
print (f"el promedio de notas total es de {prom_notes}")