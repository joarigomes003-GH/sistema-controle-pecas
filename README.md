# Sistema de Automação de Controle de Peças

## 📌 Descrição
Este projeto foi desenvolvido em Python com o objetivo de simular um sistema de controle de qualidade de peças em uma linha de produção industrial.

O sistema realiza:
- Cadastro de peças
- Validação automática de qualidade
- Armazenamento em caixas
- Geração de relatórios

---

## ⚙️ Funcionalidades

1 - Cadastrar peça  
2 - Listar peças aprovadas e reprovadas  
3 - Remover peça  
4 - Listar caixas fechadas  
5 - Gerar relatório final  

---

## 🧠 Regras de Validação

- Peso: entre 95g e 105g  
- Cor: azul ou verde  
- Comprimento: entre 10cm e 20cm  

---

## 📦 Sistema de Armazenamento

- Cada caixa comporta 10 peças aprovadas  
- Ao atingir o limite, a caixa é fechada automaticamente  

---

## ▶️ Como executar o programa

1. Instale o Python
2. Instale a biblioteca necessária:

pip install colorama

3. Execute o programa:

python sistema.py

---

## 🧪 Exemplo de uso

Entrada:
- Peso: 100
- Cor: azul
- Comprimento: 15

Saída:
- Peça APROVADA  
- Armazenada na caixa  

---

## 🎯 Objetivo do Projeto

Demonstrar na prática conceitos de lógica de programação, estruturas de decisão e repetição, além de simular um cenário real da indústria com automação de processos.
