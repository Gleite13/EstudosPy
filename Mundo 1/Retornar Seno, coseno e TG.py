import math
ang = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(ang))
print('O ângulo de {} tem SENO de {:.2f}' .format(ang,seno))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem CONSSENO de {:.2f} ' .format(ang,cos))
tan = math.tan(math.radians(ang))
print('O ângulo de {} tem TANGENTE de {:.2f}' .format(ang,tan))