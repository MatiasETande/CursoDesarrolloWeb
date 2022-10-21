'''La contaminación del agua se detecta en los laboratorios,  donde pequeñas 
muestras de agua se analizan para diversos tipos de contaminantes. Los 
organismos vivos tales como pescados se pueden también utilizar para la 
detección de la contaminación del agua. Los cambios en su comportamiento o 
crecimiento nos demuestran,  que el agua en la que viven está contaminada.

Para seguir colaborando en esta misión de salvar al planeta, necesitamos que
 elabores un programa en Python que dado el tamaño de un pez indique si su 
 organismo está contaminado. Para ello tendremos 4 opciones:

Tamaño Normal: Mensaje "Pez en buenas condiciones"

Tamaño por debajo de lo Normal: Mensaje "Pez con problemas de nutrición"

Tamaño un poco por encima de lo Normal: Mensaje "Pez con síntomas de organismo contaminado"

Tamaño sobredimensionado: Mensaje "Pez contaminado" '''

print('Opciones:\n'
+'1 - Tamaño Normal\n'
+'2 - Tamaño por debajo de lo Normal\n'
+'3 - Tamaño un poco por encima de lo Normal\n'
+'4 - Tamaño sobredimensionado\n')

tamanoPez = int(input("Ingrese su opcion: "))

if tamanoPez == 1:
    print("Pez en buenas condiciones")
elif tamanoPez == 2:
    print("Pez con problemas de nutrición")
elif tamanoPez == 3:
    print("Pez con síntomas de organismo contaminado")
elif tamanoPez == 4:
    print("Pez contaminado")
else:
    print("Error: la opcion ingresada no esta disponible")






