import pandas as pd

# Carregar os dados de vendas
dados_vendas = pd.read_csv('vendas_por_capitais.csv')

# Verificar se há valores nulos
print(dados_vendas.isnull().sum())

# Remover registros duplicados
dados_vendas = dados_vendas.drop_duplicates()

# Preenchendo valores nulos com a mediana da coluna 'Valor da Venda'
dados_vendas['Valor da Venda'] = dados_vendas['Valor da Venda'].fillna(
    dados_vendas['Valor da Venda'].median())

# Descrição estatística dos dados
print(dados_vendas.describe())
# Salvar os dados atualizados em um novo arquivo CSV

import matplotlib.pyplot as plt
import seaborn as sns

# Distribuição das vendas por capital
plt.figure(figsize=(10, 6))
sns.countplot(data=dados_vendas, x='Capital')
plt.title('Distribuição das Vendas por Capital')
plt.xlabel('Capital')
plt.ylabel('Quantidade de Vendas')
plt.show()

# Vendas totais por capital
vendas_por_capital = dados_vendas.groupby(
    'Capital')['Valor da Venda'].sum().sort_values(ascending=False)
print(vendas_por_capital)

# Vendas ao longo dos anos
vendas_por_ano = dados_vendas.groupby('Ano')['Valor da Venda'].sum()
vendas_por_ano.plot(kind='line', marker='o')
plt.title('Vendas ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Valor da Venda')
plt.show()

# Boxplot para comparação entre capitais
plt.figure(figsize=(12, 8))
sns.boxplot(data=dados_vendas, x='Capital', y='Valor da Venda')
plt.title('Comparação de Vendas entre Capitais')
plt.xlabel('Capital')
plt.ylabel('Valor da Venda')
plt.show()
