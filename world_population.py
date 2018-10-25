import json
import pygal
from pygal.maps.world import World
from country_codes import get_country_code

# Load the data into a list.
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# Build a dictionary of population data.
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        # print(country_name + ": " + str(population))
        code = get_country_code(country_name)
        if code:
            # print(code + ": " + str(population))
            cc_populations[code] = population
            break
        else:
            # print ('ERROR - ' + country_name)
            pass

wm = World()
wm.title = 'World Population in 2010, by Country'
wm.add(2010, cc_populations)

print(cc_populations)

wm.render_to_file('world_populations.svg')