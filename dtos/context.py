from .balance import Balance
from .score import Score

class Context():
    def __init__(self, request, base_score):
        self.request = request
        self.base_score = base_score
        self.auto = Balance(base_score)
        self.disability = Balance(base_score)
        self.home = Balance(base_score)
        self.life = Balance(base_score)
        self.response = Score()

    