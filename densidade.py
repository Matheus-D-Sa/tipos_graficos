import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Densidade
plt.figure(figsize=(12, 8))
sns.kdeplot(df['Preço'], fill=True, color='#863e9c')
plt.title('Densidade dos Preços')
plt.xlabel('Preço')
plt.ylabel('Densidade')
# plt.savefig('grafico_6.png') # Salvar Imagem
plt.tight_layout()
plt.show()