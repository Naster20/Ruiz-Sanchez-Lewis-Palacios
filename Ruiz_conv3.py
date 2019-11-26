# CONVERSOR DE OTROS GASTOS
#DECLARACION
persona=""
otros_gastos_2005=0.0
otros_gastos_2006=0.0
otros_gastos_2007=0.0
otros_gastos_2008=0.0
total_de_otros_gastos=0.0
#INPUT
persona=input("Ingrese nombre de la persona:")
otros_gastos_2005=float(input("Ingrese el gasto del 2005:"))# input() devuelve un float
otros_gastos_2006=float(input("Ingrese el gasto del 2006:"))# input() devuelve un float
otros_gastos_2007=float(input("Ingrese el gasto del 2007:"))# input() devuelve un float
otros_gastos_2008=float(input("Ingrese el gasto del 2008:"))# input() devuelve un float
#PROCESSING
total_de_otros_gastos=(otros_gastos_2005+otros_gastos_2006+otros_gastos_2007+otros_gastos_2008)
#DETECTOR
# Sera gasto excesivo si total > 1500
gasto_excesivo=(total_de_otros_gastos > 1500)
#OUTPUT
print("#############################################")
print("#                OTROS GASTOS               #")
print("#############################################")
print("# PERSONA :",persona,"                        #")
print("# OTROS GASTOS 2005: ",otros_gastos_2005,"    #")
print("# OTROS GASTOS 2006: ",otros_gastos_2006,"    #")
print("# OTROS GASTOS 2007: ",otros_gastos_2007,"    #")
print("# OTROS GASTOS 2008: ",otros_gastos_2008,"    #")
print("# TOTAL DE OTROS GASTOS =",total_de_otros_gastos,"#")
print("# GASTO EXCESIVO : ", gasto_excesivo,"       #")
print("#############################################")
