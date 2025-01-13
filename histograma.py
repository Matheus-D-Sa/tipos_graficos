import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string()) # Visualizar as primeiras 5 linhas

# Gráfico de Histograma
plt.figure(figsize=(10, 6))
plt.hist(df['Preço'], bins=100, color='#09b0ed', alpha=0.8)
plt.title('Histograma - Distribuição de Preço')
plt.xlabel('Preços')
plt.xticks(ticks=range(0, int(df['Preço'].max())+25, 25))
plt.ylabel('Frequência')
plt.grid(True)
# plt.savefig('grafico_1.png') # Salvar Imagem
plt.show()