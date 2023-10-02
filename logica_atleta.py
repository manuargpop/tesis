from datetime import datetime
from dateutil.relativedelta import relativedelta
from math import log

def logica_imc_atl(self, MainWindow):
    dato1 = float(altura)
    dato2 = float(peso)
    IMC_atl = dato2/dato1**2

##manuargpop: problema, existen mas de 6 pliegues, preguntar al profesor manuel
def logica_porcentaje_grasa_atl(self, MainWindow):
    dato1=float(pliegue_triceps)
    dato2=float(pliegue_subescapular)
    dato3=float(pliegue_cresta_iliaca)
    dato4=float(pliegue_abdominal)
    dato5=float(pliegue_muslo_anterior)
    dato6=float(pliegue_pantorrilla_medial)
    if sexo == hombre:
        porcentaje_grasa_atl = ((dato1+dato2+dato3+dato4+dato5+dato6)*0.1051)+2.585
    elif sexo == mujer:
        porcentaje_grasa_atl = ((dato1+dato2+dato3+dato4+dato5+dato6)*0.1548)+3.580
    else:
        print("error en sexo")
def logica_mlg_atl(self, MainWindow):
    dato1 = float(peso)
    dato2 = float(porcentaje_grasa_atl)
    dato3 = float(altura)
    MLG_atl = (dato1*(((100-dato2)/100)+6.1*(1.8*dato3)))/dato3**2

def logica_camb__iamb_atl(self, MainWindow):
    sexo = sexo

    def get_iamb(sexo):
        if sexo == "hombre":
            dato1 = float(circunferencia_brazo_rela)
            dato2 = float(pliegue_triceps)
            dato3 = 0.31416*(dato2/10)
            camb = (((dato1-dato3)**2)/(4*3.1416))-10.0

            fecha_de_nacimiento = "fecha"
            fecha_de_medicion = "fecha m"

            fecha_nacimiento = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
            porcentaje_g = camb
            edad_u = float(relativedelta(fecha_de_medicion, fecha_nacimiento))

            edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
            edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
            tabla = [34.2, 37.3, 39.6, 42.7, 49.4, 57.1, 61.8, 65.0, 72.0], [36.6, 39.9, 42.4, 46.0, 53.0, 61.4, 66.1, 68.9, 74.5], [37.9, 40.9, 43.4, 47.3, 54.4, 63.2, 67.6, 70.8, 76.1], [38.5, 42.6, 44.6, 47.9, 55.3, 64.0, 69.1, 72.7, 77.6], [38.4, 42.1, 45.1, 48.7, 56.0, 64.0, 68.5, 71.6, 77.0], [37.7, 41.3, 43.7, 47.9, 55.2, 63.3, 68.4, 72.2, 76.2], [36.0, 40.0, 42.7, 46.6, 54.0, 62.7, 67.0, 70.4, 77.4], [36.5, 40.8, 42.7, 46.7, 54.3, 61.9, 66.4, 69.6, 75.1], [34.5, 38.7, 41.2, 44.9, 52.1, 60.0, 64.8, 67.5, 71.6], [31.4, 35.8, 38.4, 42.3, 49.1, 57.3, 61.2, 64.3, 69.4], [29.7, 33.8, 36.1, 40.2, 47.0, 54.6, 59.1, 62.1, 67.3]
            percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

            for edad in zip(edad_min, edad_max):

                if edad_u >= edad[0] and edad_u <= edad[1]:

                    posicion_edad = edad_min.index(edad[0])
                    percentage = tabla[posicion_edad]

                    for valor in percentage:
                        closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                        if closest_body_fat == valor:
                            ubicacion = percentage.index(valor)
                            iamb_atl = (str(percentil[ubicacion]))
                            return iamb_atl
        elif sexo == "mujer":
            dato1 = float(circunferencia_brazo_rela)
            dato2 = float(pliegue_triceps)
            dato3 = 0.31416*(dato2/10)
            camb = (((dato1-dato3)**2)/(4*3.1416))-6.5

            fecha_de_nacimiento = "fecha"
            fecha_de_medicion = "fecha m"

            fecha_nacimiento = datetime.strptime(fecha_de_nacimiento, "%d/%m/%Y")
            porcentaje_g = camb
            edad_u = float(relativedelta(fecha_de_medicion, fecha_nacimiento))

            edad_min = [18, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
            edad_max = [24, 29, 34, 39, 44, 49, 54, 59, 64, 69, 74]
            tabla = [19.5, 21.5, 22.8, 23.5, 28.3, 33.1, 36.4, 39.0, 44.2], [20.5, 21.9, 23.1, 25.2, 29.4, 34.9, 38.5, 41.9, 47.8], [21.1, 23.0, 24.2, 26.3, 30.9, 36.8, 41.2, 44.7, 51.3], [21.1, 23.4, 24.7, 27.3, 31.8, 38.7, 43.1, 46.1, 54.2], [21.3, 23.4, 25.5, 27.5, 32.3, 39.8, 45.8, 49.5, 55.8], [21.6, 23.1, 24.8, 27.4, 32.5, 39.5, 44.7, 48.4, 56.1], [22.2, 24.6, 25.7, 28.3, 33.4, 40.4, 46.1, 49.6, 55.6], [22.8, 24.7, 26.5, 28.7, 33.7, 42.3, 47.3, 52.1, 58.8], [22.4, 24.5, 26.3, 29.2, 34.5, 41.1, 45.6, 49.1, 55.1], [21.9, 24.5, 26.2, 28.9, 34.6, 41.6, 46.3, 49.6, 56.5], [22.2, 24.4, 26.0, 28.8, 34.3, 41.8, 46.4, 49.2, 54.6]
            percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]

            for edad in zip(edad_min, edad_max):

                if edad_u >= edad[0] and edad_u <= edad[1]:

                    posicion_edad = edad_min.index(edad[0])
                    percentage = tabla[posicion_edad]

                    for valor in percentage:
                        closest_body_fat = min(percentage, key=lambda x: abs(x - porcentaje_g))
                        if closest_body_fat == valor:
                            ubicacion = percentage.index(valor)
                            iamb_atl = (str(percentil[ubicacion]))
                            return iamb_atl
        
    iamb_atle = get_iamb(sexo)

def complexion_atl(self, MainWindow):
    dato1 = float(altura)
    dato2 = float(circunferencia_muñeca)
    complexion_atl = dato1/dato2

def somatotipo_atl(self, MainWindow):
    ##manuargpop: inicia el de endomorfo
    dato1 = float(altura)
    dato2 = float(pliegue_triceps)
    dato3 = float(pliegue_subescapular)
    dato4 = float(pliegue_supraespinal)
    dato5 = dato1 + dato2 + dato3
    dato6 = dato5 * (170.18/dato1)
    endomorfia = (0.1451*dato6) - (0.00068*(dato6**2)) + (0.0000014*(dato6**3)) - 0.7182
    ##manuargpop: un resultado tipico seria 2.6 o 2.61

    ##manuargpop: inicia el de mesomorfo
    dato7 = float(diametro_humero)
    dato8 = float(diametro_femur)

    dato9 = float(perimetro/circunferencia_brazo_relajado)
    dato10 = float(dato9 - (dato2/10))

    dato11 = float(perimetro/circunferencia_pantorrilla)
    dato12 = float(pliegue_pantorilla)
    dato13 = float(dato11 - (dato12/10))
    mesomorfia = (0.858 * dato7) + (0.601 * dato8) + (0.188 * dato10) + (0.161 * dato13) - (0.131 * dato1) + 4.50

    ##manuargpop: inicia ectomorfia
    def getectomorfia(dato12):
        if dato12 > 40.75:
            ectomorfiar = (dato12 * 0.732) - 28.58
            return ectomorfiar
        elif 40.75 >= dato12 >= 38.25:
            ectomorfiar = (dato12 * 0.463) - 17.63
            return ectomorfiar
        elif dato12 < 38.25:
            ectomorfiar = 0.1
            return ectomorfiar
        else:
            print("error ectomorfia")

    dato11 = float(peso)
    dato12 = dato1/(dato11**(1/3))
    ectomorfia = getectomorfia(dato12)

    ##inicia x y y en el plano delsomatotipo
    datox = ectomorfia - endomorfia
    datoy = 2*mesomorfia - (endomorfia+ectomorfia)
    ##esto se usara para una futura grafica de somatotipo

def fraccionamiento_corporal_atl(self, MainWindow):
    sexo = sexo

    def getcas(sexo):
        if sexo == hombre:
            return 68.308
        elif sexo == mujer:
            return 73.074
        else:
            print("error sexo")
            return ("error sexo")

    def gettsk(sexo):
        if sexo == hombre:
            return 2.07
        elif sexo == mujer:
            return 1.96
        else:
            print("error sexo")
            return ("error sexo")

    ##inicio masa de la piel

    cas = getcas(sexo)
    dato1 = peso
    dato2 = altura##(en_centimetros)

    sa = cas * (dato1**0.425) * (dato2**0.725) / 10000
    tsk = gettsk(sexo)

    masa_piel = sa * tsk * 1.05

    ##inicio prediccion de la masa osea

    dato3 = perimetro_cefalico
    z_osea_cabeza = (dato3 - 57) / 1.44
    m_osea_cabeza = (z_osea_cabeza * 0.18) + 1.20

    dato4 = diametro_biacromial
    dato5 = diametro_biiliocristal
    dato6 = diametro_humero
    dato7 = diametro_femur

    scorporal = (dato4 + dato5 + dato6 +dato7)

    zcorporal = ((scorporal * (170.18/dato2)) - 98.88) / 5.33

    mcorporal = ((zcorporal * 1.34) + 6.70) / (170.18/dato2)**3

    total_masa_osea = m_osea_cabeza + mcorporal

    ##inicio prediccion dle tegido adiposo

    dato8 = pliegue_cutaneo_triceps
    dato9 = pliegue_cutaneo_subescapular
    dato10 = pliegue_cutaneo_supraespinal
    dato11 = pliegue_cutaneo_abdominal
    dato12 = pliegue_cutaneo_muslo_frontal
    dato13 = pliegue_cutaneo_pantorrilla_medial

    sadiposa = dato8 + dato9 + dato10 + dato11 + dato12 + dato13

    zadiposa = ((sadiposa * (170.18/dato2))-116.41)/34.79

    madiposa = ((zadiposa * 5.85) + 25.4) / (170.18 / dato2)**3

    ##inicio prediccion de la masa muscular

    cbrc = circunferencia_brazo_relajado - (3.14 *(dato8 / 10))
    ca = circunferencia_antebrazo
    cmfc = circunferencia_muslo - (3.14 * (dato12 / 10))
    cpmc = circunferencia_pantorrilla - (3.14 * (dato13 / 10))
    ctc = circunferencia_torax - (3.14 * (dato9 / 10))

    smus = cbrc + ca + cmfc + cpmc + ctc

    zmus = (smus * (170.18 / dato2) - 207.21) / 13.74

    mmusculae = ((zmus * 5.4) + 24.5) / (170.18 / dato2)**3

    ##inicia prediccion de masa residual
    dato14 = profundidad_anteroposterior_tórax ##esta en diametros
    dato15 = diametro_transversal_torax
    dato16 = circunferencia_cintura - (3.14 * dato11)
    sres = (dato14 + dato15 + dato16)
    hs = estatura_sentado
    zres = ((sres * (89.92 / hs)) - 109.35) / 7.08

    mres = ((zres * 1.24) + 1.60) / (89.92 / hs)**3

    ##inicio masa total
    masa_total = mpiel + madiposa + mmusculae + mosea + mresidual

##inicio indice cormico
def indice_cormico_atl(self, MainWindow):
    dato1 = estatura
    dato2 = estatura_sentado
    icor = (dato2 / dato1) * 100

##inicio longitud relativa de la extremidad superior

def longitud_relativa_extremidad_superior_atl(self, MainWindow):
    dato1 = longitud_acromio_dedal ##en cm
    dato2 = estatura
    lres = (dato1 / dato2) * 100

    ##esto es para medica
    if lres <= 44.9:
        print("usted califica en braquibraquial, osea, tiene extremidades superiores cortas")
    elif 45 < lres < 46.9:
        print("usted califica en mesobraquial, osea, tiene extremidades superiores intermedias")
    elif lres >= 47:
        print("usted califica en macrobraquial, osea, tiene extremidades superiores largas")

##inicio indice esqueletico
def indice_esqueletico_atl(self, MainWindow):
    dato1 = estatura
    dato2 = estatura_sentado
    ie = ((dato1 - dato2) / dato2) * 100

##inicio envergadura relativa
def envergadura_relativa_atl(self, MainWindow):
    dato1 = envergadura
    dato2 = estatura
    er = (dato1 / dato2) * 100
