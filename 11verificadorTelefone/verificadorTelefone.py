import phonenumbers
from phonenumbers import geocoder 

numero = input('Digite um número formato: [+55999999999]: ')

telefone = phonenumbers.parse(numero)

print(f'o numero {numero} é da região de', end= " ")
print(geocoder.description_for_number(telefone, 'pt'))