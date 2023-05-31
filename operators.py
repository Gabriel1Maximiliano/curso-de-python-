#Crear un programa que calcule las ganancias de los vendedores
#Debe preguntar nombre y volumen de ventas las comisiones
#son del 13% del total vendido

print( "Bienvenido" )


user     = input( "Ingresa tu nombre: " )
turnover = input( "Ingresa tu total de ventas: " )

print(f"Este mes tu comisión por ventas es: { round( ( float(turnover)*0.13 ) ) } ")