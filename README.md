# Previsão de Acidentes de Trânsito: Projeto com o Dataset DETRAN 2020

Este projeto tem como objetivo explorar, analisar e desenvolver modelos de **machine learning** para prever a severidade dos acidentes de trânsito, utilizando dados disponibilizados pelo **DETRAN** (Departamento de Trânsito) referentes ao ano de 2020. O conjunto de dados foi compartilhado por **Raphael Marconato**, Analista de Dados na Huawei, localizado em Dublin, Irlanda.

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
- **Pandas, NumPy, Matplotlib e Seaborn**: Manipulação e visualização de dados.
- **Scikit-learn**: Criação de modelos de machine learning (Random Forest, SVM, KNN, etc.).
- **SMOTE**: Técnica para balanceamento de classes.
- **Flask + JavaScript**: Utilizados no desenvolvimento do sistema web para visualização dos resultados.

## Escolha do Modelo Final: SVM (Support Vector Machine)

Após testes com diversos algoritmos, como Random Forest, KNN e XGBoost, o modelo SVM com kernel RBF foi o que apresentou o **melhor equilíbrio entre precisão e recall** nas três classes avaliadas:

```python
SVC(kernel='rbf', C=1.0, probability=True, random_state=42)
```

### Métricas de Validação:

| Classe          | Precisão | Revocação | F1-score |
|----------------|----------|-----------|----------|
| FATAL          | 0.74     | 0.71      | 0.72     |
| NAO FATAL      | 0.62     | 0.63      | 0.62     |
| SEM FERIMENTOS | 0.84     | 0.85      | 0.84     |
| **Acurácia**   | **0.73** |           |          |

### Métricas de Teste:

| Classe          | Precisão | Revocação | F1-score |
|----------------|----------|-----------|----------|
| FATAL          | 0.74     | 0.70      | 0.72     |
| NAO FATAL      | 0.60     | 0.66      | 0.63     |
| SEM FERIMENTOS | 0.86     | 0.83      | 0.84     |
| **Acurácia**   | **0.73** |           |          |

## Atributos Utilizados no Modelo

O modelo SVM utilizou as seguintes variáveis para realizar a predição:

- `condutor`
- `sexo`
- `cinto_seguranca`
- `embriaguez`
- `idade`
- `categoria_habilitacao`
- `especie_veiculo`
- `pedestre`
- `passageiro`

## Interface Web: FatalityPredict

Foi desenvolvida uma aplicação web utilizando Flask no backend e JavaScript no frontend, que permite ao usuário informar as condições de um acidente e obter a predição da severidade. A interface é intuitiva e responsiva.

## Próximos Passos

- **Integração de Dados Externos:** Adicionar variáveis como dados climáticos ou de infraestrutura urbana.
- **Deploy do Modelo:** Publicação do sistema em um servidor web.
- **Avaliação de Impacto:** Estudo do impacto da predição em políticas públicas e segurança viária.
