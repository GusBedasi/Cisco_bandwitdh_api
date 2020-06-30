# PROGRAMA CRIADO PARA AUTOMATIZAR CONVERSÃO DE BANDA PARA EQUIPAMENTOS CISCO

* Funcionamento:
 Básicamente o programa acessa esse site de converssão de bandwidth: https://nettools.club/cisco_rlc

 Então o funcionamento se tem por um input do usuário para realizar a conversão de banda inserida para uma entendida por equipamentos Cisco. 

 Exemplo:
 
 Input:
 "Digite a banda desejada: " ==> 10M (10 Megabits por segundo)

 Output:
 [speed]  [normal burst]  [extended burst]
 10485760    1966080         3932160

* Bibilioteca utilizada:
 * Requests do python
