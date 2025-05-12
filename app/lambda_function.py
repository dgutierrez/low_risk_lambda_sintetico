import json
import requests



def lambda_handler(event, context):
    print('iniciando lambda de teste sintetico')

    url = "http://calculadora-applb-1367425583.us-east-1.elb.amazonaws.com:5020/api/Calculadora/Somar"
    params = {
        "a": 10,
        "b": 9
    }
    headers = {
        "x-simulation": "true"
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        resultado = response.status_code
        print('status code = ' + str(resultado))
        print(data)
        return {
            "statusCode": response.status_code,
            "body": json.dumps(data)
        }
    except requests.exceptions.RequestException as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }

