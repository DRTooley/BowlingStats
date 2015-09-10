
import sqlite3
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.dates as mpl_dates
import numpy

class BowlingEntry():
    def __init__(self, entry_data):
        self.DateBowled = entry_data[0]
        self.Score = entry_data[1]
        self.League = entry_data[2]

def dated_dict_to_graph(my_dict):
    dates = sorted([datetime.datetime.strptime(key, "%Y-%m-%d") for key in my_dict.keys()])
    y = [my_dict[key.strftime("%Y-%m-%d").replace('-0', '-')] for key in dates]
    graph_dates = mpl_dates.date2num(dates)
    fig, ax = pyplot.subplots()
    years = mpl_dates.YearLocator()   # every year
    months = mpl_dates.MonthLocator()  # every month
    yearsFmt = mpl_dates.DateFormatter('%Y')
    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.autoscale_view()
    pyplot.plot(graph_dates, y)



def calculate_longest_hot_streak(bowling_information, hot_number=200):
    longest_streak = 0
    current_streak = 0
    tmp_start = datetime.datetime.now()
    streak_start = datetime.datetime.now()
    streak_end = datetime.datetime.now()
    for entry in bowling_information:
        if current_streak == 0:
            tmp_start = datetime.datetime.strptime(entry.DateBowled, "%Y-%m-%d")
        if entry.Score >= hot_number:
            current_streak += 1
        elif current_streak > longest_streak:
            streak_start = tmp_start
            streak_end = datetime.datetime.strptime(entry.DateBowled, "%Y-%m-%d")
            longest_streak = current_streak
            current_streak = 0
        else:
            current_streak = 0

    print("Your longest " + str(hot_number) + "+ streak is " + str(longest_streak) + " games!")
    print("Starting on " + streak_start.strftime('%m/%d/%Y') + " and ending on " + streak_end.strftime('%m/%d/%Y'))
    print('')


def find_high_score(bowling_information):
    return max([entry.Score for entry in bowling_information])


def graph_yearly_high_scores(bowling_information):
    yearly_scores = {}

    for entry in bowling_information:
        year = entry.DateBowled[0:4]
        if year in yearly_scores:
            if entry.Score > yearly_scores[year]:
                yearly_scores[year] = entry.Score
        else:
            yearly_scores[year] = entry.Score

    yrs = sorted(list(yearly_scores.keys()))
    y = [yearly_scores[yrs[i]] for i in range(len(yrs))]

    graph_yrs = [datetime.datetime.strptime(single_yr, "%Y") for single_yr in yrs]
    graph_dates = mpl_dates.date2num(graph_yrs)
    fig, ax = pyplot.subplots()
    years = mpl_dates.YearLocator()   # every year
    months = mpl_dates.MonthLocator()  # every month
    yearsFmt = mpl_dates.DateFormatter('%Y')
    # format the ticks
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(yearsFmt)
    ax.xaxis.set_minor_locator(months)
    ax.autoscale_view()
    pyplot.plot(graph_dates, y)

def multiple_game_average(bowling_information, number_of_games=12):
    x_game_average = {}
    past_games = []
    for entry in bowling_information:
        if len(past_games) >= number_of_games:
            past_games.pop(0)
        past_games.append(entry.Score)
        if len(past_games) == number_of_games:
            x_game_average[entry.DateBowled] = numpy.mean(past_games)

    dated_dict_to_graph(x_game_average)










if __name__ == "__main__":
    dbcon = sqlite3.connect("BowlingDatabase.db")
    cursor = dbcon.cursor()
    cursor.execute("SELECT * FROM stats")
    bowling_information = [BowlingEntry(row) for row in cursor]

    calculate_longest_hot_streak(bowling_information)
    graph_yearly_high_scores(bowling_information)
    multiple_game_average(bowling_information)
    multiple_game_average(bowling_information, 32)
    pyplot.show()


    dbcon.close()
