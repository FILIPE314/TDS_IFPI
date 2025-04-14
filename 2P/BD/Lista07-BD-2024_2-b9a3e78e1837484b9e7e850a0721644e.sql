-- Criação da tabela Aluno
CREATE TABLE Aluno (
    aluno_id NUMERIC(6, 0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL
);

-- Criação da tabela Disciplina
CREATE TABLE Disciplina (
    disciplina_id NUMERIC(6, 0) PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    carga_horaria INT NOT NULL,
    quantidade_maxima_alunos INT NOT NULL
);

-- Criação da tabela Matrícula
CREATE TABLE Matricula (
    matricula_id NUMERIC(6, 0) PRIMARY KEY,
    aluno_id NUMERIC(6, 0) NOT NULL,
    disciplina_id NUMERIC(6, 0) NOT NULL,
    faltas INT DEFAULT 0,
    media NUMERIC(5, 2) DEFAULT 0.00,
    CONSTRAINT fk_aluno FOREIGN KEY (aluno_id) REFERENCES Aluno(aluno_id) ON DELETE CASCADE,
    CONSTRAINT fk_disciplina FOREIGN KEY (disciplina_id) REFERENCES Disciplina(disciplina_id) ON DELETE CASCADE,
    UNIQUE (aluno_id, disciplina_id) -- Garante que o mesmo aluno não se matricule duas vezes na mesma disciplina
);

-- Inserção de dados na tabela Aluno
INSERT INTO Aluno (aluno_id, nome, data_nascimento) VALUES
(1, 'Fulano', '2005-01-01'),
(2, 'Beltrano', '2005-02-02'),
(3, 'Cicrano', '2005-03-03'),
(4, 'Joaozinho', '2005-04-04'),
(5, 'Pedrinho', '2005-05-05'),
(6, 'Goku', '2005-06-06'),
(7, 'Pelé', '2005-07-07'),
(8, 'Romário', '2005-08-08'),
(9, 'Zezinho', '2005-09-09'),
(10, 'Luizinho', '2005-10-10'),
(11, 'Mariazinha', '2005-11-11'),
(12, 'Chiquinho', '2005-12-12'),
(13, 'Fred', '2005-01-13'),
(14, 'George', '2005-02-14'),
(15, 'Paul', '2005-03-15'),
(16, 'Ringo', '2005-04-16'),
(17, 'Bruce', '2005-05-17'),
(18, 'Clark', '2005-06-18'),
(19, 'Diana', '2005-07-19'),
(20, 'Barry', '2005-08-20'),
(21, 'Arthur', '2005-09-21'),
(22, 'Victor', '2005-10-22'),
(23, 'Natasha', '2005-11-23'),
(24, 'Wanda', '2005-12-24'),
(25, 'Steve', '2005-01-25'),
(26, 'Tony', '2005-02-26'),
(27, 'Peter', '2005-03-27'),
(28, 'T’Challa', '2005-04-28'),
(29, 'Logan', '2005-05-29'),
(30, 'Scott', '2005-06-30');

-- Inserção de dados na tabela Disciplina
INSERT INTO Disciplina (disciplina_id, nome, carga_horaria, quantidade_maxima_alunos) VALUES
(1, 'Matemática', 40, 30),
(2, 'Português', 60, 30),
(3, 'História', 60, 30),
(4, 'Geografia', 80, 30),
(5, 'Ciências', 90, 30);

-- Inserção de dados na tabela Matrícula
-- 5 alunos matriculados em apenas 1 disciplina
INSERT INTO Matricula (matricula_id, aluno_id, disciplina_id, faltas, media) VALUES
(1, 1, 1, 10, 8.5),
(2, 2, 2, 5, 7.3),
(3, 3, 3, 8, 6.1),
(4, 4, 4, 3, 9.4),
(5, 5, 5, 7, 5.2);

-- 6 alunos matriculados em 2 disciplinas
INSERT INTO Matricula (matricula_id, aluno_id, disciplina_id, faltas, media) VALUES
(6, 6, 1, 2, 9.8), (7, 6, 2, 6, 7.0),
(8, 7, 2, 1, 6.7), (9, 7, 3, 4, 8.1),
(10, 8, 3, 0, 7.5), (11, 8, 4, 9, 5.9),
(12, 9, 4, 2, 9.0), (13, 9, 5, 5, 8.3),
(14, 10, 1, 6, 4.5), (15, 10, 5, 3, 6.9),
(16, 11, 1, 10, 5.4), (17, 11, 3, 7, 6.8);

-- 7 alunos matriculados em 3 disciplinas
INSERT INTO Matricula (matricula_id, aluno_id, disciplina_id, faltas, media) VALUES
(18, 12, 1, 5, 7.4), (19, 12, 2, 4, 6.3), (20, 12, 3, 8, 9.2),
(21, 13, 2, 2, 5.7), (22, 13, 3, 6, 8.6), (23, 13, 4, 1, 7.8),
(24, 14, 3, 3, 9.4), (25, 14, 4, 7, 5.1), (26, 14, 5, 6, 6.4),
(27, 15, 4, 2, 8.0), (28, 15, 5, 10, 5.9), (29, 15, 1, 4, 6.7),
(30, 16, 5, 8, 7.5), (31, 16, 1, 5, 6.1), (32, 16, 2, 3, 8.9),
(33, 17, 1, 6, 7.8), (34, 17, 3, 0, 5.6), (35, 17, 5, 2, 9.1),
(36, 18, 2, 9, 8.4), (37, 18, 4, 7, 5.3), (38, 18, 5, 1, 6.2);

-- 8 alunos matriculados em 4 disciplinas
INSERT INTO Matricula (matricula_id, aluno_id, disciplina_id, faltas, media) VALUES
(39, 19, 1, 4, 9.0), (40, 19, 2, 3, 8.1), (41, 19, 3, 5, 7.4), (42, 19, 4, 7, 6.8),
(43, 20, 2, 2, 9.7), (44, 20, 3, 4, 5.6), (45, 20, 4, 1, 8.3), (46, 20, 5, 8, 6.0),
(47, 21, 3, 6, 7.2), (48, 21, 4, 5, 8.8), (49, 21, 5, 3, 9.1), (50, 21, 1, 2, 5.4),
(51, 22, 4, 1, 6.9), (52, 22, 5, 3, 8.4), (53, 22, 1, 4, 7.0), (54, 22, 2, 9, 5.8),
(55, 23, 5, 7, 6.1), (56, 23, 1, 8, 7.5), (57, 23, 2, 6, 5.7), (58, 23, 3, 4, 8.2),
(59, 24, 1, 5, 9.3), (60, 24, 2, 6, 7.4), (61, 24, 4, 8, 6.5), (62, 24, 5, 2, 7.1),
(63, 25, 2, 7, 8.5), (64, 25, 3, 3, 5.6), (65, 25, 4, 1, 9.0), (66, 25, 5, 9, 6.3),
(67, 26, 1, 4, 7.8), (68, 26, 3, 8, 8.0), (69, 26, 4, 6, 6.2), (70, 26, 5, 7, 5.9);

-- 4 alunos matriculados em 5 disciplinas
INSERT INTO Matricula (matricula_id, aluno_id, disciplina_id, faltas, media) VALUES
(71, 27, 1, 9, 7.4), (72, 27, 2, 8, 6.3), (73, 27, 3, 6, 9.2), (74, 27, 4, 7, 5.1), (75, 27, 5, 3, 8.0),
(76, 28, 1, 2, 6.7), (77, 28, 2, 5, 8.9), (78, 28, 3, 8, 7.5), (79, 28, 4, 6, 9.3), (80, 28, 5, 4, 5.8),
(81, 29, 1, 5, 9.8), (82, 29, 2, 4, 8.6), (83, 29, 3, 7, 6.4), (84, 29, 4, 8, 5.7), (85, 29, 5, 3, 7.9),
(86, 30, 1, 6, 8.3), (87, 30, 2, 3, 6.5), (88, 30, 3, 8, 9.1), (89, 30, 4, 5, 7.2), (90, 30, 5, 7, 6.6);
