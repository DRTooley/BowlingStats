import sqlite3
import csv

if __name__ == '__main__':
	dbconnect = sqlite3.connect("BowlingDatabase.db")
	cursor = dbconnect.cursor()
	cursor.execute("DROP TABLE stats")
	cursor.execute("CREATE TABLE stats(DateBowled Date, Score INT, GameNumber INT, League TEXT)")


	
	with open('BowlingScores.csv') as scoresFile:
		linereader = csv.reader(scoresFile)
		for row in linereader:
			date = row[0]
			parts = date.split('/')
			if len(parts) == 3:	
				modifiedDate = parts[2]+'-'+parts[0]+'-'+parts[1]
				scoreOne = int(row[1])
				scoreTwo = int(row[2])
				scoreThree = int(row[3])
				league = row[4]	
				cursor.execute("INSERT INTO stats values(?, ?, ?, ?)", (modifiedDate, scoreOne, 1,league))
				cursor.execute("INSERT INTO stats values(?, ?, ?, ?)", (modifiedDate, scoreTwo, 2,league))
				cursor.execute("INSERT INTO stats values(?, ?, ?, ?)", (modifiedDate, scoreThree, 3,league))

	dbconnect.commit()

	cursor.execute("SELECT * FROM stats")
	for row in cursor:
		print(row[0], row[1], row[2])
	dbconnect.close()

