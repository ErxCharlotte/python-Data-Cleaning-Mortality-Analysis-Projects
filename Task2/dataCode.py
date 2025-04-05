import matplotlib.pyplot as plt
import math
import numpy as np

#Dictionaries or variables for storing the data to be used
#1: used to store the mortality rate for men, women, and overall by year
country_dict = {}
country_number = 0
overall_total_rate_by_year = {}
man_total_rate_by_year = {}
woman_total_rate_by_year = {}

#2: used to store the mortality number per 1000 for men, women, and overall by year
overall_total_number_by_year = {}
man_total_number_by_year = {}
woman_total_number_by_year = {}

#3: used to store the highest and lowest mortality rates across all countries in each year
overall_max_rate_by_year = {}
overall_min_rate_by_year = {}
man_max_rate_by_year = {}
man_min_rate_by_year = {}
woman_max_rate_by_year = {}
woman_min_rate_by_year = {}



#Read the data about country, year, probability of dying between 15 and 60 years per 1000 population for 
#male, female, and overall in data.
is_first = True
for row in open("data_merged.csv"):
    if is_first:
        is_first = False
    else:
        data = row.split(",")
        country = data[9]
        year = data[10]
        #use %
        overall_mortality_rate = (int(data[11])/1000)*100
        man_mortality_rate = (int(data[12])/1000)*100
        woman_mortality_rate = (int(data[13])/1000)*100

        overall_mortality_number = int(data[11])
        man_mortality_number = int(data[12])
        woman_mortality_number = int(data[13])

#Because most of the data contained in the data are from 2000-2014, and the data in 2015 is relatively small, it is excluded.
        if year == "2015":
            continue
#1: Find the total mortality rate for men, women, and overall over the years.
        if country not in country_dict:
            country_dict[country] = 1

        if year not in overall_total_rate_by_year:
            overall_total_rate_by_year[year] = overall_mortality_rate
            man_total_rate_by_year[year] = man_mortality_rate
            woman_total_rate_by_year[year] = woman_mortality_rate
        else:
            overall_total_rate_by_year[year] += overall_mortality_rate
            man_total_rate_by_year[year] += man_mortality_rate
            woman_total_rate_by_year[year] += woman_mortality_rate


#2: Find the mortality number per 1000 for men, women, and overall by year.
        if year not in overall_total_number_by_year:
            overall_total_number_by_year[year] = overall_mortality_number
            man_total_number_by_year[year] = man_mortality_number
            woman_total_number_by_year[year] = woman_mortality_number
        else:
            overall_total_number_by_year[year] += overall_mortality_number
            man_total_number_by_year[year] += man_mortality_number
            woman_total_number_by_year[year] += woman_mortality_number

#3: Find the highest and lowest death rates across all countries in each year.
        if year not in overall_max_rate_by_year:
            overall_max_rate_by_year[year] = overall_mortality_rate
            overall_min_rate_by_year[year] = overall_mortality_rate
            man_max_rate_by_year[year] = man_mortality_rate
            man_min_rate_by_year[year] = man_mortality_rate
            woman_max_rate_by_year[year] = woman_mortality_rate
            woman_min_rate_by_year[year] = woman_mortality_rate
        else:
            if overall_mortality_rate > overall_max_rate_by_year[year]:
                overall_max_rate_by_year[year] = overall_mortality_rate
            if overall_mortality_rate < overall_min_rate_by_year[year]:
                overall_min_rate_by_year[year] = overall_mortality_rate
            if man_mortality_rate > man_max_rate_by_year[year]:
                man_max_rate_by_year[year] = man_mortality_rate
            if man_mortality_rate < man_min_rate_by_year[year]:
                man_min_rate_by_year[year] = man_mortality_rate
            if woman_mortality_rate > woman_max_rate_by_year[year]:
                woman_max_rate_by_year[year] = woman_mortality_rate
            if woman_mortality_rate < woman_min_rate_by_year[year]:
                woman_min_rate_by_year[year] = woman_mortality_rate

#Calculate the country number
for key in country_dict:
    country_number += 1



#1: Exploring changes in the average mortality rate for men, women, and overall over the years.
overall_average = []
man_average = []
woman_average = []
year_label = []
for key in overall_total_rate_by_year:
    overall_total_rate_by_year[key] /= country_number  
    man_total_rate_by_year[key] /= country_number  
    woman_total_rate_by_year[key] /= country_number
    overall_average.append(overall_total_rate_by_year[key])
    man_average.append(man_total_rate_by_year[key])
    woman_average.append(woman_total_rate_by_year[key])
    year_label.append(key)

print("The average number for bothsex: \n" , overall_average)
print("The average number for male: \n" , man_average)
print("The average number for female: \n" , woman_average)
print("The year: \n" , year_label)

font_title = {'size':17, 'fontweight':'bold'}
font_label = {'size':15}
plt.title("The average mortality rate between 15-60 years by sex with the year", font_title)
plt.xlabel("Year (year)", font_label)
plt.ylabel("Average mortality rate between 15-60 years (%)", font_label)

plt.plot(year_label,overall_average,marker = 'o', label='Overall', color='g')
plt.plot(year_label,man_average,marker = 'v', label='Man', color='b')
plt.plot(year_label,woman_average,marker = 's', label='Woman', color='y')
plt.legend(loc=4, prop={'size': 16})
plt.grid()
plt.show()



#2: Exploring the changes of the difference of the mortality number per 1000 for men, women, and overall by year.
man_number = []
woman_number = []
man_woman_difference = []
year_label = []

for key in overall_total_number_by_year:
    overall_total_number_by_year[key] /= country_number
    man_total_number_by_year[key] /= country_number  
    woman_total_number_by_year[key] /= country_number
    man_number.append(man_total_number_by_year[key])
    woman_number.append(woman_total_number_by_year[key])
    man_woman_difference.append(man_total_number_by_year[key] - woman_total_number_by_year[key])
    year_label.append(key)

print("The total number for male: \n" , man_number)
print("The total number for female: \n" , woman_number)
print("The difference between male and female: \n" , man_woman_difference)
print("The year: \n" , year_label)


plt.bar(np.arange(len(year_label))-0.25,man_number,label='Man', width = 0.25, hatch='-')
plt.bar(year_label,woman_number,label='Woman', width = 0.25, hatch='//')
plt.bar(np.arange(len(year_label))+0.25,man_woman_difference,label='Difference between man and woman', width = 0.25, hatch='\\')

font_title = {'size':17, 'fontweight':'bold'}
font_label = {'size':15}
plt.title("The death number (per 1,000 population) between 15-60 years by gender with the year", font_title)
plt.xlabel("Year (year)", font_label)
plt.ylabel("Mortality number (per 1,000 population)", font_label)
plt.legend(loc=0, prop={'size': 12})
plt.grid(axis='y')

plt.show()



#3: Exploring the maxmium and the minimum between the countries each year.
overall_difference_rate = []
man_difference_rate = []
woman_difference_rate = []
year_label = []

for key in overall_max_rate_by_year:
    overall_difference_rate.append(overall_max_rate_by_year[key] - overall_min_rate_by_year[key])
    man_difference_rate.append(man_max_rate_by_year[key] - man_min_rate_by_year[key])
    woman_difference_rate.append(woman_max_rate_by_year[key] - woman_min_rate_by_year[key])
    year_label.append(key)

print("The difference between the max and the min for bothsex: \n" , overall_difference_rate)
print("The difference between the max and the min for male: \n" , man_difference_rate)
print("The difference between the max and the min for female: \n" , woman_difference_rate)
print("The year: \n" , year_label)


plt.subplot(211)
plt.bar(np.arange(len(year_label))-0.25,overall_difference_rate,label='Overall', width = 0.25, hatch='-', color='#FF8C00')
plt.bar(year_label,man_difference_rate,label='Man', width = 0.25, hatch='//', color='#F5DEB3')
plt.bar(np.arange(len(year_label))+0.25,woman_difference_rate,label='Woman', width = 0.25, hatch='\\', color='g')
plt.grid(axis='y')

font_title = {'size':17, 'fontweight':'bold'}
font_label = {'size':10}
plt.title("Difference between maximum and minimum number of deaths by gender with the year", font_title)
plt.xlabel("Year (year)", font_label)
plt.ylabel("Difference value (per 1,000 population)", font_label)

plt.legend(loc=1, prop={'size': 10})

plt.subplot(212)
plt.plot(year_label,overall_difference_rate,marker = 'o', label='Overall', color='#FFDEAD')
plt.plot(year_label,man_difference_rate,marker = 'v', label='Man', color='#FF8C00')
plt.plot(year_label,woman_difference_rate,marker = 's', label='Woman', color='g')
plt.xlabel("Year (year)", font_label)
plt.ylabel("Difference value (per 1,000 population)", font_label)
plt.legend(loc=1, prop={'size': 10})
plt.grid()

plt.show()
