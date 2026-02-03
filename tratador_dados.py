import pandas as pd
import sqlite3
from datetime import datetime

print("--- INICIANDO PROCESSAMENTO DE DADOS ---")

try:
    # 1.(Extract)
    dados = {
        'Cliente': ['ana', 'CARLOS', 'beatriz', 'DANIEL'],
        'Valor': [1000, 5000, -50, 2000],
        'Status': ['Ativo', 'Ativo', 'Cancelado', 'Ativo']
    }

    tabela = pd.DataFrame(dados)
    print("1. Dados carregados com sucesso.")

    # 2.(Transform)
    tabela['Cliente'] = tabela['Cliente'].str.upper()
    tabela_limpa = tabela[tabela['Valor'] > 0].copy()

    # (Rastreabilidades)
    data_hoje = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    tabela_limpa['Data_Processamento'] = data_hoje
    print("2. Regras de limpeza aplicadas.")

    # 3.(Load)
    conn = sqlite3.connect('base_dados.db')
    tabela_limpa.to_sql('clientes_tratados', conn, if_exists='replace', index=False)
    conn.close()
    print("3. Dados salvos no banco SQL local.")

    # 4. Resultado Final 
    total = tabela_limpa['Valor'].sum()
    print("\n" + "="*40)
    print(f"SUCESSO! Processo finalizado em: {data_hoje}")
    print(f"Total Financeiro Validado: R$ {total:,.2f}")
    print("="*40)
    print("\nVisualização da base final:")
    print(tabela_limpa)

except Exception as erro:
    print("\n" + "!"*30)
    print("ERRO CRÍTICO NO SISTEMA")
    print(f"Detalhe do erro: {erro}")
    print("!"*30)