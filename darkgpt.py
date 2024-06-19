import requests

base_url = 'http://62.72.6.182:1717'
dark = f'{base_url}/darkgpt'
darkbase = f'{base_url}/test_route'

json_data = {
    'task': "generator",
    'program': "python",
    "prompt": "he'll world",
    "code": None,
    'further_description1': 'none',
    'further_description2': 'none'
}

headers = {
    'X-API-KEY': 'pUC3BEfonGJU5ivGb7FMAr189oVH73rj7m9Its1eg09cDSLMCZAJH-XSSDKPPEsklOc'
}

try:
    response = requests.post(dark, json=json_data, headers=headers)
    response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
    print(response.text)
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
