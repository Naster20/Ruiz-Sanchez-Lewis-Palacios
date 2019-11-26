# CONVERSOR N°1 DE BOLETA DE TIENDA
cliente=""
producto1=""
producto2=""
producto3=""
cant_prod_1=0
cant_prod_2=0
cant_prod_3=0
costo_uni_prod_1=0.0
costo_uni_prod_2=0.0
costo_uni_prod_3=0.0
total=0.0
# INPUT
cliente=input("Ingrese el cliente:")# input() devuelve un str
producto1=input("Ingrese producto 1 :")# input() devuelve un str
producto2=input("Ingrese producto 2 :")# input() devuelve un str
producto3=input("Ingrese producto 3 :")# input() devuelve un str
cant_prod_1=int(input("Ingrese cantidad 1° producto :"))# input() devuelve un int
cant_prod_2=int(input("Ingrese cantidad 2° producto :"))# input() devuelve un int
cant_prod_3=int(input("Ingrese cantidad 3° producto :"))# input() devuelve un int
costo_uni_prod_1=float(input("Ingrese costo uni del 1° producto :"))# input() devuelve un float
costo_uni_prod_2=float(input("Ingrese costo uni del 2° producto :"))# input() devuelve un float
costo_uni_prod_3=float(input("Ingrese costo uni del 3° producto :"))# input() devuelve un float
# PROCESSING
total=(cant_prod_1*costo_uni_prod_1+cant_prod_2*costo_uni_prod_2+cant_prod_3*costo_uni_prod_3)
# OUTPUT
print("##################################")
print("#         BOLETA DE TIENDA       #")
print("##################################")
print("# Cliente : ",cliente,"          #")
print("# Producto 1 : ",producto1,"         #")
print("# Producto 2 : ",producto2,"         #")
print("# Producto 3 : ",producto3,"         #")
print("# Cantidad producto 1 : ",cant_prod_1,"             #")
print("# Cantidad producto 2 : ",cant_prod_2,"             #")
print("# Cantidad producto 3 : ",cant_prod_3,"             #")
print("# Costo Unitario producto 1 : S/.",costo_uni_prod_1,"#")
print("# Costo Unitario producto 2 : S/.",costo_uni_prod_2,"#")
print("# Costo Unitario producto 3 : S/.",costo_uni_prod_3,"#")
print("# Total: S/. ",total,"           #")
print("# COMPRADOR COMPULSIVO :",comprador_compulsivo,"#")
print("##################################")
#Fin_if

# CONVERSOR N°2 DE NOTAS
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
#Fin_if

# CONVERSOR N°3  DE OTROS GASTOS
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
#Fin_if

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
#Fin_if


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
#Fin_if


# CONVERSOR N°6 DE TOTAL DE CAPITAL CONTABLE
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
#Fin_if


# CONVERSOR N°7 DE PARTICIPACION CONTROLADORA
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
#Fin_if

# CONVERSOR N°8 DE VALOR DE LIBROS
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
#Fin_if

# CONVERSOR N°9 INDICE DE MASA CORPORAL
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
#Fin_if


# CONVERSOR N°10  DE DESCUENTO
#DECLARACION
cliente=""
articulo=""
precio=0.0
descuento=0.0
total=0.0
#IMPUT
cliente=input("Ingrese nombre de cliente : ")# input() devuelve un str
articulo=input("Ingrese articulo : ")# input() devuelve un str
precio=float(input("Ingrese el precio del articulo : "))# input() devuelve un float
descuento=float(input("Ingrese el descuento : "))# input() devuelve un float
#PROCESSING
descuento=((precio)*descuento/100)
total=(precio-descuento)

#OUTPUT
print("#####################################")
print("#            DESCUENTO              #")
print("#####################################")
print("# NOMBRE DEL CLIENTE :",cliente,"   #")
print("# NOMBRE DEL ARTICULO : ",articulo,"#")
print("# PRECIO DEL ARTICULO :",precio,"   #")
print("# DESCUENTO =",descuento,"          #")
print("# TOTAL =",total,"                  #")
print("#  BUEN PRECIO :", buen_precio,"       #")
print("#####################################")
#Fin_if
