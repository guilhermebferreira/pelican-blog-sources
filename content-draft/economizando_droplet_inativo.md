Title: Economizando com os Droplets inativos no Digital Ocean
Date: 2017-07-06 17:40
Category: CMS
Tags:  DigitalOcean, Host

![criando-themas](https://cloud.githubusercontent.com/assets/5393392/23138844/653623ec-f788-11e6-8a5f-aa3ca84c9ec9.png)

Quando comecei a interagir com o Digital Ocean, criando droplets para testar aplicações, uma coisa que ficou bem gravada na minha mente foi que 
	- droplets ativos ou inativos geram custos
	- snapshots geram custos

Então acabei não me interessando em usar snapshots e não olhei mais detalhes sobre o assunto.

Recentemnete em uma conversa, alguns amigos que tambem usam, o Digital Ocean, me mostraran uma forma de diminuir custos, quando uma aplicação só precisa funcionar durante periodos especificos do mês (ou mesmo do ano).

Trata-se de...

O custo para mander um snapchot é de 0,05 dolares por giga ao mês

Há varios casos onde isso pode ser útil, alguns casos mais básicos são aplicações ou servidores que são utilizados de forma periodica, mas apenas durante determinado intervalo de tempo, e por isso não precisam ficar disponiveis 24 horas por dia, 7 dias por semana.

