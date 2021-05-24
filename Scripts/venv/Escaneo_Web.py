import requests
import json
import logging
import getpass

def Scan():

	#Ingrese aqui el nombre de su archivo con las urls a escanear o solo configure el archivo que esta por defecto
	f = open('URL.txt')
	urls = f.read().splitlines()
	try:
		Api_key = getpass.getpass("Ingrese el Api Key: ")
		url = 'https://www.virustotal.com/vtapi/v2/url/report'
	
		parametros = {"apikey": Api_key, "resource": urls}
	
		response = requests.get(url=url, params=parametros)
		json_response = json.loads(response.text)
	
		for i in urls:
			parametros = {"apikey": Api_key, "resource": i}
			response = requests.get(url=url, params=parametros)
			json_response = json.loads(response.text)
			try:
				if json_response['response_code'] <= 0:
					with open('Resultado_Escaneo.txt', 'a') as Archivo:
						Archivo.write(i) ^ Archivo.write("\tno se encontro, por favor escanear manualmente\n")
					print("La página: "+ i + " no se encontro, por favor escanear manualmente")
				elif json_response['response_code'] >= 1:
					if json_response['positives'] <= 0:
						with open('Resultado_Escaneo.txt', 'a') as Archivo:
							Archivo.write(i) ^ Archivo.write("\tno es maliciosa\n")
						print("La página: " + i + " no es maliciosa")
					else:
						with open('Resultado_Escaneo.txt', 'a') as Archivo:
							Archivo.write(i) ^ Archivo.write("\tes maliciosa\n")
						print("La página: " + i + " es maliciosa")
			except:
				pass
	except json.decoder.JSONDecodeError:
		logging.error("Error[Escaneo_Web.py]! --> La API ingresada no existe")
		print('********************************************************** Se ha detectado un error, revise el archivo logg.txt **********************************************************')