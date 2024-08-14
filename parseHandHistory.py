#text to the right of hand result has the amount gained
#all text next to position except followed by "in chips" is a bet
import os
import re


import ignitionParser
from poker_stuff import Hand, Session
from charts import plotWinRate
import stats

def parseHands(directory):


    hands = [] #This should be a list of hand objects

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        sess = Session()
        with open(file_path, 'r') as file:
            ignitionParser.ZoomParser(file, hands, sess)
    print(f"Total of {len(hands)} hands played")
    return hands



if __name__ == "__main__":
   directory = "handhistory"
    # directory = "test_handhistory"
    # directory = "example_handhistory"
    # directory = "test1"
   hands = parseHands(directory)
   stats.calcWinrateper100bb(hands)
   profitList, SDprofitList, noSDprofitList, bbprofitList = stats.handStats(hands)
   plotWinRate(profitList, SDprofitList, noSDprofitList)