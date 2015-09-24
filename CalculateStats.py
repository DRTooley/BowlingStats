
import sqlite3
import datetime
import matplotlib.pyplot as pyplot
import matplotlib.dates as mpl_dates
import numpy


def dated_dict_to_graph(my_dict):
    dates = sorted([key for key in my_dict.keys()])
    y = [my_dict[key] for key in dates]
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

def distribution(information_list):
    for key, value in information_list.items():
        print(key, ' : ', value)

    information_list.pop(0, None)

    fig, ax = pyplot.subplots()
    index = numpy.arange(len(information_list.keys()))
    bar_width = 0.35
    opacity = 0.4
    pyplot.xlabel('Streak')
    pyplot.ylabel('Amount')
    pyplot.title('Occurances of Streak Lengths')
    pyplot.xticks(index + bar_width, list(information_list.keys()))
    mylist = [information_list[key] for key in information_list.keys()]
    rects2 = pyplot.bar(index + bar_width, mylist, bar_width)

def calculate_longest_hot_streak(bowling_information, hot_number=200):
    bowling_information.sort()
    distro_information = {}
    longest_streak = 0
    current_streak = 0
    tmp_start = datetime.datetime.now()
    streak_start = datetime.datetime.now()
    streak_end = datetime.datetime.now()
    for entry in bowling_information:
        if current_streak == 0:
            tmp_start = entry.DateBowled
        if entry.Score >= hot_number:
            current_streak += 1
        elif current_streak >= longest_streak:
            streak_start = tmp_start
            streak_end = entry.DateBowled
            longest_streak = current_streak
            distro_information[current_streak] = distro_information.get(current_streak, 0) + 1
            current_streak = 0

        else:
            distro_information[current_streak] = distro_information.get(current_streak, 0) + 1
            current_streak = 0

    distro_information.pop(0)
    distro_information.pop(1)
    distribution(distro_information)
    print("Your current " + str(hot_number) + "+ streak is " + str(current_streak) + " games!")
    print("Starting on " + tmp_start.strftime('%m/%d/%Y') + " and ending on " + bowling_information[-1].DateBowled.strftime('%m/%d/%Y'))
    print('')

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






