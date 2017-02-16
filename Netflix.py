#!/usr/bin/env python3

# -------
# imports
# -------
import math
from math import sqrt
import pickle
from requests import get
from os import path
from numpy import sqrt, square, mean, subtract


def create_cache(filename):
    """
    filename is the name of the cache file to load
    returns a dictionary after loading the file or pulling the file from the public_html page
    """
    cache = {}
    filePath = "/u/fares/public_html/netflix-caches/" + filename

    if path.isfile(filePath):
        with open(filePath, "rb") as f:
            cache = pickle.load(f)
    else:
        webAddress = "http://www.cs.utexas.edu/users/fares/netflix-caches/" + \
            filename
        bytes = get(webAddress).content
        cache = pickle.loads(bytes)

    return cache


AVERAGE_RATING = 3.60428996442
ACTUAL_CUSTOMER_RATING = create_cache(
    "cache-actualCustomerRating.pickle")
AVERAGE_MOVIE_RATING_PER_YEAR = create_cache(
    "cache-movieAverageByYear.pickle")
YEAR_OF_RATING = create_cache("cache-yearCustomerRatedMovie.pickle")
CUSTOMER_AVERAGE_RATING_YEARLY = create_cache(
    "cache-customerAverageRatingByYear.pickle")
AVERAGE_MOVIE_RATING = create_cache(
    "cache-averageMovieRating.pickle")
CUSTOMER_AVERAGE_RATING = create_cache(
    "cache-averageCustomerRating.pickle")
# for key in ACTUAL_CUSTOMER_RATING:
#     print(key)
# #     print(ACTUAL_CUSTOMER_RATING[key])
#print(ACTUAL_CUSTOMER_RATING[])

#print(ACTUAL_CUSTOMER_RATING[1048489])
# print(ACTUAL_CUSTOMER_RATING[2097068])
# print(ACTUAL_CUSTOMER_RATING[418991])


# for key in AVERAGE_MOVIE_RATING_PER_YEAR:
#     print(key)
#     #print(AVERAGE_MOVIE_RATING_PER_YEAR[key])
    
# for key in AVERAGE_MOVIE_RATING:
#     print(key)
#     print(AVERAGE_MOVIE_RATING[key])

# for key in CUSTOMER_AVERAGE_RATING:
#     print(key)
    #print(CUSTOMER_AVERAGE_RATING[key])





# actual_scores_cache ={10040: {2417853: 1, 1207062: 2, 2487973: 3}, 10030: {1234567: 1, 7654321: 1, 1111111: 1},10050: {2417850: 2, 1207060: 2, 2487970: 2}}
# movie_year_cache = {10040: 1990, 10030: 2000, 10050: 2010}
# decade_avg_cache = {1990: 2.4, 2000: 1, 2010: 2}

# ------------
# netflix_eval
# ------------


def netflix_eval(reader, writer) :
    predictions = []
    actual = []
    customer_avg = []
    movie_avg = 0
    # iterate throught the file reader line by line
    for line in reader:
    # need to get rid of the '\n' by the end of the line
        line = line.strip()
        # check if the line ends with a ":", i.e., it's a movie title 
        if line[-1] == ':':
		# It's a movie
            current_movie = line.rstrip(':')
            movie_avg = AVERAGE_MOVIE_RATING[int(current_movie)]
            # pred = 
            # pred = (pred // 10) *10
            # prediction = decade_avg_cache[pred] #prediction place -> where we code           
            writer.write(line)
            writer.write('\n')
        else:
		# It's a customer
            current_customer = line
            customer_avg.append(CUSTOMER_AVERAGE_RATING[int(current_customer)])
            prediction = (movie_avg + CUSTOMER_AVERAGE_RATING[int(current_customer)]) / 2
            predictions.append(prediction)
            actual.append(ACTUAL_CUSTOMER_RATING[(int(current_customer), int(current_movie))])
            writer.write(str(prediction)) 
            writer.write('\n')	
    # calculate rmse for predications and actuals
    rmse = sqrt(mean(square(subtract(predictions, actual))))
    print (sqrt(mean(square(subtract(predictions, actual)))))
    writer.write(str(rmse)[:4] + '\n')

#def netflix_pred(, cache): #avgMY
