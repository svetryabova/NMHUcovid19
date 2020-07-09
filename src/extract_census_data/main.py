from helpers import *

output_filename = 'D:/Projects/usa_county_dataset.csv'

# read file downloaded from Census website
input_filename = 'data.csv'
with open(input_filename) as f:
    d = f.readlines()

# calculate number of counties described in a file
header = d[0].split(',')
number_of_counties = 0
for el in header:
    if el.find('County') > -1:
        number_of_counties +=1
number_of_counties //= 2

counties = []
for i in range(2, (4 * number_of_counties - 1), 4):
    tmp_lst = d[0].split(',')
    state = tmp_lst[i + 1].rstrip('"').lstrip(' ')
    abbrev = state_abbreviations[state]
    counties.append(tmp_lst[i].lstrip('"').rstrip('County') + abbrev)

# features we want to use
feature_numbers = [1, 27, 7, 30, 31, 35, 45, 47, 60]
# delete commas
comma_ind = [1, 45]
# convert from percent to fraction:
# 7 - persons 65 and over
# 30 - computer
# 31 - Internet
# 35 - insurance
# 47 - poverty
percent_ind = [7, 30, 31, 35, 47]
# remove dollar signs
money_amount_ind = [45]

county_ind = 0
for i in range(4, (4 * number_of_counties + 1), 4):
    s = counties[county_ind] + ','
    for ind in feature_numbers:
        f = d[ind].split()[-1].split('"')[i]
        if ind in comma_ind:
            # remove comma from string
            f = f.replace(',', '')
        elif ind in percent_ind:
            # remove % character and convert to fraction representation
            f = f.replace('%', '')
            f = round((float(f) / 100) * 1000) / 1000
            f = str(f)
        if ind in money_amount_ind:
            # remove dollar sign
            f = f.replace('$', '')
        s += f + ','
    s = s.rstrip(',')
    s += '\n'
    counties[county_ind] = s
    county_ind += 1

print(counties)

with open(output_filename, 'a') as f:
    f.writelines(counties)
