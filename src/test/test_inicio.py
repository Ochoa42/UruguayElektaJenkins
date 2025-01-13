import json
import requests
#from main.cases.redElektaCases import CREDENCIALES_VALIDAS

# with open("configuration.json", "r") as config_file:
#     configuration = json.load(config_file)

with open("environment.json", "r") as env_file:
    environment = json.load(env_file)

url_base = environment["test"]["urlBase"]
user_Root = environment["test"]["accounts"]["sharedAccount"]["userRoot"]
apiKey = environment["test"]["accounts"]["sharedAccount"]["apiKey"]
#headers = environment["test"]["accounts"]["sharedAccount"]["Headers"]
# current_environment = configuration["environment"]
# username = environment[current_environment]["accounts"]["sharedAccount"]["username"]
# password = environment[current_environment]["accounts"]["sharedAccount"]["password"]
# urlBase = environment[current_environment]["urlBase"]


def obtenerToken():
    response = requests.post(f"{url_base}/adm-login", data=user_Root)
    response.raise_for_status()
    datos = response.json()
    return datos['data']['token']

def test_login():
    try:
        print("mi ruta base",url_base)
        response = requests.post(url_base+"/adm-login",data=user_Root)
        datos = response.json()
        assert datos["success"] == True, f"Error en el login: {datos.get('message', 'Sin mensaje')}"
        assert "token" in datos["data"], "Falta el token en la respuesta"
        assert "user" in datos["data"], "Falta la información del usuario en la respuesta"
        print("Test de login exitoso")
    except Exception as e:
        assert False, f"Test de login fallido: {e}"

def test_getListasUruguay():
    try:
        access_token = obtenerToken()
        headers =  {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url_base+"/listas?fullType=L",headers=headers)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == True, f"Error en la lista de listas: {datos.get}"
    except Exception as e:
        assert False, f"Test de lista fallido: {e}"

def test_getMunicipiosUruguay():
    try:
        access_token = obtenerToken()
        headers =  {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url_base+"/muns?fullType=L",headers=headers)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == True, f"Error en la lista de municipios: {datos.get}"
    except Exception as e:
        assert False, f"Error al obtener token: {e}"

def test_getMunicipiosExtraUruguay():
    try:
        access_token = obtenerToken()
        headers =  {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url_base+"/muns?fullType=EXTRA",headers=headers)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == True, f"Error en la lista de municipios Extras: {datos.get}"
    except Exception as e:
        assert False, f"Error al obtener token: {e}"

def test_getRolesUruguay():
    try:
        access_token = obtenerToken()
        headers =  {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url_base+"/roles?fullType=L&perPage=-1",headers=headers)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == True, f"Error en la lista de roles: {datos.get}"
    except Exception as e:
        assert False, f"Error al obtener token: {e}"

def test_getRolesExtraUruguay():
    try:
        access_token = obtenerToken()
        headerv =  {"Authorization": f"Bearer {access_token}"}
        response = requests.get(url_base+"/roles?fullType=EXTRA&perPage=-1", headers=headerv)
        response.raise_for_status()
        datos = response.json()
        assert datos["success"] == True, f"Error en la lista de roles Extras: {datos.get}"
    except Exception as e:
        assert False, f"Error al obtener token: {e}"
                                