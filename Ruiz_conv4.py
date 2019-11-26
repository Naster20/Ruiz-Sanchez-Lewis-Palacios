# CONVERSOR N°4 DE UTILIDAD BRUTA
#DECLARACION
persona=""
utilidad_bruta_2005=0.0
utilidad_bruta_2006=0.0
utilidad_bruta_2007=0.0
total_de_utilidad_bruta=0.0
#INPUT
persona=input("Ingrese nombre de la persona:")# input() devuelve un str
utilidad_bruta_2005=float(input("Ingrese la utilidad bruta del 2005:"))# input() devuelve un float
utilidad_bruta_2006=float(input("Ingrese la utilidad bruta del 2006:"))# input() devuelve un float
utilidad_bruta_2007=float(input("Ingrese la utilidad bruta del 2007:"))# input() devuelve un float
#PROCESSING
total_de_utilidad_bruta=(utilidad_bruta_2005+utilidad_bruta_2006+utilidad_bruta_2007)
#DETECTOR
# Sera exceso de utilidad si total > 1000
exceso_de_utildad=(total_de_utilidad_bruta > 1000)
#OUTPUT
print("#############################################")
print("#               UTILIDAD BRUTA              #")
print("#############################################")
print("# PERSONA :",persona,"                        #")
print("# UTLIDAD BRUTA 2005: ",utilidad_bruta_2005,"    #")
print("# UTLIDAD BRUTA 2006: ",utilidad_bruta_2006,"    #")
print("# UTLIDAD BRUTA 2007: ",utilidad_bruta_2007,"    #")
print("# TOTAL DE UTILIDAD BRUTA =",total_de_utilidad_bruta,"#")
print("# EXCESO DE UTILIDAD : ", exceso_de_utildad,"         #")
print("#############################################")


