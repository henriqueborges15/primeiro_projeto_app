from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get("/api/hello")
def ola_mundo():
    """
    endpoint para testar o codigo

    """


    return {"Olá, Mundo! "}

@app.get("/api/lojas/")
def get_lojas(loja : str = Query(None)):

    """
    
    endpoint para ver o catalogo das lojas
    
    """
    url = "https://raw.githubusercontent.com/henriqueborges15/test_app_info/main/lojas.json"
    response = requests.get(url)

    if response.status_code == 200:
        dados_json = response.json()
        if loja is None:
            return {"Dados" :dados_json}

        dados_loja = []
        for item in dados_json:
            if item["Company"] == loja:
                dados_loja.append({
                "item" : item["Item"],
                "price" : item["price"],
                "description" : item["description"]            
            })
        return {"Loja" :loja, "Catalogo" :dados_loja}

    else:
        return {"Erro": f"Ocorreu um erro ao obter os dados das lojas. Código de status: {response.status_code} - {response.text}"}