# 🧩 Matriz de Confusão Interativa

Projeto desenvolvido como atividade acadêmica da faculdade, com o objetivo de aplicar na prática os conceitos de avaliação de modelos de classificação binária. O código foi publicado no GitHub como registro do aprendizado.
Ferramenta interativa em Python para gerar, visualizar e interpretar matrizes de confusão.

---

## 📸 Exemplo de saída

O programa exibe dois gráficos lado a lado:

- **Mapa de calor** da matriz de confusão (TP, TN, FP, FN)
- **Gráfico de pizza** com a proporção de cada resultado
- **Métricas** exibidas abaixo dos gráficos: Acurácia, Precisão, Recall e F1-Score

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/confusion-matrix.git
cd confusion-matrix
```

### 2. (Opcional) Crie um ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute o programa

```bash
python main.py
```

---

## 🧭 Funcionalidades

Ao iniciar, o programa exibe um menu com 3 opções:

| Opção | Descrição |
|-------|-----------|
| **1 - Amostra presetada** | Escolha entre uma lista de 10 ou 200 amostras já definidas |
| **2 - Amostra aleatória** | Informe a quantidade e o programa gera os valores aleatoriamente |
| **3 - Amostra personalizada** | Digite manualmente cada valor previsto e real (0 ou 1) |

---

## 📊 Métricas calculadas

| Métrica | Fórmula | O que mede |
|--------|--------|-----------|
| **Acurácia** | (TP + TN) / Total | Proporção geral de acertos |
| **Precisão** | TP / (TP + FP) | Dos que foram previstos positivos, quantos realmente eram? |
| **Recall** | TP / (TP + FN) | Dos que eram positivos, quantos o modelo encontrou? |
| **F1-Score** | 2 × (Precisão × Recall) / (Precisão + Recall) | Equilíbrio entre Precisão e Recall |

### Legenda da matriz

| Sigla | Nome | Significado |
|-------|------|-------------|
| **TP** | Verdadeiro Positivo | Previsto como 1, era de fato 1 |
| **TN** | Verdadeiro Negativo | Previsto como 0, era de fato 0 |
| **FP** | Falso Positivo | Previsto como 1, mas era 0 (Erro tipo I) |
| **FN** | Falso Negativo | Previsto como 0, mas era 1 (Erro tipo II) |

---

## 📦 Dependências

| Biblioteca | Uso |
|-----------|-----|
| `scikit-learn` | Cálculo da matriz de confusão |
| `seaborn` | Visualização do mapa de calor |
| `matplotlib` | Exibição dos gráficos |

> Versões mínimas recomendadas no arquivo `requirements.txt`.

---

## 🗂️ Estrutura do projeto

```
confusion-matrix/
├── main.py           # Código principal
├── requirements.txt  # Dependências do projeto
└── README.md         # Documentação
```

---

## 🤝 Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma *issue* ou enviar um *pull request* com melhorias, correções ou novas funcionalidades.

---

## 📄 Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.
