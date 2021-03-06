from CyberSource import *
import os
import json
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()

# To delete None values in Input Request Json body
def del_none(d):
    for key, value in list(d.items()):
        if value is None:
            del d[key]
        elif isinstance(value, dict):
            del_none(value)
    return d

def generate_key():
    encryptionType = "None"
    targetOrigin = "https://www.test.com"
    requestObj = GeneratePublicKeyRequest(
        encryption_type = encryptionType,
        target_origin = targetOrigin
    )


    requestObj = del_none(requestObj.__dict__)
    requestObj = json.dumps(requestObj)

    format = "legacy"

    try:
        config_obj = configuration.Configuration()
        client_config = config_obj.get_configuration()
        api_instance = KeyGenerationApi(client_config)
        return_data, status, body = api_instance.generate_public_key(format, requestObj)

        print("\nAPI RESPONSE CODE : ", status)
        print("\nAPI RESPONSE BODY : ", body)

        return return_data
    except Exception as e:
        print("\nException when calling KeyGenerationApi->generate_public_key: %s\n" % e)

if __name__ == "__main__":
    generate_key()
