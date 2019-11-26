# CONVERSOR DE VALOR DE LIBROS
#DECLARACION
persona=""
valor_en_libros_por_cpo_2005=0.0
valor_en_libros_por_cpo_2006=0.0
valor_en_libros_por_cpo_2007=0.0
valor_en_libros_por_cpo_2008=0.0
total_de_valor_en_libros_por_cpo=0.0
#INPUT
persona=input("Ingrese nombre de la persona: ")# input() devuelve un str
valor_en_libros_por_cpo_2005=float(input("Ingrese monto de valor de libros del 2005:"))# input() devuelve un float
valor_en_libros_por_cpo_2006=float(input("Ingrese monto de valor de libros del 2006:"))# input() devuelve un float
valor_en_libros_por_cpo_2007=float(input("Ingrese monto de valor de libros del 2007:"))# input() devuelve un float
valor_en_libros_por_cpo_2008=float(input("Ingrese monto de valor de libros del 2008:"))# input() devuelve un float
#PROCESSING
total_de_valor_en_libros_por_cpo=(valor_en_libros_por_cpo_2005+valor_en_libros_por_cpo_2006+valor_en_libros_por_cpo_2007+valor_en_libros_por_cpo_2008)
#DETECTOR
#VALOR DE LIBROS NORMAL SI EL TOTAL > 1500
valor_en_libros_por_cpo_normal=(total_de_valor_en_libros_por_cpo > 1500)
#OUTPUT
print("#############################################")
print("#          VALOR EN LIBROS POR CPO          #")
print("#############################################")
print("# PERSONA :",persona,"                      #")
print("# VALOR EN LIBROS POR CPO 2005: ",valor_en_libros_por_cpo_2005,"    #")
print("# VALOR EN LIBROS POR CPO 2006: ",valor_en_libros_por_cpo_2006,"    #")
print("# VALOR EN LIBROS POR CPO 2007: ",valor_en_libros_por_cpo_2007,"    #")
print("# VALOR EN LIBROS POR CPO 2008: ",valor_en_libros_por_cpo_2008,"    #")
print("# TOTAL DE VALOR EN LIBROS POR CPO =",total_de_valor_en_libros_por_cpo,"#")
print("# VALOR DE LIBROS NORMAL :",valor_en_libros_por_cpo_normal,"   #")
print("#############################################")
