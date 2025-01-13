import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ecommerce_estatistica.csv')
# print(df.head().to_string())

# Múltiplos gráficos
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1) # 2 Linha, 2 Colunas, 1° Gráfico

# Gráfico de Dispersão 1
plt.scatter(df['Preço'], df['Preço'], color='#fc0328')
plt.title('Dispersão - Preço e Preço')
plt.xlabel('Preço')
plt.ylabel('Preço')

# Gráfico de Dispersão 2
plt.subplot(1, 2, 2) # 1 Linha, 2 Colunas, 2° Gráfico
plt.scatter(df['Preço'], df['Desconto'], color='#fc0328', alpha=0.6, s=30)
plt.title('Dispersão - Preço e Desconto')
plt.xlabel('Preço')
plt.ylabel('Desconto')

# plt.savefig('grafico_2.png') # Salvar Imagem
plt.tight_layout() # Ajustar espaçamentos
plt.show()