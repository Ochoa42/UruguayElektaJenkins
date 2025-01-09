import json
import requests

with open("configuration.json", "r") as config_file:
    configuration = json.load(config_file)

with open("environment.json", "r") as env_file:
    environment = json.load(env_file)

current_environment = configuration["environment"]
username = environment[current_environment]["accounts"]["sharedAccount"]["username"]
password = environment[current_environment]["accounts"]["sharedAccount"]["password"]

def test_create_comunicacion():
    try:
        response = requests.post()
        print("sdf")
    except Exception as e:
        print(f"An error occurred: {e}")
        