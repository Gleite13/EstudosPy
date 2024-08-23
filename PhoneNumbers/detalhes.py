import phonenumbers

from phonenumbers import carrier, geocoder, timezone

telefone = phonenumbers.parse(input("Digite o numero de telefone com o codigo do país: "))

print(timezone.time_zones_for_number(telefone))

print(carrier.name_for_number(telefone, "pt-br"))

print(geocoder.description_for_number(telefone,"pt-br"))

print(f'Numero valido {phonenumbers.is_valid_number(telefone)}')

