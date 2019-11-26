# CONVERSOR DE NOTAS
alumno=""
nota1=0.0
nota2=0.0
nota3=0.0
prom=0.0

# INPUT
alumno=input("Ingrese alumno:")# input() devuelve un str
nota1=float(input("Ingrese nota 1:")) # input() devuelve un float
nota2=float(input("Ingrese nota 2:")) # input() devuelve un float
nota3=float(input("Ingrese nota 3:")) # input() devuelve un float

# PROCESSING
prom=(nota1+nota2+nota3)/3
#DETECTOR
#Sera alumno bueno si su promedio >= 14.5
alumno_bueno=(prom >= 14.5)

# OUTPUT
print("###################################")
print("#              NOTAS              #")
print("###################################")
print("#""           Nota 1=",nota1,"           #")
print("#""           Nota 2=",nota2,"           #")
print("#""           Nota 3=",nota3,"           #")
print("#""Promedio del Alumno: ",alumno," es:",prom,"  #")
print("# Alumno bueno : ", alumno_bueno,"#")
print("###################################")
