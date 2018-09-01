def city_country_func(city, country, pop=''):
    if pop:
        info = city + ", " + country + " has a population of " + pop
    else:
        info = city + ", " + country
    return info
