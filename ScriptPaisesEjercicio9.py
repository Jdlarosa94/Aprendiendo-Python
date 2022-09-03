valores = (input (")Ingresa Paises separados por coma , "))
Paises = [ pais for pais in valores.split(',')]
print(','.join(sorted(list(set(Paises)))))

##Script Paises