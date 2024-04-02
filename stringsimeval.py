import Levenshtein
from simeval import SimEval

class StringSimEval(SimEval):
    def __init__(self):
        super().__init__()

    def eval(self, s1, s2):
        if len(s1) == 0 and len(s2) == 0:
            return 1
        max_len = max(len(s1), len(s2))
        distance = Levenshtein.distance(s1, s2)
        normalized_distance = 1 - distance / max_len
        return normalized_distance
