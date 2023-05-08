import requests

class Random_quotes() :

    def __init__(self) :
        """
        Initializes the api url of animechan which generates anime quotes
        arguments: None
        return: API text
        """
        self.url = f'https://animechan.vercel.app/api/random'
    
    def get(self) :
        """
        calls for the text from animechan api
        arguments: None
        return: API text
        """
        r = requests.get(self.url)
        self.quote = r.json()
        return self.quote

    def __str__(self) :
        """
        returns the text given by animechan api in str
        arguments: None
        return: API text
        """
        self.quote = Random_quotes().get()
        return self.quote

    
