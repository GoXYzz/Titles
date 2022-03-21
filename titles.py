from bs4 import BeautifulSoup
import requests
from gtts import gTTS
from playsound import playsound
  
class Titles:
    """ The goal is to get specific category titles from www.naslovi.net and make their speech able """
    # Category topic: politika, ekonomija, svet, balkan, drustvo, hronika,  kultura, 
    # sport, regioni, vojvodina, slobodno, tehnologija, auto, putovanja.
    # Accent language for speaking: https://developers.google.com/admin-sdk/directory/v1/languages
    def __init__(self, category, accent):
        self.category = category
        self.accent = accent

    # Function for scraping specified category
    def scrape(self):
        # Getting category from a web location
        web_location = requests.get('https://naslovi.net/' + self.category)
        soup = BeautifulSoup(web_location.text, features='lxml')
        # Finding specific div
        result = soup.find_all('div', {'class':'article'})
        # list text of titles
        lista = []
        # Getting the text of titles and adding them to lista[]
        for item in result:
            for element in item.find_all('h2', {'class':'a-title'}):
                lista.append(element.text)

        # Separate elements with "." to make sentences
        final_text = '. '.join([str(item) for item in lista])
        print (final_text)
        # Create .mp3 file to store speech
        audio = 'speech.mp3'
        # Storing speech with accent
        sp = gTTS(text= final_text, lang=self.accent)
        sp.save(audio)
        # Speak
        playsound(audio)    


