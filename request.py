import requests

def funcao_request(nome_site):
    informacao = requests.get(nome_site)
    return informacao.text
    print(informacao.text)

if __name__ == "__main__":

    funcao_request( "https://www.devmedia.com.br/javascript-concat-concatenando-arrays-e-strings/37964" )