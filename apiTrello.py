import requests
import json

# Dados de acesso para API Trello
url_trello = "https://api.trello.com/1"
api_key_trello = "INSIRA SUA CHAVE DA API"
token_trello = "INSIRA SEU TOKEN"
headers_trello = {'content-type': 'application/json',"Accept": "application/json"}

def boards_trello():
    """
    ==> Função para buscar os quadros no Trello via API
    :return: Retorna um array com os quadros no Trello
    """
    url = 'https://api.trello.com/1/members/me/boards'
    parametros = {
        'key': api_key_trello,
        'token': token_trello,
        'fields': 'name,url',
                  }
    response = requests.get(url, headers=headers_trello,params=parametros)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro de integração: {response.status_code}')

def list_trello(board_id):
    """
    ==> Função para buscar as listas de um quadro especifico do Trello via API
    :param board_id: ID do quadro no Trello
    :return: Retorna um array com as listas do quadro
    """
    url = f'{url_trello}/boards/{board_id}/lists'
    parametros = {
        'key': api_key_trello,
        'token': token_trello,
        'fields': 'name'
    }
    response = requests.get(url, headers=headers_trello,params=parametros)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro de integração do board {board_id}: {response.status_code}')

def cards_trello(list_id):
    """
    ==> Função para buscar as tarefas de uma lista especifica do Trello via API
    :param list_id: ID da lista no Trello
    :return: Retorna um array com as tarefas da lista
    """
    url = f'{url_trello}/lists/{list_id}/cards'
    parametros = {
        'key': api_key_trello,
        'token': token_trello,
        'fields': 'name,desc,due'
    }
    response = requests.get(url, headers=headers_trello,params=parametros)
    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro de integração do board {list_id}: {response.status_code}')




