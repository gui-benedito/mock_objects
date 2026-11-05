# Exercício Prático - Mock Object (CustomStack & NumberAscOrder)

Repositório com a resolução da atividade prática de testes de unidade e utilização de **Mock Objects** em Python para o curso de Testes de Software.

---

## Contexto da Atividade

A atividade é dividida em duas partes:

1. **Parte 1 — Testes de Unidade da Classe `CustomStack`**:
   - Alcançar **100% de cobertura de testes** (analisado via `pytest-cov`).
   - Identificar e analisar a efetividade dos testes existentes.
   - Corrigir bugs de lógica presentes na implementação original da pilha (onde a verificação de capacidade máxima comparava o método `self.size` diretamente com `self.limit` em vez de chamar `self.size()`).

2. **Parte 2 — Ordenação dos Números da Mega-Sena (`NumberAscOrder`) com Dublês de Teste (Mock)**:
   - Implementar a classe `NumberAscOrder` e o método `sort(custom_stack) -> list` que coleta os números sorteados armazenados em um `CustomStack` e os retorna em ordem crescente.
   - Criar casos de teste usando `Mock` para isolar a classe sob teste da implementação concreta da pilha:
     - **Cenário 1**: Pilha de 6 posições contendo 6 números sorteados (aleatoriamente).
     - **Cenário 2**: Pilha de 6 posições vazia.
     - **Cenários complementares**: Validações de integração com pilha real e tratamento de entradas nulas (`ValueError`).

---

## Tecnologias e Ferramentas

- **Linguagem**: Python 3.10+
- **Framework de Testes**: `pytest`
- **Cobertura de Código**: `pytest-cov`
- **Mocks e Dublês**: `unittest.mock` / `pytest-mock`

---

## Como Preparar o Ambiente e Executar

### 1. Criar e Ativar o Ambiente Virtual

No diretório do projeto `custom-stack`:

#### No Windows (PowerShell):
```powershell
cd custom-stack
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

#### No Linux / macOS:
```bash
cd custom-stack
python3 -m venv .venv
source .venv/bin/activate
```

---

### 2. Instalar as Dependências

Com a `venv` ativada:
```bash
pip install -r requirements.txt
```

---

### 3. Executar os Testes e Gerar Relatório de Cobertura

Dentro da pasta `custom-stack`, execute:

```bash
python -m pytest test --cov=src --cov-report=term-missing
```

#### Resultado Obtido:
```text
============================= test session starts =============================
platform win32 -- Python 3.13.3, pytest-8.1.1, pluggy-1.5.0
plugins: cov-5.0.0, mock-3.14.0
collected 11 items

test\custom_stack_test.py ......                                         [ 54%]
test\test_number_asc_order.py .....                                      [100%]

---------- coverage: platform win32, python 3.13.3-final-0 -----------
Name                        Stmts   Miss  Cover   Missing
---------------------------------------------------------
src\__init__.py                 0      0   100%
src\custom_stack_class.py      24      0   100%
src\number_asc_order.py         8      0   100%
---------------------------------------------------------
TOTAL                          32      0   100%

============================= 11 passed in 0.19s =============================
```

---

## Estrutura de Arquivos

```text
mock_objects/
├── .gitignore
├── README.md                          # Documentação principal do projeto
└── custom-stack/
    ├── requirements.txt               # Dependências do projeto
    ├── README.md                      # Instruções originais
    ├── src/
    │   ├── __init__.py
    │   ├── custom_stack_class.py      # Implementação da pilha CustomStack
    │   └── number_asc_order.py        # Coletor e ordenador da Mega-Sena
    └── test/
        ├── __init__.py
        ├── custom_stack_test.py       # Testes unitários do CustomStack (100% cov)
        └── test_number_asc_order.py   # Testes com Mock Object de NumberAscOrder
```
