from bs4.element import SoupStrainer
import requests
from bs4 import BeautifulSoup
import os

from requests.models import Response



class Lyrics: 
    def __init__ (self):
        self.nameofsong = str(input("NameOfSong: ")).lower().replace(" ","")
        self.nameofsinger= str(input("NameOfSinger: ")).lower().replace(" ","")
        
        
    def request(self):
        urlofwebsite = "https://www.azlyrics.com/lyrics/" 
        slash = "/"
        extension = ".html"
        fullurl = urlofwebsite+str(self.nameofsinger)+slash+str(self.nameofsong)+extension
        #print (fullurl)
        sendrequest = requests.get(fullurl)
        self.response = sendrequest.content

    def grablyrics(self): 
        soup = BeautifulSoup(self.response,'html.parser')
        theelementwewanttoscrape = "body > div.container.main-page > div > div.col-xs-12.col-lg-8.text-center > div:nth-child(8)" 
        divlyrics = soup.select_one(theelementwewanttoscrape).text
        self.Lyricsofthesong = divlyrics.lstrip()
        print (self.Lyricsofthesong)

    def savelyrics (self):
        if os.path.isdir('Lyrics'):  
            os.chdir ('Lyrics')
        else :
            os.system ('mkdir Lyrics')
            os.chdir ('Lyrics')
        
        nameofdirectoryofsinger = self.nameofsinger.upper()
        if os.path.isdir(nameofdirectoryofsinger):
            os.chdir (nameofdirectoryofsinger)
        else:
            os.mkdir (self.nameofsinger.upper())
            os.chdir (nameofdirectoryofsinger)


        nameofsongtext = self.nameofsong+".txt"
        with open (nameofsongtext,"a") as file :
            file.writelines(self.Lyricsofthesong)



    

    


data = Lyrics()
data.request()
data.grablyrics()
data.savelyrics()


