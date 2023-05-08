import requests

class Random_facts() :
    
    def __init__(self) :
        """
        Initializes the api url of uselessfacts
        arguments: None
        return: API text
        """
        self.url = f'https://uselessfacts.jsph.pl/api/v2/facts/random'
    
    def get(self) :
        """
        calls for the text given by the api
        arguments: None
        return: API text
        """
        r = requests.get(self.url)
        self.fact = r.json()
        return self.fact

    def __str__(self) :
        """
        returns the text given by the api in str
        arguments: None
        return: API text
        """
        self.fact = Random_facts().get()
        return self.fact