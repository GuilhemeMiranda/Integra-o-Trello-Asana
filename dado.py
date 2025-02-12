import requests
import json
import datetime
from apiAsana import *
from apiTrello import *
from dateutil import parser

def main():
    # 1 - Obter quadros do Trello
    boards = boards_trello()
    for board in boards:
        print(f'Processando o board {board['name']}')

        # 2 - Criando o projeto no Asana
        project = project_asana(board['name'],board['url'])
        print(f'Criado o projeto {project['data']['name']} com sucesso!')

        # 3 - Obter lista do quadro no Trello
        lists = list_trello(board['id'])
        for list in lists:
            print(f'Processando lista {list["name"]}')

            # 4 - Criar seção no Asana
            section = section_asana(project['data']['gid'],list['name'])
            print(f'Seção criada {section['data']['name']} com sucesso!')

            # 5 - Obter cards da lista no Trello
            cards = cards_trello(list['id'])
            for card in cards:
                print(f'Processando card {card["name"]}')

            # 6 - Criar tarefa no Asana
                data_trello = card.get("due") # buscar no card a data de vencimento
                if data_trello:
                    data_atualizada = parser.isoparse(data_trello) #Como o Trello devolve a data em um padrão podemos converter a str em datetime
                    data_atualizada = data_atualizada.strftime('%Y-%m-%d') #Convertendo na str padrão do Asana
                else:
                    data_atualizada = None # Se não havia data no trello não haverá no Asana
                task = task_asana(project['data']['gid'],section['data']['gid'],card['name'],card['desc'],data_atualizada)


if __name__ == '__main__':
    main()

