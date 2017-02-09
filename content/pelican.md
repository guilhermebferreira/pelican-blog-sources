Title: Criando um blog estatico com Pelican
Date: 2017-01-23 17:20
Category: CMS
Tags: CMS, Pelican

![Pelican - sites estáticos][1]

[1]: /images/pelican.png

[Pelican](https://github.com/getpelican/pelican) é um gerador de sites estaticos, escrito em Python.

Sua instalação e execução é bastante simples e depende de poucas linhas de comando.

#Instalação e configuraçao do Pelican
	pip3 install pelican markdown
	pelican-quickstart 

#Execução do pelican em abiente de local
	cd output/
	python3 -m pelican.server

#Criação de conteúdo
Para criar conteudo, basta criar arquivos de texto dentro do diretório content/ utilizando a extenção .md ([markdown](http://daringfireball.net/projects/markdown/) )
Os metadados devem ser informado no inicio do arquivo como o exemplo abaixo:

	Title: Criando um blog estatico com Pelican
	Date: 2017-01-23 17:20
	Category: CMS

Depois basta rodar o comando 

	pelican content