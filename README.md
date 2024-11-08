<h1 align="center">Games Portal</h1>
<p align="center">
  <img src="https://img.shields.io/badge/html-v5.2-orange" />
  <img src="https://img.shields.io/badge/css-v3-blue" />
  <img src="https://img.shields.io/badge/javascript-ECMAScript%202018-yellow" />
</p>

## Tabela de Conteúdo

- [Tabela de Conteúdo](#tabela-de-conte%C3%BAdo)
- [Sobre o Projeto](#sobre-o-projeto)
  - [Disciplina de Interfaces com HTML e CSS](#disciplina-de-interfaces-com-html-e-css)
  - [Disciplina de Javascript](#no-projeto-de-javascript).
  - [Feito Com](#feito-com)
- [Começando](#come%C3%A7ando)
  - [Pré-requisitos](#pr%C3%A9-requisitos)
  - [Estrutura de Arquivos](#estrutura-de-arquivos)
  - [Instalação](#instala%C3%A7%C3%A3o)
- [Contribuição](#contribui%C3%A7%C3%A3o)
- [Contato](#contato)

## Sobre o Projeto

Este site / sistema web proporciona a integração entre as disciplinas regulares de Interfaces Web e Javascript.

Na disciplina de Javascript, foi o desenvolvimento de um jogo da memória utilizando as
técnicas desta disciplina. Descrição da parte do [javascript](#no-projeto-de-javascript).

Para a disciplina de Interfaces Web foi o desenvolvimento de um portal de games, contendo o detalhamento a seguir. O projeto se adequa em diferentes dispositivos, sendo responsivo. Portanto, foi necessário utilizar as media-queries necessárias para uma correta visualização em celulares, tablets e desktops, mesmo que de forma simplificada.

### Disciplina de Interfaces com HTML e CSS

Etapas do projeto :

### Etapa 1:

- Construa uma Página Inicial para o seu portal de games contendo uma barra de navegação principal e itens de menu de acesso as demais páginas, logotipo centralizado e uma capa/cover de destaque com imagem do seu jogo, com link às páginas internas do seu trabalho. Na navegação, destaque o item de menu para login ou registro no seu portal de jogos (destaque pode ser feito com cores ou tipografia ou ambos). Para este item, crie um submenu / dropdown com os itens login e registro/cadastro. Os itens de navegação devem ter algum destaque para o efeito hover do mouse (a navegação deverá ser feita com as tags de lista). Insira um box para busca / search.

- Ainda nessa página, insira 3 sub-destaques para itens fictícios do seu portal. Faça a marcação html para os itens, mesmo que sejam fictícios. O sub-destaque será composto de imagem e descrição. A imagem receberá algum tipo de destaque no efeito hover do mouse, como animate ou rotate, ou qualquer técnica de sua escolha, via css.

- Crie ainda uma seção com pequenos e breves comentários de supostos usuários do seu portal, com background em css gradiente.

- No rodapé, insira links para as redes sociais, utilizando a técnica de css sprites, além de itens de menu de forma simplificada, para acesso às demais áreas do seu site.

### Etapa 2:

- Construa uma página de detalhamento do seu portal de jogos, denominada
“Sobre”. Esta página deverá seguir a estrutura estética aplicada na criação do logotipo,
contendo o seu nome ou sobrenome. Para criação do logotipo, utilizem as ferramentas
gratuitas e simplificadas: 
- Canva (https://www.canva.com/pt_br/);
- FreeLogo Design (https://pt.freelogodesign.org/);
- Logo Genio (https://www.logogenio.pt/design-de-logotipo).

- Nesse detalhamento, insira, no mínimo, dois parágrafos expondo a história do seu game,
e mais dois parágrafos detalhando a estrutura do projeto integrado entre as DRs de
Interfaces e Javascript. Por fim, detalhe, com no mínimo dois parágrafos, a sua
experiencia no desenvolvimento das suas entregas deste bloco.

- As 3 áreas terão título de acordo com a hierarquia solicitada.

- Em todas as páginas internas, deve-se manter a estrutura de topo e rodapé.

### Etapa 3:

- Desenvolva uma página para área de contato contendo formulário para envio de sugestões, reclamações e/ou elogios. Deve-se permitir o preenchimento de nome, email, campo para seleção do Game(select), caso tenha mais de um, e campo para descrição/detalhamento (textarea). Todos os campos deverão ter Label. No Select, insira dois ou mais itens com atributo disabled.

- Em todas as páginas internas, deve-se manter a estrutura de topo e rodapé.

### Etapa 4:

Desenvolva uma página de notícias e informações relevantes ao mundo de games. Deve-se ter um artigo principal com links relacionados ao final do artigo. Também deverá ter link para 3 notícias com imagem e legenda com links.

- Em todas as páginas internas, deve-se manter a estrutura de topo e rodapé.

### Etapa 5:

- Desenvolva uma página de Login / Registro, que será uma area dedicada a login de usuários cadastrados, ou registro de usuários ainda não cadastrados. Simule o acesso as duas áreas na mesma página, utilizando técnica de exibir ou esconder, via css, a partir
de chamadas de links. Técnicas livres. Ao acessar, faça ancoragem para elementos da página, como formulário de login já exibido inicialmente e formulário de cadastro exibido a partir de clique em item do formulário, para quem não é registrado.

- Após o fluxo de login, deve-se exibir área do cadastro do usuário logado, incluindo
as possíveis interações que este tenha com o sistema, anteriormente, como compras de
jogos ou créditos online no formato de dados tabulares - tabela (apenas simule com as
marcações html).

- Em todas as páginas internas, deve-se manter a estrutura de topo e rodapé.

### Etapa 6:

- Por fim, desenvolva uma página de jogos com destaque para o jogo desenvolvido
no projeto do AT de JavaScript. Exiba um breve detalhe sobre o jogo e o processo de
desenvolvimento. 

- Ao acessar o link principal, dê acesso ao jogo da memória, com topo e rodapé
seguindo a estética das outras páginas.

### No projeto de Javascript

Um aplicativo que apresenta um tabuleiro de jogo da memória (4x4, 8 pares de figuras), um botão que permita iniciar/reiniciar o jogo e um botão para mostrar o melhor tempo de jogo (que deve ser armazenado entre desligamentos do aplicativo). Além disso, Nossas 16 figuras são as cartas que precisamos parear.

- Após o carregamento da página, o app deve mostrar todas as cartas desviradas e em pares conforme condição inicial do vídeo exemplo;
Ao clicar no botão iniciar/reiniciar jogo, o app deve embaralhar as cartas usando uma função pseudo-randômica, posicioná-las no tabuleiro e mostrá-las desviradas ao jogador por 3 segundos;
- Ao clicar sobre uma carta, ela deve ser desvirada. Caso seja a segunda carta desvirada, deve-se testar a igualdade das cartas; se formarem um par permanecem desviradas, senão, voltam a ser viradas após um intervalo de 1,5 segundos (para que o usuário veja qual foi a segunda carta);
- Após todas as cartas terem sido desviradas, o jogo termina;
- Após desvirar a segunda carta, não deve ser possível virar uma terceira até que seja verificada a paridade e desferido o resultado da verificação;
- A medição de tempo de jogo deve ser feita entre o click de iniciar o jogo até o momento em que todas as cartas encontrem seus pares.

### Feito Com

Segue abaixo o que foi utilizado:

- [Visual Studio Code](https://code.visualstudio.com/) - O Visual Studio Code é um editor de código-fonte desenvolvido pela Microsoft para Windows, Linux e macOS. Ele inclui suporte para depuração, controle Git incorporado, realce de sintaxe, complementação inteligente de código, snippets e refatoração de código.
- [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - HTML(Linguagem de Marcação de HiperTexto) é o bloco de construção mais básico da web. Define o significado e a estrutura do conteúdo da web.
- [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - CSS (Cascading Style Sheets ou Folhas de Estilo em Cascata) é uma linguagem de estilo usada para descrever a apresentação de um documento escrito em HTML ou em XML (incluindo várias linguagens em XML como SVG, MathML ou XHTML). O CSS descreve como elementos são mostrados na tela, no papel, na fala ou em outras mídias.
- [JavaScript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript) - JavaScript® (às vezes abreviado para JS) é uma linguagem leve, interpretada e baseada em objetos com funções de primeira classe, mais conhecida como a linguagem de script para páginas Web, mas usada também em vários outros ambientes sem browser, tais como node.js,  Apache CouchDB e Adobe Acrobat. O JavaScript é uma linguagem baseada em protótipos, multi-paradigma e dinâmica, suportando estilos de orientação a objetos, imperativos e declarativos (como por exemplo a programação funcional).

## Começando

Para conseguir utilizar ou visualizar o projeto, seja através do Visual Studio Code ou outro editor de código, siga os passos abaixo:

### Pré-requisitos

Antes de seguirmos para as configurações e uso do projeto, é ideal que você tenha o git instalado e configurado, para isso você pode seguir o link abaixo.

[Git - Book](https://git-scm.com/book/pt-br/v2)

### Estrutura de Arquivos

A estrutura de arquivos está da seguinte maneira:

```bash
games-portal
├── css/
│   ├── style.css
│   │
│   images/
│   │
│   js/
│   ├── script.js
│   │
│   ├── css/
│       └── style.css
│     
├── about.html
├── contact.html
├── games.html
├── home.html
├── index.html
├── login.html
├── memory-game.html
├── news.html
├── register.html
└── README.md
```

### Instalação

- Para instalar e utilizar esse projeto, o processo é bem simples. Basta utilizar o seguinte comando no terminal:

```sh
git clone https://github.com/MTevangelista/memory-game.git
```
---

## Contribuição

Contribuições são o que fazem a comunidade open source um lugar incrível para aprender, inspirar e criar. Qualquer contribuição que você fizer será **muito apreciada**.

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/FeatureIncrivel`)
3. Adicione suas mudanças (`git add .`)
4. Comite suas mudanças (`git commit -m 'Adicionando uma Feature incrível!`)
5. Faça o Push da Branch (`git push origin feature/FeatureIncrivel`)
6. Abra um Pull Request

## Contato

👤  **Matheus Evangelista**

- Linkedin: [@MatheusEvangelista](https://www.linkedin.com/in/matheus01/)
- Github: [@MTevangelista](https://github.com/MTevangelista?tab=repositories)
- Instagram: [@_matheusrj](https://www.instagram.com/_matheusrj/?hl=pt-br)
