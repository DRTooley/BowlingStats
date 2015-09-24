__author__ = 'david'
import datetime


class BowlingEntry():
    def __init__(self, entry_data):
        self.DateBowled = datetime.datetime.strptime(entry_data[0], "%Y-%m-%d")
        self.Score = entry_data[1]
        self.GameNumber = entry_data[2]
        self.League = entry_data[3]

    def print(self):
        print(self.DateBowled, ' ', self.GameNumber, ' ',self.Score)

    def __le__(self, entry):
        if self.DateBowled == entry.DateBowled:
            return self.GameNumber <= entry.GameNumber
        return self.DateBowled <= entry.DateBowled

    def __ge__(self, entry):
        if self.DateBowled == entry.DateBowled:
            return self.GameNumber >= entry.GameNumber
        return self.DateBowled >= entry.DateBowled


    def __lt__(self, entry):
        if self.DateBowled == entry.DateBowled:
            return self.GameNumber < entry.GameNumber
        return self.DateBowled < entry.DateBowled

    def __gt__(self, entry):
        if self.DateBowled == entry.DateBowled:
            return self.GameNumber > entry.GameNumber
        return self.DateBowled > entry.DateBowled

    def __eq__(self, entry):
        return self.DateBowled == entry.DateBowled and self.GameNumber == entry.GameNumber and self.Score == entry.Score