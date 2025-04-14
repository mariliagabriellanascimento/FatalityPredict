# Previsão de Acidentes de Trânsito: Projeto com o Dataset DETRAN 2020

Este projeto tem como objetivo explorar, analisar e desenvolver modelos de **machine learning** para prever a severidade dos acidentes de trânsito, utilizando dados disponibilizados pelo **DETRAN** (Departamento de Trânsito) referentes ao ano de 2020. O conjunto de dados foi disponibilizado por **Raphael Marconato**, Analista de Dados na Huawei, localizado em Dublin, Irlanda.

## Sobre o Dataset

O dataset contém **22.644 registros de acidentes** ocorridos no Brasil em 2020, distribuídos em **18 colunas**, sendo **14 variáveis categóricas**. As principais variáveis incluem:

- `num_boletim`: Número do boletim de ocorrência.
- `data_hora_boletim`: Data e hora do registro.
- `nº_envolvido`: Número de pessoas envolvidas.
- `condutor`: Indica se o condutor foi responsável pelo acidente.
- `desc_severidade`: Informa se o acidente foi fatal ou não.
- `sexo`: Sexo da pessoa envolvida.
- `cinto_seguranca`: Uso do cinto de segurança.
- `embriaguez`: Condição do condutor quanto ao uso de álcool.
- `idade` e `nascimento`: Faixa etária e data de nascimento.
- `categoria_habilitacao` e `descricao_habilitacao`: Tipo e descrição da habilitação.
- `declaracao_obito`: Indicação de óbito no acidente.
- `cod_severidade_antiga`: Código anterior de severidade.
- `especie_veiculo`: Tipo de veículo envolvido.
- `pedestre` e `passageiro`: Envolvimento de pedestres e passageiros.

## Objetivos do Projeto

### 1. **Exploração e Análise de Dados (EDA):**  
   Análise da distribuição dos acidentes, identificação de fatores de risco e estudo das correlações entre variáveis.

### 2. **Modelagem Preditiva:**  
   Desenvolvimento de modelos para prever a probabilidade de um acidente resultar em fatalidade, considerando diversas condições.

### 3. **Análise de Fatores de Risco:**  
   Identificação dos principais fatores que aumentam a gravidade dos acidentes, fornecendo subsídios para estratégias de prevenção.

## Tecnologias e Métodos Utilizados

- **Python**: Linguagem principal para análise e desenvolvimento de modelos.
- **Pandas, NumPy e Matplotlib**: Ferramentas para manipulação e visualização dos dados.
- **Scikit-learn**: Para a criação de modelos de machine learning, como regressão, classificação e clustering.
- **XGBoost e Random Forest**: Modelos avançados de classificação e previsão.
- **Análise de Séries Temporais**: Para entender a variação dos acidentes ao longo do tempo e prever futuros acidentes.

## Motivação

Os acidentes de trânsito representam uma das principais causas de mortes no mundo. A análise desses dados pode ser uma ferramenta poderosa para a criação de políticas públicas de segurança viária mais eficazes. Através da modelagem preditiva e da análise das fatalidades dos acidentes, nosso objetivo é contribuir com soluções que possam **reduzir o número de vítimas** e promover mais segurança para motoristas e pedestres.

## Próximos Passos

- **Integração de Dados Externos:** Adicionar variáveis como dados climáticos em tempo real ou informações sobre infraestrutura urbana.
- **Deploy do Modelo:** Criar um sistema de recomendação para as autoridades de trânsito com base nos dados previstos.
- **Avaliação de Impacto:** Estudar o impacto potencial das soluções implementadas para melhorar a segurança no trânsito.
