import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Mapa de Calor
plt.figure(figsize=(10, 6))
corr = df[['Preço', 'Desconto']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlação de Preço e Desconto')
# plt.savefig('grafico_3.png') # Salvar Imagem
plt.show()