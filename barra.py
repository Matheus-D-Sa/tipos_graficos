import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Barra
x = df['Gênero'].value_counts().index
y = df['Gênero'].value_counts().values

plt.figure(figsize=(17, 6))
plt.bar(x, y, color='#03800f')
plt.title('Divisão de Gêneros')
plt.xlabel('Tipos de Gêneros Disponíveis')
plt.ylabel('Quantidade')
# plt.savefig('grafico_4.png') # Salvar Imagem
plt.tight_layout()
plt.show()