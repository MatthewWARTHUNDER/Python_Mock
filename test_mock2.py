import requests

# Função que uma chama a uma API (apenas exemplo)
def obter_dados_da_api(url):
    resposta = requests.get(url)
    return resposta.json()

# Teste sem fazer a chamada real da API
def test_obter_dados_da_api(mocker):
    #Mocando a resposta da função request.get
    mock_response = mocker.patch('requests.get')

# Definindo um retorno fictício para o mock
    mock_response.return_value.json.return_value = {"id": 1, "nome": "teste"}

# Testando a função com o mock
    resultado = obter_dados_da_api("http://api.exemplo.com/dados")

# Verificando se o resultado é o esperado

    assert resultado == {"id": 1, "nome": "teste"}