import requests

def banda_request():
    banda_input = input("Digite a banda desejada: ")
    req = requests.post('https://nettools.club/_cisco_rlc_ajax', data = {'inspeed': banda_input})
    response = (req.text).split(' ')

    print("[speed]  [normurst]  [extended burst]")
    print(response[0], str(" " * 1) ,response[1], str(" " * 4) ,response[2])

banda_request()