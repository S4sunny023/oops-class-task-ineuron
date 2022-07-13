import logging
import logging as lg
lg.basicConfig(filename="POLY.log",level=logging.DEBUG,format=("%(levelname)s %(asctime)s %(message)s"))

class YouTube:
    motto = "we are youtubers"
    def __init__(self, name , channal,views, comment,category):
        logging.info("constructer of Parent Class")
        self.name = name
        self.channal = channal
        self.views = views
        self.comment = comment
        self.category = category
        self.special_yt = "this is a instance variable from class Youtube "

    def Yt_CATEGORY(self):
        try:
            logging.info("will return category")
            return self.category
        except Exception as e:
            logging.error(e)

    def yt_details(self):
        try:
            return self.name, self.channal, self.views,self.comment
        except Exception as e:
            logging.error(e)

class Music(YouTube):

    def __init__(self, name,channal,type_music):
        logging.info("constructer of child class is formed")
        logging.info("super is being used to overweite function of child class in parent class")
        self.name = name
        self.channal = channal
        self.type_music = type_music
        self.music_theme = "WORK MODE -no time to waste"

    def __str__(self):
        try:
            logging.info("will return itself from music class ")
            return "this is a youtuber from music channal"
        except Exception as e:
            logging.error(e)

    def yt_details(self):
        try:
            logging.info("will return details of the person")
            return self.name , self.channal, self.type_music
        except Exception as e:
            logging.error(e)


person1 = YouTube("sunny","xyz","255K","55K","trance")
person2 = Music("rohan","abc","english pop")

#both parent and child class have the method yt_details, but when called firstly the method from child class is being used
print(person1.yt_details())
print(person2.yt_details())
#print(person2.special_yt)-  will throw error because in music class new constructer is formrd so it will not inherit the functions of parent class to avoid this , we will use "super"  command to access the parent class functions



class Vlog(Music):
    motto = "we are Youtubers from vlogging channel"
    def __init__(self,name ,channal,type_music, salary,videos):
        super().__init__(name,channal,type_music)
        self.name = name
        self.channal = channal
        self.type_music = type_music
        self._salary = salary
        self.__videos = videos



    def __str__(self):
        try:
            logging.info("will return itself")
            return f"{self.name}this is a youtuber from vlogging channal"
        except Exception as e:
            logging.error(e)

person3 = Vlog("SUDHANSHU","EDUCATIONAL_VLOGS","ROCK","95K",555)
print(person3.music_theme) # we can access the parent class method easily by Super method
print(person3._salary)
print(person3._Vlog__videos)

