from fpdf import FPDF
from dateutil.relativedelta import relativedelta
from datetime import datetime

def create_pdf(filename):
    apellidos = "rodriguez ralei"
    nombres = "gustavo alexander"
    sexo = "hombre"
    tipo_doc = "CI"
    id_doc = "29502268"
    lugar_nac = "Venezuela, Zulia, Maracaibo"
    deporte = "caminar"
    tipo_pa = "adulto"
    fecha_me = "31/8/2023"
    fecha_nac = "10/10/1998"
    estatura = "180"
    peso = "65"

    imc = "20.00"
    icc = "0.9"
    ice = "ice"
    por_grasa = "%grasa"
    pe_grasa = "peso de la grasa"
    por_grasa_p = "grasa persentil"
    mlg = "18"
    camb = "camb pls"
    iamb = "32"
    complexion = "10.0"

    ##le estoy robando la formula a peso ideal por que no quiero programar tod0 otra vez solo para buscarlo
    fecha_nacimiento = datetime.strptime(fecha_nac, "%d/%m/%Y")
    fecha_med = datetime.strptime(fecha_me, "%d/%m/%Y")
    fedad = relativedelta(fecha_med, fecha_nacimiento).years
    print(fedad)
    ##print(f"{edad.years} años, {edad.months} meses y {edad.days} días")
    edad = fedad
    peso_ideal = float(estatura) - 100 - (((float(estatura)-150)/4)+((edad -20)/20))
    print(peso_ideal)
    ##fuente: Helvetica

    pdf = FPDF('P', 'pt', (2067, 2756))
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("formato1.jpg", 0, 0)
    ## 7 espacios en blanco para primera
    top = pdf.y
    offset = pdf.x + 40
    pdf.multi_cell(0, 20, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"{apellidos}\n\n\n\n\n\n\n\n\n       "
                          f"{nombres}\n\n\n\n\n\n\n\n\n       "
                          f"{sexo}\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_doc}\n\n\n\n\n\n\n\n\n       "
                          f"{id_doc}\n\n\n\n\n\n\n\n\n       "
                          f"{lugar_nac}\n\n\n\n\n\n\n\n\n\n       "
                          f"{deporte}\n\n\n\n\n\n\n\n\n       "
                          f"{tipo_pa}\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_me}\n\n\n\n\n\n\n\n\n       "
                          f"{fecha_nac}\n\n\n\n\n\n\n\n\n\n       "
                          f"{estatura}\n\n\n\n\n\n\n\n       "
                          f"{peso}")

    pdf.y = top
    pdf.x = offset

    pdf.multi_cell(0, 20, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {imc}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {icc}\n\n\n\n\n\n\n\n\n"
                          f"                                                            {ice}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {por_grasa}\n\n\n\n\n\n\n\n\n\n"
                          f"\n\n"
                          f"                                                            {pe_grasa}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {por_grasa_p}\n\n\n\n\n\n\n\n\n"
                          f"                                                            {mlg}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {camb}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {iamb}\n\n\n\n\n\n\n\n\n"
                          f"                                                            {complexion}\n\n\n\n\n\n\n\n\n\n"
                          f"                                                            {peso_ideal}")

    pdf.add_page()
    pdf.set_font("Helvetica", "B", 64)
    pdf.image("formato2.jpg", 0, 0)
    pdf.y = top
    pdf.x = offset

    def imc_medic(imc):
        fimc = float(imc)
        if fimc < 18.5:
            print("peso bajo")
            return "peso bajo"
        elif 18.5 < fimc < 24.9:
            print("Peso saludable")
            return "peso saludable"
        elif 18.5 < fimc < 24.9:
            print("Sobre peso")
            return "sobre peso"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 1")
            return "obesidad, grado 1"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 2")
            return "obesidad, grado 2"
        elif 18.5 < fimc < 24.9:
            print("Obesidad, grado 3, obesidad morbida")
            return "obesidad, grado 3, obesidad morbida"
        else:
            print("error final1bonus1")
            return "error imc"

    def icc_medic(icc,sexo):
        ficc = float(icc)
        if sexo == "hombre":
            if ficc >= 1.0:
                print("androide")
                return "androide"
            elif ficc < 1.0:
                print("ginecoide")
                return "ginecoide"
            else:
                print("error final2bonus1")
                return "error icc"
        elif sexo == "mujer":
            if ficc >= 0.8:
                print("androide")
                return "androide"
            elif ficc < 0.8:
                print("ginecoide")
                return "ginecoide"
            else:
                print("error final2bonus1")
                return "error icc"
        else:
            print("error sexo")
            return "error sexo"

    def icc_texto(icc):
        if icc == "androide":
            return f"usted tiene mayor riesgo para el desarrollo de \n\n\n       " \
                   f"enfermedades crónico-degenerativas debido a la \n\n\n       " \
                   f"acumulación de grasa visceral"
        elif icc == "ginecoide":
            return f"usted tiene mayor riesgo problemas de retorno \n\n\n       " \
                   f"venoso"

    def mlg_medic(mlg, sexo):
        fmlg = float(mlg)
        if sexo == "hombre":
            mlgh = [18, 20, 22, 25]
            dato2 = min(mlgh, key=lambda x: abs(x - fmlg))
            if dato2 == 18:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 20:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 22:
                print("Marcadamente musculoso ")
                return "marcadamente musculoso"
            if dato2 == 25:
                print("No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso de "
                      "agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return f"en un rango que no se logra normalmente sin \n\n\n       " \
                       f"levantar pesas / límite superior de la \n\n\n       " \
                       f"musculatura obtenida sin uso de agentes \n\n\n       " \
                       f"fármaco-lógicos, por loque el MLG podría  \n\n\n       " \
                       f"llegar a 40"
            else:
                print("error final2bonus1")
                return "error mlg"
        elif sexo == "mujer":
            mlgm = [13, 15, 17, 22]
            dato2 = min(mlgm, key=lambda x: abs(x - fmlg))
            if dato2 == 13:
                print("Complexión ligera con poca musculatura")
                return "con complexion ligera con poca musculatura"
            if dato2 == 15:
                print("Musculatura promedio")
                return "con musculatura promedio"
            if dato2 == 17:
                print("Marcadamente musculoso ")
                return "marcadamente musculosa"
            if dato2 == 22:
                print(
                    "No se logra normalmente sin levantar pesas / Límite superior de la musculatura obtenida sin uso "
                    "de agentes fármaco-lógicos, por lo que el MLG podría llegar a 40")
                return "con medidas que no se logran normalmente \n\n\n      " \
                       "sin levantar pesas / límite superior de \n\n\n      " \
                       "la musculatura obtenida sin uso de \n\n\n      " \
                       "agentes fármaco-lógicos, por lo que el \n\n\n      " \
                       "MLG podría llegar a 40"
            else:
                print("error final2bonus1")

    def iamb_medic(iamb):
        fiamb = float(iamb)
        if fiamb < 5:
            print("Bajo nivel de musculatura o disminución")
            return "un bajo nivel de musculatura o disminucion"
        elif fiamb in range(5, 15):
            print("Masa muscular debajo del promedio")
            return "una masa muscular debajo del promedio"
        elif fiamb in range(16, 85):
            print("Masa muscular promedio")
            return "una masa muscular promedio"
        elif fiamb in range(86, 95):
            print("Masa muscular arriba del promedio o hipertrofia muscular")
            return "una masa muscular arriba del promedio o \n\n\n      " \
                   "hièrtrofia muscular"
        elif fiamb > 95:
            print("Masa muscular alta - hipertrofia muscular")
            return "una masa muscular alta - hipertrofia \n\n\n      " \
                   "muscular"
        else:
            print("error iamb")
            return "error iamb"

    def complexion_medic(complexion, sexo):
        fcomplexion = float(complexion)
        if sexo == "hombre":
            if fcomplexion > 10.4:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.6 < fcomplexion < 10.3:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.5:
                print("complexion grande")
                return "complexion grande"
        elif sexo == "mujer":
            if fcomplexion > 10.9:
                print("complexion pequeña")
                return "complexion pequeña"
            elif 9.9 < fcomplexion < 10.8:
                print("complexion mediana")
                return "complexion mediana"
            elif fcomplexion < 9.8:
                print("complexion grande")
                return "complexion grande"

    def peso_ideal_medic(peso, peso_ideal):
        fpeso = float(peso)
        fpeso_ideal = float(peso_ideal)
        print(fpeso_ideal)
        ## abajo esta % de peso ideal, falta este dato de salida
        dato3 = int((fpeso * 100) / fpeso_ideal)
        print(dato3)
        if dato3 < 60:
            print("Malnutrición severa")
            return "malnutricion severa"
        elif 60 <= dato3 <= 89:
            print("Malnutrición moderada")
            return "malnutricion moderada"
        elif 90 <= dato3 <= 109:
            print("Normalidad")
            return "nutricion promedio"
        elif 110 <= dato3 <= 120:
            print("Sobrepeso")
            return "sobrepeso"
        elif dato3 > 120:
            print("Obesidad")
        else:
            print("error")

    imc_info = imc_medic(imc)
    icc_info = icc_medic(icc, sexo)
    icc_text = icc_texto(icc_info)
    mlg_info = mlg_medic(mlg, sexo)
    iamb_info = iamb_medic(iamb)
    complexion_info = complexion_medic(complexion, sexo)
    peso_ideal_info = peso_ideal_medic(peso, peso_ideal)

    pdf.multi_cell(0, 20, f"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n       "
                          f"con un indice de masa corporal de "
                          f"{imc} usted califica que \n\n\n       posee {imc_info}\n\n\n\n\n\n       "
                          f"con un indice cintura cadera de {icc} usted califica como \n\n\n       "
                          f"{icc_info} y {icc_text}\n\n\n\n\n\n       "
                          f"con un indice de masa libre de grasa de {mlg} usted esta \n\n\n       "
                          f"{mlg_info}\n\n\n\n\n\n       "
                          f"con un indice del area muscular del brazo de {iamb} \n\n\n       "
                          f"en persentiles se puede afirmar que usted posee \n\n\n       "
                          f"{iamb_info}\n\n\n\n\n\n       "
                          f"con un indice de complexion de {complexion} usted posee una \n\n\n       "
                          f"{complexion_info}\n\n\n\n\n\n       "
                          f"con un porcentaje de peso ideal del {peso_ideal} usted posee \n\n\n       "
                          f"{peso_ideal_info}")

    pdf.output("new.pdf", "F")

if __name__ == "__main__":
    create_pdf("new.pdf")