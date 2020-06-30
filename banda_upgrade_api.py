import requests

def banda_request():
    banda_input = input("Digite a banda desejada: ")
    req = requests.post('https://nettools.club/_cisco_rlc_ajax', data = {'inspeed': banda_input})
    print(req.text)

banda_request()