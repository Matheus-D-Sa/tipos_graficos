import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Pizza
x = df['Qtd_Vendidos'].value_counts().index
y = df['Qtd_Vendidos'].value_counts().values

plt.figure(figsize=(6, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição de Quantidade de Produtos Vendidos')
# plt.savefig('grafico_5.png') # Salvar Imagem
plt.tight_layout()
plt.show()