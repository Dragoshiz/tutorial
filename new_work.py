# Write a program which downloads some movie data from a given url and saves it to a "result.json" file for later re-use. 
# Prerequisite: 
# - Watch some introductory video about the python request library, you can find some in youtube
# - After having a sense of what it does read the requests "get" method documentation from the official requests documentation (https://2.python-requests.org/en/master/), the "get" method is what you need for this excersise.
# - Research the python json module, watch some videos, read articles etc...
# - Look into how to write data (and json) to files using python
# Steps:
# - the url is https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json save this to a variable as string in a main function
# - write another function which takes a url as parameter and downloads the data from the given url using the requests.get method. Use return to return the data to the main function
# - call the previous functions with your variable holding the url to the data
# - write another function which takes a data and a filepath argument and writes the data to the given filepath   
# - create a filename variable in the main function (like filename = 'results.json' and call your previous function with this filepath and the downloaded data
# FINAL: you should see a the a file containing the data you've downloaded from the website next to your python file
import requests
url = "https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json"
r = requests.get('https://raw.githubusercontent.com/prust/wikipedia-movie-data/master/movies.json')
print(type(r))