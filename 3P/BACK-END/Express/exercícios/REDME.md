# Exercícios de programação Back-end

## 1 - Sistema de cadastro de livros 

Objetivo: Criar uma aplicação com formulário para cadastrar livros em uma biblioteca pessoal.

### Requisitos

1. Criar uma página com um formulário (método POST) contendo os campos:
    
<ul>
    <li>Título (texto)</li>
    <li>Autor (texto)</li>
    <li>Ano de publicação (número inteiro)</li>
    <li>Gênero (select: "Ficção", "Não Ficção", "Fantasia", "Biografia")</li>
</ul>

2. Ao submeter, criar um objeto com os dados do livro e armazenar em uma lista.

3. Criar uma página que exibe todos os livros cadastrados em uma tabela.

4. Colocar um link na última página para cadastrar um novo livro

<p> <strong>Desafio:</strong></p>

Após o cadastro, redirecionar para a página de listagem dos livros.

<hr>

## 2 - Sistema de registro de treinos

Objetivo: Criar uma aplicação para registrar treinos realizados durante a semana.

### Requisitos

1. Criar uma página com um formulário com os seguintes campos:
    
<ul>
    <li>Dia da semana (select: "Segunda", "Terça", ..., "Domingo")</li>
    <li>Nome de exercício (texto)</li>
    <li>Duração em minutos (número inteiro)</li>
</ul>

2. Criar um objeto com os dados enviados e adicionar à lista de treinos.

3. Criar uma rota que exibe todos os treinos em uma tabela.

<p> <strong>Desafio:</strong></p>

Implementar uma filtragem por dia da semana usando query params (ex: /treinos?dia=Segunda).

<hr>

## 3 - Sistema de controle de tarefas

Objetivo: Criar uma API simples de gerenciamento de tarefas (to-do list).

### Requisitos

1. Criar uma página com um formulário com os seguintes campos:
    
<ul>
    <li>Descrição da tarefa (texto)</li>
    <li>Prioridade (select: "Alta", "Média", "Baixa")</li>
    <li>Status (select: "Pendente", "Em Andamento", "Concluída")</li>
</ul>

2. Ao submeter, criar um objeto com os dados da tarefa e armazenar em uma lista.

3. Criar uma página com uma tabela que lista as tarefas com suas informações.

4. Colocar um link na última página para cadastrar uma nova tarefa

<p> <strong>Desafio:</strong></p>

Adicionar um botão para alterar o status da tarefa diretamente na lista (simular com uma rota POST ou PUT).