from helpers import *

# read file downloaded from Census website
filename = 'data.csv'
with open(filename) as f:
    d = f.readlines()

# calculate number of counties described in a file
header = d[0].split(',')
number_of_counties = 0
for el in header:
    if el.find('County') > -1:
        number_of_counties +=1
number_of_counties //= 2

lines = []
for i in range(2, (4 * number_of_counties - 1), 4):
    tmp_lst = d[0].split(',')
    state = tmp_lst[i + 1].rstrip('"').lstrip(' ')
    abbrev = state_abbreviations[state]
    print(tmp_lst[i].lstrip('"').rstrip('County') + abbrev)
