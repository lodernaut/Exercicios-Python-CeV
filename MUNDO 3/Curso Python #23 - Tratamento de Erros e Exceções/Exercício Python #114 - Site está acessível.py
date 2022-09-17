import urllib.request


def conecta(host):
    try:
        url = host
        req = urllib.request.Request(url, headers={
                                     'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36"})
        urllib.request.urlopen(req)
        # o Request faz a identificação como browser perante o site e assim o acesso fica liberado.
    except:
        return False
    else:
        return True


# Programa principal
site = 'https://www.estadao.com.br/politica/eleicoes/feed-estadao/?liveId=7LIRJSG5ONGKTAOPA4UZIJHUKY&offset=0?utm_source=twitter:newsfeed&utm_medium=social-organic&utm_campaign=redes-sociais:092022:e&utm_content=:::&utm_term='
conecta(site)
print(f'Site → ( {site} )\nestá acessivel.' if conecta(
    site) else f'Site → ( {site} )\nNÃO está acessível.')
