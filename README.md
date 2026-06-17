# FlowChat_Padronizado
O Projeto FlowChat adaptado para os Padrões de Software que melhora a resolução de problemas presentes.

Usando os conceitos de Herança e Polimorfismo, o código foi reestruturado para implementar os seguintes padrões, cada um para lidar com uma questão:
Abstract Factory (Criacional)
Bridge (Estrutural)
Strategy (Comportamental)

1- Problema de Classes Excessivas
Na classe Mensagem, foi implementada o método Bridge, para economizar o espaço que as classes anteriores foram ocupados, já que as subclasses eram muito semelhantes.
Solução (Bridge na classe Mensagem.py)

2- Problema de Gerar o Chat adequado
Para solucionar o problema de diferentes Famílias de Obejtos, implementamos o Abstract Factory na classe Chat, pois as suas subclasses tinham uma série de métodos diferentes.
Solução (Abstract Factory nas classes Chat)

3- Problema da Falta de Variedades
Por fim, para lidar com o problema da falta de opções ao pesquisar por mensagens específicas, implementamos o Strategy na classe Pesquisa para definir diferentes formas de procurar mensagens.
Solução (Strategy na nova classe Pesquisa.py)
