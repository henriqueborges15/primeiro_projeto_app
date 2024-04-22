import requests
import json

url = "https://raw.githubusercontent.com/henriqueborges15/test_app_info/main/lojas.json"
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    # print(dados_json)
    dados_loja = {}
    for item in dados_json:
        nome_loja = item["Company"]
        if nome_loja not in dados_loja:
            dados_loja[nome_loja] = [] 

        dados_loja[nome_loja].append({
            "item" : item["Item"],
            "price" : item["price"],
            "description" : item["description"]            
         })


else:
    print(f"O erro foi: {response.status_code}")


for nome_loja, dados in dados_loja.items():
    nome_arquivo = f"{nome_loja}.json"
    with open(nome_arquivo, "w") as arquivo_loja:
        json.dump(dados, arquivo_loja, indent=4)


print(dados_loja["Amazon"])


