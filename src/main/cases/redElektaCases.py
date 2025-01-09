import json
with open("configuration.json", "r") as config_file:
    configuration = json.load(config_file)

with open("environment.json", "r") as env_file:
    environment = json.load(env_file)

current_environment = configuration["environment"]
username = environment[current_environment]["accounts"]["sharedAccount"]["username"]
password = environment[current_environment]["accounts"]["sharedAccount"]["password"]

CREDENCIALES_VALIDAS ={
    "username": username,
    "password": password,
}

CREDENCIALES_INVALIDAS = {
    "usename":"credencial-Invalida",
    "password":"897379234"
}