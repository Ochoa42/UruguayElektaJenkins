import json
import requests
from main.cases.redElektaCases import CREDENCIALES_VALIDAS

with open("configuration.json", "r") as config_file:
    configuration = json.load(config_file)

with open("environment.json", "r") as env_file:
    environment = json.load(env_file)

current_environment = configuration["environment"]
username = environment[current_environment]["accounts"]["sharedAccount"]["username"]
password = environment[current_environment]["accounts"]["sharedAccount"]["password"]
urlBase = environment[current_environment]["urlBase"]
def test_login():
    try:
        response = requests.post(f"{urlBase}/adm-login",json=CREDENCIALES_VALIDAS)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == "Login successfu",f"Mensaje inesperado:{datos['message']}"
        print("login_esitoso: prueba exitosa")
        return datos['data']['token']
    except Exception as e:
        print(f"test_login: Prueba fallida {e}")
        