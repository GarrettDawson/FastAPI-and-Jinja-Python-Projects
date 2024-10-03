import requests

class CatApi:
    def __init__(self) -> None:
        self.base_url = 'https://cat-fact.herokuapp.com' 

    def get_facts(self):
        endpoint = self.base_url + '/facts'
        return requests.get(endpoint).json()
    

if  __name__ == '__main__':
    c = CatApi()
    print(c.get_facts())
