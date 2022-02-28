def city_country(city, country, population=''):
    if population != '':
        ret = (f'{city}, {country} - population {population}')
    else:
        ret = (f'{city}, {country}')
    return ret.title() 
