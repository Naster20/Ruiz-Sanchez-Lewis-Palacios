# CONVERSOR N°5 DE FLUJO DE OPERACION
#DECLARACION
persona=""
flujo_de_operacion_2005=0.0
flujo_de_operacion_2006=0.0
flujo_de_operacion_2007=0.0
total_flujo_de_operacion=0.0
#INPUT
persona=input("Ingrese nombre de la persona: ")# input() devuelve un str
flujo_de_operacion_2005=float(input("Ingrese el flujo de operacion del 2005:"))# input() devuelve un float
flujo_de_operacion_2006=float(input("Ingrese el flujo de operacion del 2006:"))# input() devuelve un float
flujo_de_operacion_2007=float(input("Ingrese el flujo de operacion del 2007:"))# input() devuelve un float
#PROCESSING
total_flujo_de_operacion=(flujo_de_operacion_2005+flujo_de_operacion_2006+flujo_de_operacion_2007)
#DETECTOR
#flujo de operacion normal si total de flujo < 1400
flujo_de_operacion_normal=(total_flujo_de_operacion < 1400)
#OUTPUT
print("#############################################")
print("#             FLUJO DE OPERACION            #")
print("#############################################")
print("# PERSONA :",persona,"                        #")
print("# FLUJO DE OPERACION 2005: ",flujo_de_operacion_2005,"    #")
print("# FLUJO DE OPERACION 2006: ",flujo_de_operacion_2006,"    #")
print("# FLUJO DE OPERACION 2007: ",flujo_de_operacion_2007,"    #")
print("# TOTAL DEL FLUJO DE OPERACION =",total_flujo_de_operacion,"#")
print("# FLUJO DE OPERACION NORMAL : ",flujo_de_operacion_normal," #")
print("#############################################")

