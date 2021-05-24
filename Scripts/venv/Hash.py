import subprocess

def Obtener_Claves():

	comando = "HashAcquire.ps1"
	lineaPS = "powershell -Executionpolicy ByPass -file " + comando
	runningProcesses = subprocess.check_output(lineaPS)
	print(lineaPS)
	print("Las claves se han generado exitosamente en el txt")