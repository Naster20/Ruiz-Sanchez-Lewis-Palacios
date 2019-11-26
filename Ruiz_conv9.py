# CONVERSOR INDICE DE MASA CORPORAL
#DECLARACION
nombre=""
edad=0
talla=0.0
peso=0.0
indice_de_masa_corporal=0.0
#IMPUT
nombre=input("Ingrese Nombre del Paciente : ")# input() devuelve un str
edad=int(input("Ingrese su Edad : "))# input() devuelve un int
talla=float(input("Ingrese su talla : "))# input() devuelve un float
peso=float(input("Ingrese su Peso : "))# input() devuelve un float
#PROCESSING
indice_de_masa_corporal=(peso/(talla)**2)
#DETECTOR
# PERSONA OBESA SI EL INDICE DE MASA CORPORAL > 30
persona_obesa=(indice_de_masa_corporal > 30)
#OUTPUT
print("#############################################")
print("#          INDICE DE MASA CORPORAL          #")
print("#############################################")
print("# NOMBRE :",nombre,"                      #")
print("# EDAD : ",edad,"    #")
print("# TALLA  : ",talla,"    #")
print("# PESO  : ",peso,"    #")
print("INDICE DE MASA CORPORAL =",indice_de_masa_corporal,"#")
print("# PERSONA OBESA :",persona_obesa,"          #")
print("#############################################")

