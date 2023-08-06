if __name__ == '__main__':

    percentil_u = float(input("Enter the body fat percentage (5 to 95): "))
    edad_u = input("Ingrese su edad: ")

    percentil = [5, 10, 15, 25, 50, 75, 85, 90, 95]
    edad_min = ['18', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70']
    edad_max = ['24', '29', '34', '39', '44', '49', '54', '59', '64', '69', '74']
    tabla = [8, 9, 10, 12, 16, 20, 23, 25, 28], [9, 10, 11, 13, 18, 23, 25, 26, 29], [16, 17, 18, 20, 23, 26, 27, 28, 30], [15, 17, 18, 20, 23, 25, 27, 27, 29], [14, 16, 18, 21, 26, 30, 32, 34, 36], [15, 17, 19, 21, 26, 30, 32, 34, 36], [15, 17, 19, 22, 27, 31, 30, 35, 37], [15, 18, 20, 22, 27, 31, 30, 35, 37], [16, 18, 20, 22, 27, 31, 33, 35, 37], [13, 16, 18, 21, 26, 30, 33, 35, 37], [13, 16, 18, 21, 26, 30, 33, 34, 36]

    closest_body_fat = min(percentil, key=lambda x: abs(x - percentil_u))

    for i in percentil:

        if  closest_body_fat == i:

            posicion_per = percentil.index(i)

            for a in zip(edad_min, edad_max):

                #print("min: ", a[0])
                #print("max: ", a[1])

                if edad_u >= a[0] and edad_u <= a[1]:

                    posicion_edad = edad_min.index(a[0])

                    print("GOD: ", tabla[posicion_edad][posicion_per])