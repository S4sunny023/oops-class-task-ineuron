import logging
import logging as lg
lg.basicConfig(filename="PPP.log",level=logging.DEBUG,format=("%(levelname)s %(asctime)s %(message)s"))
class Youtube:
    logging.info("youtube class is being created")
    def __init__(self,yt_channal,yt_name,salary,views,comments,subscribers):
        self.yt_channal = yt_channal
        self._salary = salary
        self.__views = views
        self.comment = comments
        self.subscriber = subscribers

    def __str__(self):
        try:
            logging.info("will return channal name")
            return self.yt_channal
        except Exception as e:
            logging.error(e)

        def rating(self, subscriber):
            try:
                logging.info("will return channal name")
                return self.yt_channal
            except Exception as e:
                logging.error(e)
candidate1 = Youtube("INEURON","SUDHANSHU SIR",500000,"206M","256K",250550)

#to call private variable : object._varName:

print(candidate1._salary)

#to call private variable : object._className__varName:

print(candidate1._Youtube__views)

class Entertainment(Youtube):
    __address = " "
    _trending = 0
    def __init__(self):
        self.__address = "Youtube India Mumbai"
        self._trending = "indian entertainment  of youtubers are trending worldwide"

    def ranking(self):
        return self.subscriber










