# Trabalhando com Número de Telefone
# Refêrencia: https://pyp.org/project/phonenumbers/

import phonenumbers

# Ajuste do telefone para usarmos o phonenumber
telefone = "+5521999999999"
telefoneAjustado = phonenumbers.parse(telefone)# pode-se adicionar , "BR" e Retirar o numero +55 do telefone
print(telefoneAjustado)

# descobrir a localização do telefone
from phonenumbers import geocoder
local = geocoder.description_for_number(telefoneAjustado, 'pt-br')
print(local)

#Formatar um numero de telefone
telefoneFormulario = "21965802410"
telefoneFormularioAjustado = phonenumbers.parse(telefoneFormulario, "BR")
telefoneFormatado = phonenumbers.format_number(telefoneFormularioAjustado,
                                               phonenumbers.PhoneNumberFormat.NATIONAL)
print(telefoneFormatado)

#Descobrir a operadora do telefone
from phonenumbers import carrier
operadora = carrier.name_for_number(telefoneAjustado, "pt-br")
print(operadora)