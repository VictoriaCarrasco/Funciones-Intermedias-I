x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# Actualizar valores en diccionarios y listas

x [1][0] = 15 
print (x) 

acceder  = estudiantes[1]
acceder ['last_name'] = 'Bryant'
print (estudiantes)

directorio_deportes ['fútbol'][0]= "Andres"
print (directorio_deportes)

letras = z [0]
letras ['y']= 30
print (z)  

#Iterar a traves de una lista de dicciinario

def iterateDistionary (some_list):
    for item in some_list:
        texto = ""
        for key, value in item.items():
            texto += key+" - "+value+" , "
        print (texto)

iterateDistionary (estudiantes)

# Obtener valores de una lista de diccionario

def iterateDictionary2 (key_name, somelist):
    for estudiantes in somelist: 
        if key_name in estudiantes: 
            valor = estudiantes[key_name]
            print (valor)


iterateDictionary2 ('first_name', estudiantes)

def iterateDictionary3 (apellido, somelist):
    for estudiantes in somelist :
        if apellido in estudiantes:
            valor2 = estudiantes[apellido] 
            print (valor2)

iterateDictionary3 ('last_name', estudiantes)

print ("________________________________")

#Iterar a través de un diccionarios con valores de lista
dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


for clave, valor in dojo.items():
    print (f"{len(valor)} {clave.upper()}")
    for item in valor: #pasa por cada item de los valores e imprimelo
        print (item)
    print()
