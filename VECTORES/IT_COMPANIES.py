#Lista
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
#funcion insert
it_companies.insert(0,"Dell")

print(it_companies)
#comprobar si empresa existe en lista
existe_o_no="Apple" in it_companies
print(existe_o_no)
#ordenar 
it_companies.sort()
print(it_companies)

#invertir lista
it_companies.sort(reverse=True)
print(it_companies)

#eliminar primera empresa
it_companies.pop(0)
print(it_companies)

del it_companies [0]
print(it_companies)

#eliminartodas las empresas de la lista
it_companies.clear()
print(it_companies)