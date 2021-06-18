# Py Adv 4E3 Capitals - creating dict comprehension with zip and then printing it
# output Bulgaria -> Sofia
# Romania -> Bucharest
# Germany -> Berlin
# England -> London
# input Bulgaria, Romania, Germany, England
# Sofia, Bucharest, Berlin, London

countries = [country for country in input().split(", ")]
capitals = [capital for capital in input().split(", ")]
result = {country: capital for country, capital in zip(countries, capitals)}
[print(f'{key} -> {value}') for key, value in result.items()]
