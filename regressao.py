import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Gráfico de Regressão
sns.regplot(x='Desconto', y='Preço', data=df, color='#278f65', scatter_kws={'alpha': 0.5, 'color': '#34c289'})
plt.title('Regressão de Preço por Desconto')
plt.xlabel('Desconto')
plt.ylabel('Preço')
# plt.savefig('grafico_7.png') # Salvar Imagem
plt.tight_layout()
plt.show()