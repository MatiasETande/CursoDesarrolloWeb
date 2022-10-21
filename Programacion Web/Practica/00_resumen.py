# Caracteristicas Python
# Es un leguaje interpretado
# Multiparadigma
# Multiplataforma
# Tipado Dinámico
# Fuertemente Tipado




# Este es un comentario, se usa el simbolo de la almohadilla o numeral (#)
'''Este es un 
comentario 
multilinea'''
""" Comentario multilinea
las comillas sencillas o dobles
se usan de manera indistinta"""


# Manejo de variables
# diclaracion: <nombreDeLaVariable> = <valor>
# pueden empezar con una letra o un guión bajo
# por convencion la primera letra es una minuscula
# puede contener letras, numeros y guión bajo
# python es case sensitive
# no se pueden utilizar palabras claves o reservadas de python


'''En Python no existen constantes ni variables, tan sólo objetos con los
que hacer modificaciones.
Lo que mal-llamamos variables (o constantes) no son otra cosa que
'referencias' a objetos, como etiquetas para poder identificarlos.
Los objetos en Python pueden ser ‘mutables’ si puede
modificarse solo algunas posiciones del dato o ‘inmutables’ si no
pueden modificarse'''


unaVariable="soy una variable"
_variable="tambien soy una variable"
unnumero=1

# en python las constates no existen
# por convencion las variables que se van a usa como constantes
# se escriben con mayusculas

CONSTANTE = "Soy una constante"

# Tipos de datos estandares

# numeros
1 #enteros int
1.2 #decimales float
1+4j #complejos complex

# Cadenas o Strings
"soy un string" #str

# Booleanos
True #bool
False #bool

# Conjuntos
# Es una colección de datos desordenada
# que no contiene elementos que se repiten.
conjunto = {'naranja',1,'c',2.6,True,1,'naranja'} #set 
print(conjunto) # su salida sera {'c', 1, 'naranja', 2.6}

# Listas
unaLista=[0.5,'manzana',25,25] #list

# tuplas
# Es una lista que no se puede modificar después de su creación
unaTupla = 1, 25, 1.5, 'Hola' #tuple
otraTupla = (45, 25, 1.6, "eso") #tuple

# Diccionarios
'''Es un tipo de dato similar a los arreglos, pero trabajan con
llaves y valores en vez de índices.
Cada valor está almacenado en un diccionario que puede ser accedido
usando una clave en cualquier tipo de objeto (una cadena, número, lista, etc)
en vez de usar un índice para referirse.'''
unDiccionario={
    1: 'hola',
    2: 'como',
    6: 'No'
} #dict
print(unDiccionario[6]+" "+unDiccionario[1])

# NONE
# A menudo None es utilizado cuando se quiere crear una variable
# pero aún no se le quiere asignar ningún valor en particular

algunaVariable=None

# operadores matematicos
print(2 + 3)             # addition(+)
print(3 - 1)             # subtraction(-)
print(2 * 3)             # multiplication(*)
print(3 / 2)             # division(/)
print(3 ** 2)            # exponential(**)
print(3 % 2)             # modulus(%)
print(3 // 2)            # Floor division operator(//)

# opradores de comparacion
1==1
1!=1
1<1
1<=1
1>1
1<=1

# operadores lógicos
1==1
1!=1
True and True
True or True
not True

# operadores 

# la funcion type()
print(type(10))          # Int
print(type(3.14))        # Float
print(type(1 + 3j))      # Complex number
print(type('Asabeneh'))  # String
print(type([1, 2, 3]))   # List
print(type({'name':'Asabeneh'})) # Dictionary
print(type({9.8, 3.14, 2.7}))    # Set
print(type((9.8, 3.14, 2.7)))    # Tuple

class Persona():
    def __init__(self) -> None:
        pass