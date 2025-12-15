## 🏥 Clínica Vida+

Este projeto e contruido para gerenciar pacientes e consultas médicas de uma clínica de saúde que  sofre com a grande demanda de serviços médicos e procura por uma solução digital capaz de otimizar o atendimento e a experinecia dos pacientes.

## 🏥 Visão Geral do Projeto

A contrução do projeto esta sendo criada em duas partes:

1.  **Backend (Python):** Responsável pela lógica de negócio e persistência de dados.
2.  **Frontend (React/JavaScript):** Interface de usuário (a ser iniciada).

## 🚀 Status Atual do Projeto — Fase 1 (Backend)

Atualmente, o foco do projeto está na **organização e refatoração do backend em Python**.

### ✅ O que já foi feito

* Definição e criação da **estrutura modular** completa do backend (`models/`, `controllers/`, `services/`, `utils/`, etc.).
* **Modelos (Dados):** A classe **Paciente** foi isolada corretamente em `backend/models/paciente.py`.
* **Utilitários (Ferramentas):** As funções de **validação de *input*** (checagem de nome, idade e telefone) foram isoladas no módulo `backend/utils/validacoes.py`.
* **Controlador (Lógica de Negócio):** O **`PacienteController`** foi implementado em `backend/controllers/paciente_controller.py`, gerenciando o cadastro, listagem e busca dos pacientes.
* **Teste de Integridade:** Foi adicionado um **Teste Rápido de Integração** (`backend/teste_controllers.py`) para validar o fluxo de comunicação entre as camadas **Controller**, **Models**, e **Utils**.

### ⏳ Próximas Tarefas de Refatoração

* **Implementar o Serviço:** Isolar a lógica de cálculos e plotagem de relatórios de estatísticas no módulo *services/estatisticas.py.*
* **Finalizar o Menu:** Ajustar o arquivo *app.py* para chamar o Controller e o Service, restaurando a funcionalidade completa do sistema.

### ❌ Ainda não iniciado

* Criação de novas funcionalidades (editar paciente, excluir paciente, criar consulta, etc.)
* Integração com banco de dados (substituir a lista em memória).
* Desenvolvimento do frontend e a comunicação entre as camadas.

