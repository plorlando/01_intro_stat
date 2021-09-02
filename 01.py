import numpy as np

data = [44, 48, 56, 63, 68, 72, 82, 97, 53, 57, 63, 68, 74, 85, 100, 60, 63, 69, 77, 90, 106, 54, 60, 65, 69, 78, 93,
107, 56, 62, 66, 70, 80, 95, 56, 63, 67, 71, 81, 95]

media = np.mean(data)
mediana = np.median(data)
quartil_1 = np.percentile(data, 25)
quartil_2 = np.percentile(data, 50)  # não é necessário calcular, pois sempre é igual a mediana
quartil_3 = np.percentile(data, 75)
maior_valor = np.max(data)
menor_valor = np.max(data)
amplitude = maior_valor - menor_valor  # calcula a amplitude total da amostra


print(media)
print(mediana)
print(quartil_1)
print(quartil_2)
print(quartil_3)
print('oi')