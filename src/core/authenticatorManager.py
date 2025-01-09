import json

with open("configuration.json", "r") as config_file:
    configuration = json.load(config_file)

with open("environment.json", "r") as env_file:
    environment = json.load(env_file)

current_environment = configuration["environment"]

apiKey = environment[current_environment]["accounts"]["sharedAccount"]["apiKey"]

authenticatorManager = {
        "apiKey":{
            "headers" : {
                "Authorization" : apiKey.value,
                "Content-Type" : "application/json"
            }
        },
        "bearer":{
            "headers" : {
                "Authorization" : f"bearer {apiKey.value}",
                "Content-Type" : "application/json"
            }
        },
        "invalidApiKey":{
            "headers" : {
                "Authorization" : "invalid-api-key",
                "Content-Type" : "application/json"
        }
    }
}