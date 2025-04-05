from itertools import count

#Check for null values in dataset
is_first_line, is_second_line = True, True
row_index = 0
null_ls = []

for row in open("C:\\Users\\ALIENWARE\\Desktop\\archive\\Adult mortality.csv"):
    if is_first_line:
        is_first_line = False
    elif is_second_line:
        is_second_line = False
    else:
        data = row.split(",")  
        for value in data:
            if value == None:
                null_ls.append(row_index)
    row_index += 1

if null_ls != []:
    print("The data in this dataset contains null values.")
else:
    print("There are no null values in th dataset.")

print("")
#Assemble the values in the dataset as a dictionary
is_first_line = True
is_second_line = True
mortality_dict = {}

for row in open("C:\\Users\\ALIENWARE\\Desktop\\archive\\Adult mortality.csv"):
    row_index += 1
    if is_first_line:
        is_first_line = False
    elif is_second_line:
        is_second_line = False
    else:
        data = row.split(",")        
        country, year = (data[0].strip()).strip('"'), int((data[1].strip()).strip('"'))
        bothsex, male, female = int((data[2].strip()).strip('"')), int((data[3].strip()).strip('"')), int((data[4].strip()).strip('"'))
        
        #Check for incorrect values (Eg: -1 for population)
        if year not in range(2000, 2017) or bothsex < 0 or male < 0 or female < 0:
            print("Error data") 

        #Add the data to the dict
        if country not in mortality_dict:
            mortality_dict[country] = [[year, bothsex, male, female]]
        else:
            mortality_dict[country].append([year, bothsex, male, female])


print("")
#Analyze the data (The larger the number in the data, the higher the mortality rate for that data)
#Eg: 100 means "0.1" and 200 means "0.2" (probability of dying between 15 and 60 years per 1000 population)

#Find the average mortality rate for each country by gender (from 2000-2016) (ages 15-60)
both_average_dict = {}
male_average_dict = {}
female_average_dict = {}

for key in mortality_dict:
    both_num, male_num, female_num = 0, 0, 0
    ls_len = len(mortality_dict[key])
    for i in range(ls_len):
        both_num += mortality_dict[key][i][1]
        male_num += mortality_dict[key][i][2]
        female_num += mortality_dict[key][i][3]
    both_average, male_average, female_average = both_num/ls_len, male_num/ls_len, female_num/ls_len
    both_average_dict[key] = format(both_average/1000, '.3f')
    male_average_dict[key] = format(male_average/1000, '.3f')
    female_average_dict[key] = format(female_average/1000, '.3f')


#Find the maximum/minimum average mortality rate for each country by gender (from 2000-2016) (ages 15-60)
max_both, min_both = max(both_average_dict.values()), min(both_average_dict.values())
max_male, min_male = max(male_average_dict.values()), min(male_average_dict.values())
max_female, min_female = max(female_average_dict.values()), min(female_average_dict.values())

for key in both_average_dict:
    if both_average_dict[key] == max_both:
        max_both_country = key
    if both_average_dict[key] == min_both:
        min_both_country = key

    if male_average_dict[key] == max_male:
        max_male_country = key
    if male_average_dict[key] == min_male:
        min_male_country = key    

    if female_average_dict[key] == max_female:
        max_female_country = key
    if female_average_dict[key] == min_female:
        min_female_country = key   

print("Between 2000 and 2016, the highest mortality rate for people aged 15 to 60 was " + str(max_both) + ", occurring in " + max_both_country + ".")
print("Between 2000 and 2016, the lowest mortality rate for people aged 15 to 60 was " + str(min_both) + ", occurring in " + min_both_country + ".")

print("Between 2000 and 2016, the highest mortality rate for male aged 15 to 60 was " + str(max_male) + ", occurring in " + max_male_country + ".")
print("Between 2000 and 2016, the lowest mortality rate for male aged 15 to 60 was " + str(min_male) + ", occurring in " + min_male_country + ".")

print("Between 2000 and 2016, the highest mortality rate for female aged 15 to 60 was " + str(max_female) + ", occurring in " + max_female_country + ".")
print("Between 2000 and 2016, the lowest mortality rate for female aged 15 to 60 was " + str(min_female) + ", occurring in " + min_female_country + ".")


print("")
#Find the relationship between mortality (from 2000-2016) (ages 15-60) and gender in each country
male_rate_bigger_country = 0
country_amount = len(both_average_dict)
lower_country_ls = []

for key in both_average_dict:
    if male_average_dict[key] > female_average_dict[key]:
        male_rate_bigger_country += 1
    else:
        lower_country_ls.append(key) 
print("In " + str(male_rate_bigger_country) + " of the " + str(country_amount) + " countries in total, men aged 15 to 60 had a higher mortality rate than women aged 15 to 60")
print("Women in these countries have lower mortality rates than men: " + str(lower_country_ls))


print("")
#Find which country has the highest/smallest difference in mortality between male and female
max_difference = 0
min_difference = 1

for key in male_average_dict:
    difference = abs(float(male_average_dict[key]) - float(female_average_dict[key]))
    if difference > max_difference:
        max_difference = difference
        max_difference_country = key
    if difference < min_difference:
        min_difference = difference
        min_difference_country = key

print("The largest gender mortality gap between male and female is " + max_difference_country + ", with a value of " + format(max_difference, ".3f") + ".")
print("The smallest gender mortality gap between male and female is " + min_difference_country + ", with a value of " + format(min_difference, ".3f") + ".")


