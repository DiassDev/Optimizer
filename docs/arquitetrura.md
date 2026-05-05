# Arquitetura do Sistema — Optimizer

**Versão:** 1.0
**Data:** Maio 2026

---S

# 1. Visão Geral

O sistema **Optimizer** tem como objetivo resolver o problema de alocação de turmas em laboratórios utilizando **Pesquisa Operacional**, mais especificamente **Programação Linear Inteira (PLI)**.

O sistema busca:

* Garantir que nenhuma turma fique sem sala
* Evitar superlotação
* Minimizar o desperdício de capacidade (ociosidade)

A resolução é feita via **solver CBC**, utilizando a biblioteca **PuLP**, integrada a uma aplicação web baseada em **Django + Django REST Framework**.

---

# 2. Modelagem Matemática

## 2.1 Variáveis de Decisão

A variável binária define a alocação:

```
x[i][j] = 1 → turma i alocada no laboratório j
x[i][j] = 0 → caso contrário
```

Onde:

* i ∈ turmas (1..n)
* j ∈ laboratórios (1..m)

---

## 2.2 Função Objetivo

Minimizar a ociosidade total:

```
Min Σ_i Σ_j (capacidade[j] - alunos[i]) * x[i][j]
```

Objetivo:

* Preferir salas com capacidade próxima ao tamanho da turma
* Reduzir desperdício de recursos

---

## 2.3 Restrições

### 1. Designação única

Cada turma deve ser alocada em exatamente um laboratório:

```
Σ_j x[i][j] = 1   ∀ i
```

---

### 2. Unicidade por sala

Cada laboratório recebe no máximo uma turma:

```
Σ_i x[i][j] ≤ 1   ∀ j
```

---

### 3. Sem superlotação

```
alunos[i] ≤ capacidade[j]  quando x[i][j] = 1
```

---

### 4. Binariedade

```
x[i][j] ∈ {0,1}
```

---

# 3. Arquitetura do Sistema

O sistema segue uma arquitetura em camadas:

---

## 3.1 Camada de Apresentação

* Interface Web (inicialmente Django Templates)
* Evolução prevista: SPA com React
* Consome API REST

---

## 3.2 Camada de Aplicação

Responsabilidades:

* Receber requisições HTTP
* Validar dados (Serializers)
* Orquestrar execução do solver
* Retornar respostas

Tecnologias:

* Django
* Django REST Framework

---

## 3.3 Camada de Otimização

Responsável pela lógica de Pesquisa Operacional:

* Modelagem PLI → PuLP
* Pré-processamento → NumPy
* Execução → CBC Solver

Funções principais:

* Construção das matrizes
* Validação de viabilidade
* Execução do modelo
* Cálculo de métricas

---

## 3.4 Camada de Dados

* ORM: Django ORM
* Banco:

  * SQLite (desenvolvimento)
  * PostgreSQL (produção)

Responsável por persistir:

* Turmas
* Laboratórios
* Alocações
* Histórico de execuções

---

# 4. Estrutura de Diretórios (Backend)

```
backend/
│
├── manage.py
├── requirements.txt
│
├── apps/
│   ├── core/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── serializers.py
│   │   └── urls.py
│   │
│   └── solver/
│       ├── lp_model.py
│       ├── preprocessor.py
│       ├── runner.py
│       └── exceptions.py
```

---

# 5. Modelos de Dados

## Laboratorio

```python
class Laboratorio(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.PositiveIntegerField()
    recursos = models.JSONField(default=list)
```

---

## Turma

```python
class Turma(models.Model):
    codigo = models.CharField(max_length=20)
    disciplina = models.CharField(max_length=100)
    num_alunos = models.PositiveIntegerField()
    turno = models.CharField(max_length=20)
```

---

## Alocacao

```python
class Alocacao(models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    ociosidade = models.IntegerField()
    criado_em = models.DateTimeField(auto_now_add=True)
```

---

# 6. Requisitos do Sistema

## 6.1 Requisitos Funcionais

* RF-01: Cadastro de laboratórios
* RF-02: Cadastro de turmas
* RF-03: Execução do solver
* RF-04: Diagnóstico de viabilidade
* RF-05: Visualização da grade
* RF-06: Exportação CSV

---

## 6.2 Requisitos Não Funcionais

* RNF-01: Resposta < 5 segundos
* RNF-02: Pré-validação antes do solver
* RNF-03: Suporte a expansão (ex: variável tempo)
* RNF-04: Solver independente e testável
* RNF-05: Portabilidade de banco

---

# 7. Decisões de Arquitetura

## PuLP

* Interface de modelagem PLI em Python
* Permite trocar o solver sem alterar o modelo

---

## NumPy

* Construção eficiente de matrizes
* Validação prévia de viabilidade
* Cálculo de métricas

---

## Django

* ORM robusto
* Sistema de migrations
* Integração com REST

---

## Solver isolado

Benefícios:

* Testável com pytest
* Independente do Django
* Possível evolução para microserviço

---

# 8. Próximos Passos

* Implementar models e migrations
* Criar e validar modelo PLI
* Implementar pré-processamento
* Criar endpoints REST
* Integrar frontend
* Adicionar variável de tempo no modelo

---

# 📌 Observações finais

* O módulo `solver/` deve permanecer desacoplado do Django
* A API será o ponto central de integração com o frontend
* O sistema foi projetado para evolução incremental

---
