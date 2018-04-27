import requests
from bs4 import BeautifulSoup

def carregaTabela():
  url = "https://www.animestelecine.net"
	r = requests.get(url)
	bsObj = BeautifulSoup(r.text, "html.parser")
	bloco = bsObj.findAll("div", {"class":"container-download-epi"})
	lista = []
	for x in bloco:
		nome = x.find("h2")
		link = x.find("a")
		uploader = x.find("div", {"style":"width: auto;min-width: 170px;"})
		fansub = x.find("div", {"style":"min-width: 150px;"})

		linksmp4 = x.find("div", {"class": "links_mp4"})
		linksmp4Download = linksmp4.findAll("div", {"class":"botao-download"})

		links720p = x.find("div", {"class": "links_720p"})
		links720pDownload = links720p.findAll("div", {"class":"botao-download"})

		links1080p = x.find("div", {"class": "links_1080p"})
		links1080pDownload = links1080p.findAll("div", {"class":"botao-download"})


		#linksmp4
		link_mp4 = {}
		link_720p = {}
		link_1080p = {}

		for mp4link in linksmp4Download:
			nomeDownload = mp4link.find("span", {"class": "btn-download-words"})
			link_mp4[nomeDownload.text] = mp4link['data-urltratada']

		for l720link in linksmp4Download:
			nomeDownload = l720link.find("span", {"class": "btn-download-words"})
			link_720p[nomeDownload.text] = l720link['data-urltratada']

		for l1080link in linksmp4Download:
			nomeDownload = l1080link.find("span", {"class": "btn-download-words"})
			link_1080p[nomeDownload.text] = l1080link['data-urltratada']

		dict = {
				"nome": nome.text.lstrip(),
				"linkPagina": link['href'],
				"uploader": uploader.text,
				"fansub" : fansub.text,
				"download" : {
							"mp4" : link_mp4,
							"720p" : link_720p,
							"1080p" : link_1080p
							}
				}
		lista.append(dict)
	print(lista)
#links-down-epi

carregaTabela()
