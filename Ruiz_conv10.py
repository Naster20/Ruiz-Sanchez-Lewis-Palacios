# CONVERSOR DE DESCUENTO
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
#DETECTOR
# BUEN PRECIO SI EL TOTAL > A 1000
buen_precio=(total > 1000)
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

