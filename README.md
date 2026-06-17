FlowChat Padronizado

Descrição

O FlowChat Padronizado é uma adaptação do projeto FlowChat cujo objetivo é aplicar padrões de projeto (Design Patterns) para melhorar a organização do código, reduzir duplicações e facilitar sua manutenção e expansão.

A refatoração foi baseada nos princípios de Herança e Polimorfismo, utilizando padrões de software para resolver problemas específicos identificados na implementação original.

Padrões Implementados

- Abstract Factory (Criacional)
- Bridge (Estrutural)
- Strategy (Comportamental)

---

1. Bridge – Redução de Classes Excessivas

Problema

A implementação original possuía diversas subclasses de "Mensagem" que apresentavam diferenças mínimas entre si, resultando em duplicação de código e dificuldade de manutenção.

Solução

Foi aplicado o padrão Bridge na classe "Mensagem", separando a abstração da implementação. Dessa forma, diferentes tipos de mensagens podem compartilhar a mesma estrutura sem a necessidade de criar uma nova subclasse para cada variação.

Arquivos envolvidos:

- "Mensagem.py"

Benefícios obtidos:

- Redução da quantidade de classes;
- Eliminação de código duplicado;
- Maior facilidade para adicionar novos tipos de mensagem.

---

2. Abstract Factory – Criação de Chats

Problema

Cada tipo de chat possuía características e comportamentos próprios, tornando a criação dos objetos dependente de diversas subclasses específicas.

Solução

Foi implementado o padrão Abstract Factory para encapsular a criação das diferentes famílias de objetos relacionadas aos chats. Assim, cada fábrica é responsável por instanciar o conjunto correto de objetos sem que o restante do sistema conheça sua implementação.

Arquivos envolvidos:

- Classes relacionadas a "Chat"

Benefícios obtidos:

- Desacoplamento entre criação e utilização dos objetos;
- Facilidade para adicionar novos tipos de chat;
- Código mais organizado e extensível.

---

3. Strategy – Pesquisa de Mensagens

Problema

O sistema possuía apenas uma forma de pesquisar mensagens, dificultando a implementação de novos critérios de busca.

Solução

Foi criado o módulo "Pesquisa.py", utilizando o padrão Strategy para encapsular diferentes algoritmos de pesquisa. Cada estratégia representa uma forma distinta de localizar mensagens, permitindo trocar o algoritmo em tempo de execução.

Arquivos envolvidos:

- "Pesquisa.py"

Benefícios obtidos:

- Inclusão de novos métodos de pesquisa sem modificar o código existente;
- Maior flexibilidade;
- Melhor aderência ao princípio Open/Closed (OCP).

---

Resultado

Com a aplicação dos padrões Bridge, Abstract Factory e Strategy, o projeto passou a apresentar uma arquitetura mais modular, reutilizável e de fácil manutenção. Além de resolver problemas específicos da implementação original, essas mudanças tornam o sistema mais preparado para futuras expansões e servem como exemplo prático da utilização de padrões de projeto em Python.
