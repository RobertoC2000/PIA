import argparse
import Cifrado_Cesar
import Crackeo_Cesar
import Descifrado_Cesar
import Email
import Metadatos
import Escaneo_Web
import Hash
import logging

def main():
	class SmartFormatter(argparse.HelpFormatter):
		def _split_lines(self, text, width):
			# this is the RawTextHelpFormatter._split_lines
			if text.startswith('R|'):
				return text[2:].splitlines()
			return argparse.HelpFormatter._split_lines(self, text, width)

	logging.basicConfig(
		format='%(asctime)s %(message)s',
		filename='logg.txt',
		filemode='a')
	parser = argparse.ArgumentParser(description = '**************************** SCRIPT MULTITAREAS PARA CIBERSEGURIDAD ****************************', formatter_class=SmartFormatter)


	parser.add_argument(
		'-herramienta',choices = ['1','2','3','4','5','6','7'],
		help="R|************************ SELECCIONE UN HERRAMIENTA ************************\n"
					' 1. Cifrado Cesar\n'
			 		' 2. Descifrado Cesar\n'
			 		' 3. Crackeo Cesar\n'
			 		' 4. Obtencion de metadatos\n'
			 		' 5. Obtención de claves HASH\n'
			 		' 6. Escaneo de páginas Web\n'
			 		' 7. Envio de archivos adjuntos por email\n'
					'***********************************************************************')

	#Argumento para la herramienta de metadatos
	parser.add_argument(
		'-c', '--config', help = 'Ingrese la ruta de la carpeta en donde se encuentran las imagenes para la obtención de sus metadatos.', )

	args = parser.parse_args()

	#Herramientas
	if args.herramienta == "1":
		Cifrado_Cesar.Cifrar()

	if args.herramienta == "2":
		Descifrado_Cesar.Descifrar()

	if args.herramienta == "3":
		Crackeo_Cesar.Hackear()

	if args.herramienta == "4":
		Metadatos.printMeta(args.config)

	if args.herramienta == "5":
		Hash.Obtener_Claves()
	
	if args.herramienta == "6":
		Escaneo_Web.Scan()

	if args.herramienta == "7":
		Email.Enviar_Correo()	

if __name__ == "__main__":
	main()
