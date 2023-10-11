cantidad_pacientes = cantidad_pacientes_registrados
pacientes = []

contador1=0
while contador1<cantidad_pacientes:
    with open('file.txt', 'r') as f:
        for line in f:
            ##con el rstrip se eliminan los "next line" y el split coloca cada palabra en un item de list
            text = line.rstrip('\n').split(" --- ")
            if len(text) > 1:
                pacientes.append(text[1])

def