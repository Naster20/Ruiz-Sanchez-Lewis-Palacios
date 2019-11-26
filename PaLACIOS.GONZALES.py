#Informacion_de_boleta_de_venta
#DECLARACION
libro_de_auditoria_tributaria=0.0
libro_manual_del_contador=0.0
compendio_laboral=0.0
total=0.0
#INPUT
libro_de_auditoria_tributaria=float(input("Ingrese Precio:"))
libro_manual_del_contador=float(input("Ingrese Precio:"))
compendio_laboral=float(input("Ingrese Precio:"))
#PROCESSING
total=(libro_de_auditoria_tributaria+libro_manual_del_contador+compendio_laboral)
#Detector
#El precio sera correcto si es <800
precio_justo=(total<800)
#OUTPUT
print("###########################")
print("      Boleta de venta      ")
print("###########################")
print("Libro e auditoria tributaria:",libro_de_auditoria_tributaria)
print("Libro manual del contador:",libro_manual_del_contador)
print("Compendio laboral:",compendio_laboral)
print("Total:",total)
print("Precio Justo:",precio_justo)
print("###########################")
#Informacion_de_nro_de_visitas_de_Operating_system
#DECLARACION
ios=0
android=0
windows_phone=0
not_set=0
blackberry=0
nokia=0
total=0
#INPUT
ios=int(input("Visitas de IOS:"))
android=int(input("Visitas de Android:"))
windows_phone=int(input("Visitas de windows phone:"))
not_set=int(input("Visitas not set:"))
blackberry=int(input("Visitas blackberry:"))
nokia=int(input("Visita de Nokia:"))
#PROCESSING
total=(ios+android+windows_phone+not_set+blackberry+nokia)
#Detector
#Tiene un mal indice de visita si tiene <500
indice_de_visitas=(total<500)
#OUTPUT
print("########################################")
print("   Nro de visitas de Operating system   ")
print("########################################")
print("IOS:",ios)
print("Android:",android)
print("Windows phone:",windows_phone)
print("Not set:",not_set)
print("Blackberry:",blackberry)
print("Nokia:",nokia)
print("Total:",total)
print("Indice de Visitas:",indice_de_visitas)
print("#######################################")
#Informacion_de_Nro_de_visitas_de_Social_network
#DECLARACION
google=0
facebook=0
twitter=0
total=0
#INPUT
google=int(input("Visitas de Google:"))
facebook=int(input("Visitas de Facebook:"))
twitter=int(input("Visitas de Twitter:"))
#PROCESSING
total=(google+facebook+twitter)
#Detector
#Seria malo si la cantidad de visitas es <112
cantidad_de_visitas=(total<112)
#OUTPUT
print("######################################")
print("   Nro de visitas de Social network   ")
print("######################################")
print("Google:",google)
print("Facebook:",facebook)
print("Twitter:",twitter)
print("Total:",total)
print("Cantidad de visitas:",cantidad_de_visitas)
print("#####################################")
#Informacion_de_nro_de_visitas_de_Mobile_device_info
#DECLARACION
apple_iphone=0
apple_ipad=0
samsung_gt_s3=0
not_set=0
google_nexus_4=0
samsung_galaxy=0
samsung_gt_s2=0
google_nexus_7=0
htc=0
total=0
#INPUT
apple_iphone=int(input("Visitas de Apple iphone:"))
apple_ipad=int(input("Visitas de Ipad:"))
samsung_gt_s3=int(input("Visitas de Samsung gt s3:"))
not_set=int(input("Visitas not set:"))
google_nexus_4=int(input("Visitas de Google nexus 4:"))
samsung_galaxy=int(input("Vsitias de Samsung Galaxy:"))
samsung_gt_s2=int(input("Visitas de Samsung gt S2:"))
google_nexus_7=int(input("Visitas de Google nexus 7:"))
htc=int(input("Visitas de HTC:"))
#PROCESSING
total=(apple_iphone+apple_ipad+samsung_gt_s3+not_set+google_nexus_4+samsung_galaxy+samsung_gt_s2+google_nexus_7+htc)
#Detector
#Si el indice es <399
indice_de_visitas_de_mobile=(total<399)
#OUTPUT
print("##########################################")
print("   Nro de visitas de Mobile device info   ")
print("##########################################")
print("Apple iphone:",apple_iphone)
print("Apple ipad:",apple_ipad)
print("Samsung GT S3:",samsung_gt_s3)
print("Not set:",not_set)
print("Google nexus 4:",google_nexus_4)
print("Samsung galaxy:",samsung_galaxy)
print("Samsung GT S2:",samsung_gt_s2)
print("Google nexus 7:",google_nexus_7)
print("HTC:",htc)
print("Total:",total)
print("Indice de visitas de mobile:",indice_de_visitas_de_mobile)
print("##########################################")
#Informacion_de_Ventas_netas
#DECLARACION
ventas_netas_05=0
ventas_netas_06=0
ventas_netas_07=0
ventas_netas_08=0
ventas_netas_09=0
ventas_netas_10=0
total=0
#INPUT
ventas_netas_05=float(input("Ventas netas del 2005:"))
ventas_netas_06=float(input("Ventas netas del 2006:"))
ventas_netas_07=float(input("Ventas netas del 2007:"))
ventas_netas_08=float(input("Ventas netas del 2008:"))
ventas_netas_09=float(input("Ventas netas del 2009:"))
ventas_netas_10=float(input("Ventas netas del 2010:"))
#PROCESSING
total=(ventas_netas_05+ventas_netas_06+ventas_netas_07+ventas_netas_08+ventas_netas_09+ventas_netas_10)
#Detector
#Buen año de ventas si el total de ventas es <10000
total_de_ventas=(total<10000)
#OUTPUT
print("##################")
print("   Ventas netas   ")
print("##################")
print("Ventas netas 05:",ventas_netas_05)
print("Ventas netas 06:",ventas_netas_06)
print("Ventas netas 07:",ventas_netas_07)
print("Ventas netas 08:",ventas_netas_08)
print("Ventas netas 09:",ventas_netas_09)
print("Ventas netas 10:",ventas_netas_10)
print("Total:",total)
print("Total de ventas:",total_de_ventas)
print("##################")
#Informacion_de_Costo_de_ventas
#DECLARACION
costo_de_ventas_05=0
costo_de_ventas_06=0
costo_de_ventas_07=0
costo_de_ventas_08=0
costo_de_ventas_09=0
costo_de_ventas_10=0
total=0
#INPUT
costo_de_ventas_05=float(input("Costo de ventas del 2005:"))
costo_de_ventas_06=float(input("Costo de ventas del 2006:"))
costo_de_ventas_07=float(input("Costo de ventas del 2007:"))
costo_de_ventas_08=float(input("Costo de ventas del 2008:"))
costo_de_ventas_09=float(input("Costo de ventas del 2009:"))
costo_de_ventas_10=float(input("Costo de ventas del 2010:"))
#PROCESSING
total=(costo_de_ventas_05+costo_de_ventas_06+costo_de_ventas_07+costo_de_ventas_08+costo_de_ventas_09+costo_de_ventas_10)
#Detector
#Es buen año si el costo de ventas es < 5000
total_de_costos=(total<5000)
#OUTPUT
print("#####################")
print("   Costo de ventas   ")
print("#####################")
print("Costo de ventas 05:",costo_de_ventas_05)
print("Costo de ventas 06:",costo_de_ventas_06)
print("Costo de ventas 07:",costo_de_ventas_07)
print("Costo de ventas 08:",costo_de_ventas_08)
print("Costo de ventas 09:",costo_de_ventas_09)
print("Costo de ventas 10:",costo_de_ventas_10)
print("Total:",total)
print("Total de Costos:",total_de_costos)
print("####################")
#Informacion_de_Utilidad_bruta
#DECLARACION
utilidad_bruta_05=0
utilidad_bruta_06=0
utilidad_bruta_07=0
utilidad_bruta_08=0
utilidad_bruta_09=0
utilidad_bruta_10=0
total=0
#INPUT
utilidad_bruta_05=float(input("Utilidad bruta del 2005:"))
utilidad_bruta_06=float(input("Utilidad bruta del 2006:"))
utilidad_bruta_07=float(input("Utilidad bruta del 2007:"))
utilidad_bruta_08=float(input("Utilidad bruta del 2008:"))
utilidad_bruta_09=float(input("Utilidad bruta del 2009:"))
utilidad_bruta_10=float(input("Utilidad bruta del 2010:"))
#PROCESSING
total=(utilidad_bruta_05+utilidad_bruta_06+utilidad_bruta_07+utilidad_bruta_08+utilidad_bruta_09+utilidad_bruta_10)
#Detector
#Es buen año si la utilidad es <36000
total_de_utilidad=(total<36000)
#OUTPUT
print("####################")
print("   Utilidad Bruta   ")
print("####################")
print("Utilidad bruta 05:",utilidad_bruta_05)
print("Utilidad bruta 06:",utilidad_bruta_06)
print("Utilidad bruta 07:",utilidad_bruta_07)
print("Utilidad bruta 08:",utilidad_bruta_08)
print("Utilidad bruta 09:",utilidad_bruta_09)
print("Utilidad bruta 10:",utilidad_bruta_10)
print("Total:",total)
print("Total de utilidad:",total_de_utilidad)
print("###################")
#Informacion_de_Gastos_de_operacion
#DECLARACION
gasto_de_operacion_05=0
gasto_de_operacion_06=0
gasto_de_operacion_07=0
gasto_de_operacion_08=0
gasto_de_operacion_09=0
gasto_de_operacion_10=0
total=0
#INPUT
gasto_de_operacion_05=float(input("Gasto de operacion del 2005:"))
gasto_de_operacion_06=float(input("Gasto de operacion del 2006:"))
gasto_de_operacion_07=float(input("Gasto de operacion del 2007:"))
gasto_de_operacion_08=float(input("Gasto de operacion del 2008:"))
gasto_de_operacion_09=float(input("Gasto de operacion del 2009:"))
gasto_de_operacion_10=float(input("Gasto de operacion del 2010:"))
#PROCESSING
total=(gasto_de_operacion_05+gasto_de_operacion_06+gasto_de_operacion_07+gasto_de_operacion_08+gasto_de_operacion_09+gasto_de_operacion_10)
#Detector
#Si el año es bueno el gasto de costo es <18000
total_de_gasto=(total<18000)
#OUTPUT
print("########################")
print("   Gasto de operacion   ")
print("########################")
print("Gasto de operacion 05:",gasto_de_operacion_05)
print("Gasto de operacion 06:",gasto_de_operacion_06)
print("Gasto de operacion 07:",gasto_de_operacion_07)
print("Gasto de operacion 08:",gasto_de_operacion_08)
print("Gasto de operacion 09:",gasto_de_operacion_09)
print("Gasto de operacion 10:",gasto_de_operacion_10)
print("Total:",total)
print("Totla de Gasto:",total_de_gasto)
print("#######################")
#Informacion_de_Resultado_de_operacion_antes_de_otros_gastos_neto
#DECLARACION
resultado_de_operacion_antes_de_otros_gastos_neto_05=0
resultado_de_operacion_antes_de_otros_gastos_neto_06=0
resultado_de_operacion_antes_de_otros_gastos_neto_07=0
resultado_de_operacion_antes_de_otros_gastos_neto_08=0
resultado_de_operacion_antes_de_otros_gastos_neto_09=0
resultado_de_operacion_antes_de_otros_gastos_neto_10=0
total=0
#INPUT
resultado_de_operacion_antes_de_otros_gastos_neto_05=float(input("Resultado del 2005:"))
resultado_de_operacion_antes_de_otros_gastos_neto_06=float(input("Resultado del 2006:"))
resultado_de_operacion_antes_de_otros_gastos_neto_07=float(input("Resultado del 2007:"))
resultado_de_operacion_antes_de_otros_gastos_neto_08=float(input("Resultado del 2008:"))
resultado_de_operacion_antes_de_otros_gastos_neto_09=float(input("Resultado del 2009:"))
resultado_de_operacion_antes_de_otros_gastos_neto_10=float(input("Resultado del 2010:"))
#PROCESSING
total=(resultado_de_operacion_antes_de_otros_gastos_neto_05+resultado_de_operacion_antes_de_otros_gastos_neto_06+resultado_de_operacion_antes_de_otros_gastos_neto_07+resultado_de_operacion_antes_de_otros_gastos_neto_08+resultado_de_operacion_antes_de_otros_gastos_neto_09+resultado_de_operacion_antes_de_otros_gastos_neto_10)
#Detector
#Si el año es bueno el resultado sera <16000
total_de_resultados=(total<16000)
#OUTPUT
print("######################################################")
print("   Resultado de operacion de ante de otros gastos neto")
print("######################################################")
print("Resultado de operacion antes de otros gastos neto 05:",resultado_de_operacion_antes_de_otros_gastos_neto_05)
print("Resultado de operacion antes de otros gastos neto 06:",resultado_de_operacion_antes_de_otros_gastos_neto_06)
print("Resultado de operacion antes de otros gastos neto 07:",resultado_de_operacion_antes_de_otros_gastos_neto_07)
print("Resultado de operacion antes de otros gastos neto 08:",resultado_de_operacion_antes_de_otros_gastos_neto_08)
print("Resultado de operacion antes de otros gastos neto 09:",resultado_de_operacion_antes_de_otros_gastos_neto_09)
print("Resultado de operacion antes de otros gastos neto 10:",resultado_de_operacion_antes_de_otros_gastos_neto_10)
print("Total:",total)
print("Total de resultados:",total_de_resultados)
print("######################################################")
#Informacion_de_Otros_gastos_netos
#DECLARACION
otros_gastos_neto_05=0
otros_gastos_neto_06=0
otros_gastos_neto_07=0
otros_gastos_neto_08=0
otros_gastos_neto_09=0
otros_gastos_neto_10=0
total=0
#INPUT
otros_gastos_neto_05=float(input("Otros Gastos del 2005:"))
otros_gastos_neto_06=float(input("Otros Gastos del 2006:"))
otros_gastos_neto_07=float(input("Otros Gastos del 2007:"))
otros_gastos_neto_08=float(input("Otros Gastos del 2008:"))
otros_gastos_neto_09=float(input("Otros Gastos del 2009:"))
otros_gastos_neto_10=float(input("Otros Gastos del 2010:"))
#PROCESSING
total=(otros_gastos_neto_05+otros_gastos_neto_06+otros_gastos_neto_07+otros_gastos_neto_08+otros_gastos_neto_09+otros_gastos_neto_10)
#Detector
#Si el año es bueno otros gastos sera <3000
total_otros_gastos=(total<3000)
#OUTPUT
print("########################")
print("   Otros gastos netos   ")
print("########################")
print("Otros gastos netos 05:",otros_gastos_neto_05)
print("Otros gastos netos 06:",otros_gastos_neto_06)
print("Otros gastos netos 07:",otros_gastos_neto_07)
print("Otros gastos netos 08:",otros_gastos_neto_08)
print("Otros gastos netos 09:",otros_gastos_neto_09)
print("Otros gastos netos 10:",otros_gastos_neto_10)
print("Total:",total)
print("Total otros gastos:",total_otros_gastos)
print("#######################")
