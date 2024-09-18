#HERRAMIENTA DE AUTOMATIZACION DE BUSQUEDAS DE PAGINAS WEB
#AUTOR DEL SCRIPT: ALEJANDRO DORAL

import webbrowser
import time
from colorama import Fore, init

# Inicializa colorama
init(autoreset=True)

time.sleep(2)
print("")
print(Fore.BLUE + "Noticias Ciberseguridad")

time.sleep(2)
print("")
print("Elige la pagina web de noticias de ciberseguridad que te interese:")
print("Elige un numero del 1 al 7, estas son las opciones:")

print("1. The Hacker News")
print("2. Krebs on Security")
print("3. Dark Reading")
print("4. SecurityWeek")
print("5. Cyberscoop")
print("6. WeLiveSecurity")
print("7. ZDNet Security")

time.sleep(2)
print("\n")
respuesta_usuario = input("--->")

match int(respuesta_usuario):
    case 1:
        time.sleep(2)
        print("\n")
        print("Vale, pues vamos a abrir la pagina web de The Hacker News")
        time.sleep(2)
        webbrowser.open("https://thehackernews.com/")

        time.sleep(2)
        print("\n")
        print("¿Ahora cual de las secciones quieres ver?")
        print("Elige un numero del 1 al 4, estas son las opciones:")
        time.sleep(2)
        print("1. Ciberataques")
        print("2. Vulnerabilidades")
        print("3. Expertos en ciberseguridad")
        print("4. Contactar con The Hacker News")
        time.sleep(2)
        print("")
        respuesta_usuario2 = input("--->")

        match int(respuesta_usuario2):
            case 1:
                time.sleep(2)
                print("Vale, pues vamos a abrir la pagina web de Ciberataques")
                time.sleep(2)
                webbrowser.open("https://thehackernews.com/search/label/Cyber%20Attack")
            case 2:
                time.sleep(2)
                print("Vale, pues vamos a abrir la pagina web de Vulnerabilidades")
                time.sleep(2)
                webbrowser.open("https://thehackernews.com/search/label/Vulnerability")
            case 3:
                time.sleep(2)
                print("Vale, pues vamos a abrir la pagina web de Expertos en ciberseguridad")
                time.sleep(2)
                webbrowser.open("https://thehackernews.com/expert-insights/")
            case 4:
                time.sleep(2)
                print("Vale, pues vamos a abrir la pagina web de Contacto")
                time.sleep(2)
                webbrowser.open("https://thehackernews.com/contact-us/")
            case _:
                time.sleep(2)
                print("Opción no válida, tienes que ingresar un número del 1 al 4")

    case 2:
        time.sleep(2)
        print("Vale, pues vamos a abrir la página web de Krebs on Security")
        time.sleep(2)
        webbrowser.open("https://krebsonsecurity.com/")

        print("¿Ahora cuál de las secciones quieres ver?")
        print("Elige un número del 1 al 2, estas son las opciones:")
        time.sleep(2)
        print("1. Acerca del autor")
        print("2. Advertising/Speaking")
        time.sleep(2)
        respuesta_usuario3 = input("--->")

        match int(respuesta_usuario3):
            case 1:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página acerca del autor")
                time.sleep(2)
                webbrowser.open("https://krebsonsecurity.com/about/")
            case 2:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página de Advertising/Speaking")
                time.sleep(2)
                webbrowser.open("https://krebsonsecurity.com/cpm/")
            case _:
                time.sleep(2)
                print("Opción no válida")

    case 3:
        time.sleep(2)
        print("Vale, pues vamos a abrir la página web de Dark Reading")
        time.sleep(2)
        webbrowser.open("https://www.darkreading.com/")
        time.sleep(2)
        print("Parece que en esta ocasión no hay secciones que elegir")

    case 4:
        time.sleep(2)
        print("Vale, pues vamos a abrir la página web de SecurityWeek")
        time.sleep(2)
        webbrowser.open("https://www.securityweek.com/")
        time.sleep(2)
        print("Elige un número del 1 al 5, estas son las opciones:")
        time.sleep(2)
        print("1. Malware")
        print("2. Operaciones de seguridad")
        print("3. Arquitecturas de ciberseguridad")
        print("4. Estrategias de CISO")
        print("5. Conferencias industriales de ciberseguridad")
        time.sleep(2)
        respuesta_usuario4 = input("--->")

        match int(respuesta_usuario4):
            case 1:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página web de Malware")
                time.sleep(2)
                webbrowser.open("https://www.securityweek.com/category/malware-cyber-threats/")
            case 2:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página web de Operaciones de Seguridad")
                time.sleep(2)
                webbrowser.open("https://www.securityweek.com/category/threat-intelligence/")
            case 3:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página web de Arquitectura de Ciberseguridad")
                time.sleep(2)
                webbrowser.open("https://www.securityweek.com/category/security-architecture/")
            case 4:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página web de Estrategias de CISO")
                time.sleep(2)
                webbrowser.open("https://www.securityweek.com/category/ciso-strategy/")
            case 5:
                time.sleep(2)
                print("Vale, pues vamos a abrir la página web de Conferencias Industriales")
                time.sleep(2)
                webbrowser.open("https://www.securityweek.com/category/industrial-security/")
            case _:
                time.sleep(2)
                print("Opción no válida, tienes que ingresar un número")

    case 5:
        time.sleep(2)
        print("")
        print("Vale pues vamos a abrir la pagina web de CyberScoop")
        time.sleep(2)
        webbrowser.open("https://cyberscoop.com/")

        print("Esta pagina web tiene varias categorias")
        print("")
        print("Las categorias son estas:")
        print("1.Aiscoop")
        print("2.Fedscoop")
        print("3.Defenscoop")
        print("4.Cybescoop")
        print("5.Statescoop")
        print("6.Edscoop")
        time.sleep(2)
        print("")
        print("Elige una")
        respuesta_usuario5 = int(input("--->"))

        match respuesta_usuario5:
            case 1:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Aiscoop")
                time.sleep(2)
                webbrowser.open("https://aiscoop.com/")

            case 2:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Fedscoop")
                time.sleep(2)
                webbrowser.open("https://fedscoop.com/")

            case 3:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Defensescoop")
                time.sleep(2)
                webbrowser.open("https://defensescoop.com/")

            case 4:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Cybescoop")
                time.sleep(2)
                webbrowser.open("https://cyberscoop.com/")

            case 5:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Statescoop")
                time.sleep(2)
                webbrowser.open("https://statescoop.com/")

            case 5:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Edscoop")
                time.sleep(2)
                webbrowser.open("https://edscoop.com/")

            case _:
                time.sleep(2)
                print("")
                print("Opcion no valida")
                print("Tienes que ingrear un numero")

    case 6:
        time.sleep(2)
        print("")
        print("Vale pues vamos a abrir la pagina web de WeLiveSecurity")
        time.sleep(2)
        webbrowser.open("https://www.welivesecurity.com/en/")

        print("Esta pagina web tiene varias categorias")
        print("Son estas:")
        print("1.Tips y consejos")
        welivesecuriti1 = "https://www.welivesecurity.com/en/tips-advice/"
        print("Elige una de ellas")
        respuesta_usuario6 = int(input("--->"))
        print("2.Business")
        welivesecuriti2 = "https://www.welivesecurity.com/en/business-security/"
        print("3.Welivesience")
        welivesecuriti3 = "https://www.welivesecurity.com/en/we-live-science/"
        print("4.Scams")
        welivesecuriti4 = "https://www.welivesecurity.com/en/scams/"
        print("5.Privacidad")
        welivesecuriti5 = "https://www.welivesecurity.com/en/privacy/"
        print("6.Kids online")
        welivesecuriti6="https://www.welivesecurity.com/en/kids-online/"
        print("Elige una de ellas")
        respuesta_usuario7 = int(input("--->"))

        match respuesta_usuario7: 
            case 1: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de tips y consejos") #
                time.sleep(2)
                webbrowser.open(welivesecuriti1) #

            case 2: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de business") #
                time.sleep(2)
                webbrowser.open(welivesecuriti2) #

            case 3: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de WeLiveSience") #
                time.sleep(2)
                webbrowser.open(welivesecuriti3) #

            case 4: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web estafas") #
                time.sleep(2)
                webbrowser.open(welivesecuriti4) #

            case 5: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de privacidad") #
                time.sleep(2)
                webbrowser.open(welivesecuriti5) #

            case 6: #
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de kids online") #
                time.sleep(2)
                webbrowser.open(welivesecuriti6) #

            case _:
                time.sleep(2)
                print("")
                print("Opcion no valida")
                print("Tienes que elegir un numero")


    case 7:
        time.sleep(2)
        print("")
        print("Muy bien pues vamos a abrir la pagina web de ZDNet Security")
        time.sleep(2)
        webbrowser.open("https://www.zdnet.com/topic/security/")

        print("Esta pagina web tiene varias categorias")
        print("Son estas:")
        print("1.Cyber Treats")
        ZDNet1 = "https://www.zdnet.com/topic/cyber-threats/"
        print("2.Password Manager")
        ZDNet2 = "https://www.zdnet.com/topic/password-manager/"
        print("3.Ransomware")
        ZDNet3 = "https://www.zdnet.com/topic/ransomware/"
        print("4.VPN")
        ZDNet4 = "https://www.zdnet.com/topic/vpn/"
        time.sleep(2)
        print("")
        print("Elige una de ellas")
        respuesta_usuario8 = int(input("--->"))

        match respuesta_usuario8:
            case 1:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Cyber Treats")
                time.sleep(2)
                webbrowser.open(ZDNet1)
            case 2:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Password Manager")
                time.sleep(2)
                webbrowser.open(ZDNet2)
            case 3:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de Ransomware")
                time.sleep(2)
                webbrowser.open(ZDNet3)
            case 4:
                time.sleep(2)
                print("")
                print("Vale pues vamos a abrir la pagina web de VPN")
                time.sleep(2)
                webbrowser.open(ZDNet4)

            case _:
                time.sleep(2)
                print("")
                print("Esa no es una opcion valida")
                print("Tienes que elegir un numero")
            
    case _:
        time.sleep(2)
        print("Opción no válida, tienes que ingresar un número válido")


time.sleep(2)
print("")
print("Bueno... esas eran todas las paginas web")
print("Quieres ingresar una URL? (SI/NO)")

respuesta_usuario7 = (input("--->"))
respuesta_usuario_url = respuesta_usuario7.lower()

if respuesta_usuario_url == "si":
    time.sleep(2)
    print("")
    print("Vale pues ingresa una URL")
    url_usuario = input("--->")
    
    try:
        webbrowser.open(url_usuario)
    except Exception as e:
        print(e)
        print("Error en la busqueda de tu URL")

elif respuesta_usuario_url == "no":
    time.sleep(2)
    print("")
    print("Esta bien") 
    print("Pues ya hemos acabado...")

else:
    time.sleep(2)
    print("")
    print("Esa no es una respuesta valdia")
    print("Tenias que escribir si o no")


time.sleep(2)
print("")
print("Gracias por usar mi programa!!!")
print("Ha sido un placer ayudarte")
print("Autor del script: Alejandro Doral")
print("")
print("")
