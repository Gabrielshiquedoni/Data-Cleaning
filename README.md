# Pipeline de Validação de Dados Financeiros (ETL)

## 📌 Sobre o Projeto
Este projeto simula uma demanda real de uma área de **Business Intelligence**: a ingestão, limpeza e estruturação de dados financeiros para análise.

O objetivo foi criar um script automatizado que recebe dados brutos (com erros de digitação e valores inconsistentes), aplica regras de negócio para validar a qualidade da informação (**Data Quality**) e armazena o resultado em um banco de dados relacional.

Embora seja um projeto introdutório, ele aplica conceitos fundamentais de Engenharia de Dados, como **ETL** (Extract, Transform, Load) e **Tratamento de Erros**.

## 🚀 Tecnologias Utilizadas
* **Python 3.x**: Linguagem principal para a lógica de automação.
* **Pandas**: Utilizado para manipulação tabular e performance no tratamento dos dados.
* **SQLite3**: Banco de dados relacional para persistência dos dados tratados.
* **DateTime**: Para geração de logs e rastreabilidade do processamento.

## ⚙️ Funcionalidades do Pipeline
O script `tratamento_dados.py` executa as seguintes etapas:

1.  **Ingestão de Dados (Extract):** Simula o recebimento de uma base de dados externa (Dicionário/JSON).
2.  **Transformação (Transform):**
    * **Padronização:** Converte nomes de clientes para maiúsculo (`.upper()`), eliminando duplicidades por *case sensitivity*.
    * **Sanitização:** Remove registros com valores de investimento negativos ou inválidos (Regra de Negócio).
    * **Enriquecimento:** Adiciona uma coluna de `Data_Processamento` para garantir rastreabilidade (Audit Trail).
3.  **Carga (Load):**
    * Exporta os dados validados para um banco de dados SQL local (`base_blackbird.db`).
    * Utiliza a lógica de `replace` para permitir a reexecução do script mantendo os dados sempre atualizados.
4.  **Segurança:**
    * Implementação de blocos `try/except` para capturar falhas críticas sem quebrar a execução abruptamente.

## 🛠 Como Executar

### Pré-requisitos
Certifique-se de ter o Python instalado. Em seguida, instale a biblioteca Pandas:

```bash
pip install pandas
