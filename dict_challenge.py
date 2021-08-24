# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
damages_list = []
def reformat_damage(damages):
    for item in damages:
        # Keeping the non-recorded damages as string
        if item == 'Damages not recorded':
            damages_list.append(item)
        # Appending float value for millions
        elif item[-1] == "M":
            damages_list.append(float(item[:-1])*1000000)
        # Appending float value for billions
        elif item[-1] == "B":
            damages_list.append(float(item[:-1])*1000000000)
    return damages_list
reformat_damage(damages)
# print(damages_list)


# write your construct hurricane dictionary function here:
dict = {}
def make_dict():
    for index in range(0, len(names)):
        dict[names[index]] = {"Name": names[index],
        "Month": months[index],
        "Year": years[index],
        "Max Sustained Wind": max_sustained_winds[index],
        "Areas Affected": areas_affected[index],
        "Damage": damages_list[index],
        "Deaths": deaths[index]}
    return dict

# print(make_dict())


# write your construct hurricane by year dictionary function here:
year_dict = {}
def make_year_dict():
    for index in range(0, len(years)):
        year_dict[years[index]] = {"Name": names[index],
        "Month": months[index],
        "Year": years[index],
        "Max Sustained Wind": max_sustained_winds[index],
        "Areas Affected": areas_affected[index],
        "Damage": damages_list[index],
        "Deaths": deaths[index]}
    return year_dict    
# print(make_year_dict())



# write your count affected areas function here:
areas = []
lst_areas_affected = []
for lst in areas_affected:
    for j in lst:
        lst_areas_affected.append(j)
        if j not in areas:
            areas.append(j)
# print(areas)
dict_areas = {}
def count_areas():
    for i in areas:
        dict_areas[i] = lst_areas_affected.count(i)
    return dict_areas
count_areas()




# write your find most affected area function here:
max_key = max(dict_areas, key=dict_areas.get)
# print(max_key, dict_areas.get(max_key))



# write your greatest number of deaths function here:
def greatest_deaths():
    max_deaths = max(deaths)
    return names[deaths.index(max_deaths)]
# print(greatest_deaths())


# write your catgeorize by mortality function here:
# mortality_scale = {0: 0,
#                    1: 100,
#                    2: 500,
#                    3: 1000,
#                    4: 10000}
mortality_dict = {}
def mortality():
    sub100 = []
    sub500 = []
    sub1000 = []
    sub10000 = []
    over10000 = []
    for i in range(0, len(names)):
        if deaths[i] < 100:
            sub100.append(names[i])
            mortality_dict['0'] = sub100
        elif (deaths[i] > 100 and deaths[i] < 500) :
            sub500.append(names[i])
            mortality_dict['1'] = sub500
        elif (deaths[i] > 500 and deaths[i] < 1000):
            sub1000.append(names[i])
            mortality_dict['2'] = sub1000
        elif (deaths[i] > 1000 and deaths[i] < 10000):
            sub10000.append(names[i])
            mortality_dict['3'] = sub10000
        else:
            over10000.append(names[i])
            mortality_dict['4'] = over10000            
    return mortality_dict
# print(mortality())


# write your greatest damage function here:
number_list = [i for i in damages_list if i != 'Damages not recorded']

def greatest_damage():
    max_damage = max(number_list)
    print(max_damage)
    return names[damages_list.index(max_damage)]
print(greatest_damage())


# write your catgeorize by damage function here:
damages_dict = {}
def damages_func():
    sub100M = []
    sub1B = []
    sub10B = []
    sub50B = []
    over50B = []
    for i in range(0, len(names)):
        if damages_list[i] == 'Damages not recorded':
            continue
        elif damages_list[i] < 100000000:
            sub100M.append(names[i])
            damages_dict['0'] = sub100M
        elif (damages_list[i] > 100000000 and damages_list[i] < 1000000000) :
            sub1B.append(names[i])
            damages_dict['1'] = sub1B
        elif (damages_list[i] > 1000000000 and damages_list[i] < 10000000000):
            sub10B.append(names[i])
            damages_dict['2'] = sub10B
        elif (damages_list[i] > 10000000000 and damages_list[i] < 50000000000):
            sub50B.append(names[i])
            damages_dict['3'] = sub50B
        elif (damages_list[i] > 50000000000):
            over50B.append(names[i])
            damages_dict['4'] = over50B            
    return damages_dict
print(damages_func())