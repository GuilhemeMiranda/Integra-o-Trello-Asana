import requests
import json

#Dados de acesso para API Asana
url_asana = 'https://app.asana.com/api/1.0'
token_asana = 'INSIRA SEU TOKEN'
headers_asana = {
    'Authorization': f'Bearer {token_asana}','content-type': 'application/json','Accept': 'application/json'}

def project_asana(nome,notas):
    """
    ==>Função para criar um projeto no Asana equivalente a um quadro no Trello
    :param nome: Nome do quadro no Trello
    :param notas: Link da url do quadro no Trello
    :return: Retorna um array com os dados do projeto criado
    """
    url = f'{url_asana}/projects'
    payload = {
        "data": {
            "name": nome,
            "color": "dark-pink",
            "notes": notas,
            "default_access_level": "admin",
            "minimum_access_level_for_customization": "admin",
            "minimum_access_level_for_sharing": "admin",
            "workspace": "INSIRA SEU WORKSPACE"
        }
    }
    response = requests.post(url, json=payload, headers=headers_asana)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao criar projeto {nome} no Asana: {response.status_code}")
        print(response.json())

def section_asana(project_id,nome):
    """
    ==> Função para criar a seção dentro de um projeto especifico
    :param project_id: Id do projeto a ser editado
    :param nome: Nome da seção a ser incluida
    :return: Retorna um array com os dados da seção criada
    """
    url = f'{url_asana}/projects/{project_id}/sections'
    payload = {
        'data': {
            "name": nome,
        }
    }
    response = requests.post(url, json=payload, headers=headers_asana)
    if response.status_code == 201:
        return response.json()
    else:
        print(f"Erro ao criar seção {nome} no projeto {project_id}: {response.status_code}")

def task_asana(project_id,section_id, nome, description,data_atualizada):
    """
    ==> Função para incluir uma tarefa dentro de um projeto, informando sua seção especifica.
    :param project_id: Id do projeto a ser editado
    :param section_id: Id da seção especifica da tarefa
    :param nome: Nome da tarefa
    :param description: Observações e Descrição da tarefa
    :param data_atualizada: Data de vencimento da tarefa
    :return: Retorna um array com os dados da tarefa criada
    """
    url = f'{url_asana}/tasks'
    payload = {
        'data': {
            'name': nome,
            'description': description,
            'due_on': data_atualizada,
            'workspace': 'INSIRA SEU WORKSPACE',
            'memberships': [{
                'project': project_id,
                'section': section_id,
            }]
        }
    }
    response = requests.post(url, json=payload, headers=headers_asana)
    if response.status_code == 201:
        print(f'Tarefa {nome} criada com sucesso!')
        return response.json()
    else:
        print(f"Erro ao criar tarefa {nome} na seção {section_id}: {response.status_code} {response.json()}")



