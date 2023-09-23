print ("ingrese los valores con |,  que usted desee para calcular el rectangulo")
largo1_rectangulo1 = float(input("Ingrese el largo  del primer rectángulo\n"). replace("|", ""))
ancho1_rectangulo1 = float(input("Ingrese el  ancho del primer rectángulo\n"). replace("|", ""))
largo2_rectangulo2 = float(input("Ingrese el  largo del segundo rectángulo\n"). replace("|", ""))
ancho2_rectangulo2 = float(input("Ingrese el  ancho del segundo rectángulo\n"). replace("|", ""))

rectangulo1 = largo1_rectangulo1,ancho1_rectangulo1
rectangulo2 = largo2_rectangulo2,ancho2_rectangulo2

rectangulo1= largo1_rectangulo1*ancho1_rectangulo1
rectangulo2= largo2_rectangulo2*ancho2_rectangulo2
 
print (rectangulo1)
print(rectangulo2)