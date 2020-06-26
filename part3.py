###########################
# PANTELIDIS NIKOS AM2787 #
###########################
import loader
from spatio_textual_search import *
from spatial_search import *
from text_search import *
import sys
import time


path = 'Data\\Restaurants_London_England.tsv'
restaurants_list, borders = loader.load_reviews_to_list(path)

# Initialize Grid
x_list, y_list = create_grid(borders,50)
grid = add_restaurants_to_grid(x_list, y_list, restaurants_list)

# Initialize Inverted File
tags_list, bags_of_restaurants = generate_inverted_index(restaurants_list)

r_query = sys.argv[1:5]
r_query = [float(i) for i in r_query]
exit_flag = False
for i in range(2):
    if r_query[i] < borders['min_x'] or r_query[i] > borders['max_x']:
        print("X out of bounds. Exiting")
        exit_flag = True

for i in range(2,4):
    if r_query[i] < borders['min_y'] or r_query[i] > borders['max_y']:
        print("Y out of bounds. Exiting..")
        exit_flag = True

t_query = sys.argv[5:]
if len(t_query) == 0:
    print("No tags were given. Exiting..")
    exit_flag = True

if exit_flag:
    exit()

start_time = time.time()
results_raw = kwSpaSearchRaw(r_query, t_query, restaurants_list)
raw_time = time.time() - start_time
print("\n|==============================================================|\n")
print('-->kwSpaSearchRaw:', len(results_raw), 'results, cost:', raw_time, 'seconds\n')
for r in results_raw:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')


start_time = time.time()
results_if = kwSpaSearchIF(r_query, t_query,tags_list, bags_of_restaurants, x_list, y_list, grid, restaurants_list)
if_time = time.time() - start_time
print("\n|==============================================================|\n")
print('-->kwSpaSearchIF:', len(results_if), 'results, cost:', if_time, 'seconds\n')
for r in results_if:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')


start_time = time.time()
results_grid = kwSpaSearchGrid(r_query, t_query,tags_list, bags_of_restaurants, x_list, y_list, grid, restaurants_list)
grid_time = time.time() - start_time
print("\n|==============================================================|\n")
print('-->kwSpaSearchGrid:', len(results_if), 'results, cost:', grid_time, 'seconds\n')
for r in results_grid:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')

print("\n|==============================================================|\n")
