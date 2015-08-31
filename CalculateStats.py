import sqlite3
import datetime
if __name__ == "__main__":
    dbcon = sqlite3.connect("BowlingDatabase.db")
    cursor = dbcon.cursor()


    
    cursor.execute("SELECT * FROM stats")
    BowlingInformation = [row for row in cursor]
    longestStreak = 0
    currentStreak = 0
    tmpStart = datetime.datetime.now()
    streakStart = datetime.datetime.now()
    streakEnd = datetime.datetime.now()
    for score in BowlingInformation:
        if currentStreak == 0:
            tmpStart = datetime.datetime.strptime(score[0], "%Y-%m-%d")
        if score[1] >= 200:
            currentStreak += 1
        elif currentStreak > longestStreak:
            streakStart = tmpStart
            streakEnd = datetime.datetime.strptime(score[0], "%Y-%m-%d")
            longestStreak = currentStreak
            currentStreak = 0
        else:
            currentStreak = 0

    print("Your longest 200 Streak is " + str(longestStreak) + " games!")
    print("Starting on " + streakStart.strftime('%m/%d/%Y') + " and ending on " + streakEnd.strftime('%m/%d/%Y'))



    dbcon.close()
