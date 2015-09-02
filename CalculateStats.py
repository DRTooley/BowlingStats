import sqlite3
import datetime

import matplotlib.pyplot as pyplot

class BowlingEntry():
    def __init__(self, EntryData):
        self.DateBowled = EntryData[0]
        self.Score = EntryData[1]
        self.League = EntryData[2]

def CalculateLongestHotStreak(BowlingInformation, HotNumber=200):
    longestStreak = 0
    currentStreak = 0
    tmpStart = datetime.datetime.now()
    streakStart = datetime.datetime.now()
    streakEnd = datetime.datetime.now()
    for entry in BowlingInformation:
        if currentStreak == 0:
            tmpStart = datetime.datetime.strptime(entry.DateBowled, "%Y-%m-%d")
        if entry.Score >= HotNumber:
            currentStreak += 1
        elif currentStreak > longestStreak:
            streakStart = tmpStart
            streakEnd = datetime.datetime.strptime(entry.DateBowled, "%Y-%m-%d")
            longestStreak = currentStreak
            currentStreak = 0
        else:
            currentStreak = 0

    print("Your longest "+ str(HotNumber) +"+ streak is " + str(longestStreak) + " games!")
    print("Starting on " + streakStart.strftime('%m/%d/%Y') + " and ending on " + streakEnd.strftime('%m/%d/%Y'))
    print('')

def GraphYearlyHighScores(BowlingInformation):
    pass

if __name__ == "__main__":
    dbcon = sqlite3.connect("BowlingDatabase.db")
    cursor = dbcon.cursor()
    cursor.execute("SELECT * FROM stats")
    BowlingInformation = [BowlingEntry(row) for row in cursor]

    CalculateLongestHotStreak(BowlingInformation)

    GraphYearlyHighScores(BowlingInformation)

    dbcon.close()
