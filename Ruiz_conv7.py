# CONVERSOR DE PARTICIPACION CONTROLADORA
#DECLARACION
persona=""
participacion_controladora_2005=0.0
participacion_controladora_2006=0.0
participacion_controladora_2007=0.0
total_participacion_controladora=0.0
#INPUT
persona=input("Ingrese nombre de la persona: ")# input() devuelve un str
participacion_controladora_2005=float(input("Ingrese monto de participacion controladora del 2005:"))# input() devuelve un float
participacion_controladora_2006=float(input("Ingrese monto de participacion controladora del 2006:"))# input() devuelve un float
participacion_controladora_2007=float(input("Ingrese monto de participacion controladora del 2007:"))# input() devuelve un float
#PROCESSING
total_participacion_controladora=(participacion_controladora_2005+participacion_controladora_2006+participacion_controladora_2007)
#DETECTOR
#PARTICIPAACION CONTROLADORA NORMAL SI EL TOTAL > 2000
participacion_controladora_normal=(total_participacion_controladora> 2000)
#OUTPUT
print("#############################################")
print("#         PARTICIPACION CONTROLADORA        #")
print("#############################################")
print("# PERSONA :",persona,"                        #")
print("# PARTICIPACION CONTROLADORA 2005: ",participacion_controladora_2005,"    #")
print("# PARTICIPACION CONTROLADORA 2006: ",participacion_controladora_2006,"    #")
print("# PARTICIPACION CONTROLADORA 2007: ",participacion_controladora_2007,"    #")
print("# TOTAL DE PARTICIPACION CONTROLADORA =",total_participacion_controladora,"#")
print("# PARTICIPACION CONTROLADORA NORMAL : ",participacion_controladora_normal," #")
print("#############################################")

