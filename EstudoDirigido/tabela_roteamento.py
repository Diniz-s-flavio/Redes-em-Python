import subprocess
import platform

def get_routing_table():
    so = platform.system()
    
    comando = ["route", "print"]
    
    resultado = subprocess.run(comando, capture_output=True, text=True)
    print(resultado.stdout)

get_routing_table()