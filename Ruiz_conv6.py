# CONVERSOR DE TOTAL DE CAPITAL CONTABLE
#DECLARACION
persona=""
capital_contable_2005=0.0
capital_contable_2006=0.0
capital_contable_2007=0.0
total_capital_contable=0.0
#INPUT
persona=input("Ingrese nombre de la persona: ")# input() devuelve un str
capital_contable_2005=float(input("Ingrese el capital contable del 2005:"))# input() devuelve un float
capital_contable_2006=float(input("Ingrese el capital contable del 2006:"))# input() devuelve un float
capital_contable_2007=float(input("Ingrese el capital contable del 2007:"))# input() devuelve un float
#PROCESSING
total_capital_contable=(capital_contable_2005+capital_contable_2006+capital_contable_2007)
#DETECTOR
#capital contable normal si el total > 3000
capital_contable_normal=(total_capital_contable > 3000)
#OUTPUT
print("#############################################")
print("#             CAPITAL CONTABLE              #")
print("#############################################")
print("# PERSONA :",persona,"                        #")
print("# CAPITAL CONTABLE 2005: ",capital_contable_2005,"    #")
print("# CAPITAL CONTABLE 2006: ",capital_contable_2006,"    #")
print("# CAPITAL CONTABLE 2007: ",capital_contable_2007,"    #")
print("# TOTAL DEL CAPITAL CONTABLE S/. =",total_capital_contable,  "#")
print("# CAPITAL CONTABLE NORMAL S/. =",capital_contable_normal,"    #")
print("#############################################")
