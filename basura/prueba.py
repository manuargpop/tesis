porcent_grasa_f = 30
estatura = 1.75
peso = 96

indice_mlg = (peso * (((100 - porcent_grasa_f) / 100) + 6.1 * (1.8 - estatura))) / estatura ** 2
print(indice_mlg)