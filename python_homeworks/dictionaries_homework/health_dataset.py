countries = ['Romania', 'France', 'Germany', 'Netherlands', 'Spain', 'Portugal']
sexes = ['F', 'M']
years = [2017, 2018]
health_indexes = [3.4, 4, 78, 12, 78.1, 79]

dataset = [
    (country, year, sex, health_index)
    for country in countries
    for year in years
    for sex in sexes
    for health_index in health_indexes
]
#  This implementation will always overwrite the values because we cannot have duplicate key in the same dict
# health_index_2017 = {
#     country: [sex, health_index]
#     for country, year, sex, health_index in dataset
#     if year == 2017
# }

health_index_2017 = {
    country_: [
        [sex, health_index]
        for country, year, sex, health_index in dataset
        if year == 2017 and country == country_
    ]
    for country_ in countries
}

#  This implementation will always overwrite the values because we cannot have duplicate key in the same dict
# health_index_2018 = {
#     country: [sex, health_index]
#     for country, year, sex, health_index in dataset
#     if year == 2018
# }

health_index_2018 = {
    country_: [
        [sex, health_index]
        for country, year, sex, health_index in dataset
        if year == 2018 and country == country_
    ]
    for country_ in countries
}
# print(health_index_2017)
# print(health_index_2018)

# This implementation will always overwrite the values because we cannot have duplicate key in the same dict
# group_by_year = {
#     year: [sex, health_index]
#     for country, year, sex, health_index in dataset
#     if country == 'Germany' and year in years
# }

group_by_year = {
    year: [
        [sex, health_index]
        for country, year, sex, health_index in dataset
        if country == 'Germany'
    ] for year in years
}
# print(group_by_year)

group_by_country_year = {
    country_ + '_' + str(year_): [
        [year, sex, health_index]
        for country, year, sex, health_index in dataset
        if country == country_
    ]
    for country_ in countries for year_ in years
}
# print(group_by_country_year)

# Print health_index > 5
for country_year, values_list in group_by_country_year.items():
    health_index_greater = {
        country_year: [
            [year, sex, health_index]
            for year, sex, health_index in values_list
            if health_index > 5
        ]
        for country_years in group_by_country_year
    }
    print(health_index_greater)

# Print health_index > 5 and sex == 'female'
for country_year, values_list in group_by_country_year.items():
    health_index_sex = {
        country_year: [
            [year, sex, health_index]
            for year, sex, health_index in values_list
            if health_index > 5 and sex == 'F'
        ]
        for country_year in group_by_country_year
    }
    # print(health_index_sex)

# Use for loop for printing the health_index
for country_name, values_list in group_by_country_year.items():
    for year, sex, health_index in values_list:
        print(health_index)
