import maestra as m

m.limpia()
#Cargamos un Json y mostramos el resultado en pantalla
contactos = m.leerJson('contactos.json')
print(contactos)

#añadimos un contacto al diccionario
nombre = input("Dime el nombre del siguiente contacto: ")
contactos.append({'nom': nombre, 'tel': '9789789', 'direccions': [{'carrer': 'Falsa', 'numero': '456', 'pis': '12', 'cp': '44444'}]})
print(contactos)

guardar = input('Quieres guardar? ')
if(guardar=='s' or guardar =='si'):
    m.escribirJson(contactos,'contactos.json')
    print('Contacto Guardado')
else:
    print('Contacto no guardado')

#print(m.variable1)
#print(m.suma2())

#print(m.variable1)

#print(m.divide())

#print('HOLA')

# print(m.vauto)
# m.vauto = m.autosuma(m.vauto)
# m.vauto = m.autosuma(m.vauto)
# print(m.vauto)