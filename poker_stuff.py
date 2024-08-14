class Hand:
    def __init__(self):
        self.pos: str = ""
        self.bb_stakes: float = 0
        self.profit_from_hand: float = 0
        self.rake: float = 0
        self.handNumber: int = 0
        self.pfr: bool = False
        self.VPip: bool = False
        self.heroHand: str = ""
        self.villian_hand: str = ""
        self.startingChips = 0
        self.showdown = True
    
    def startHandAction(self):
        self.handaction: HandAction = HandAction(self.bb_stakes)
    

class HandAction:
    def __init__(self, bb_stakes):
        self.bb_stakes: float = bb_stakes
        self.preflop: str = ""
        self.flop: str = ""
        self.turn: str = ""
        self.river: str = ""
        self.profit_from_hand: float = 0


class Session:
    def __init__(self):
        self.sessionHands: list[Hand] = []
        self.date: str = ""
        self.sessionProfit: float = 0
        self.bb_stakes: float = 0