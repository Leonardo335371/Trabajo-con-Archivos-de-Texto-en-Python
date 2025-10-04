# Escribir en el archivo
with open('my_notes.txt', 'w') as file:
    # Escribir las notas personales
    file.write('Nota 1: Despertarse correctamente.\n')
    file.write('Nota 2: Alistarse y lavarse los dientes.\n')
    file.write('Nota 3: Cocinar mi desayuno y almuerzo.\n')

# Leer y mostrar el contenido del archivo
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea
    line = file.readline()
    while line:
        # Mostrar cada línea, eliminando el salto de línea adicional
        print(line.strip())
        line = file.readline()
