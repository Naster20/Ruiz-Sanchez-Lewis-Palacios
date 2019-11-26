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
#DETECTOR
# Sera comprador compulsivo cuando el total > 150
comprador_compulsivo=(total >=100)
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

