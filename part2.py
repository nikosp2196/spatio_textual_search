###########################
# PANTELIDIS NIKOS AM2787 #
###########################
import loader
import spatial_search as ss
import sys
import time

path = 'Data\\Restaurants_London_England.tsv'
restaurants_list, borders = loader.load_reviews_to_list(path)

start_time = time.time()
x_list, y_list = ss.create_grid(borders,50)
grid = ss.add_restaurants_to_grid(x_list, y_list, restaurants_list)
grid_creation_time = time.time() - start_time


print("\n|==============================================================|\n")
print("-->grid creation time:", grid_creation_time, "seconds")
ss.print_grid_info(borders,grid)

q = sys.argv[1:]
print(borders)
r_query = [float(i) for i in q]
exit_flag = False
for i in range(2):
    if r_query[i] < borders['min_x'] or r_query[i] > borders['max_x']:
        print("X out of bounds. Exiting")
        exit_flag = True

for i in range(2,4):
    if r_query[i] < borders['min_y'] or r_query[i] > borders['max_y']:
        print("Y out of bounds. Exiting..")
        exit_flag = True

if exit_flag:
    print("Borders:", borders)
    exit()

start_time = time.time()
results_raw = ss.spaSearchRaw(r_query, restaurants_list)
raw_time = time.time() - start_time
print("\n|==============================================================|\n")
print('-->spaSearchRaw:', len(results_raw), 'results, cost:', raw_time, 'seconds\n')
'''for r in results_raw:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')'''


start_time = time.time()
results_grid = ss.spaSearchGrid(r_query, x_list, y_list, grid, restaurants_list)
grid_time = time.time() - start_time
print("\n|==============================================================|\n")
print('spaSearchGrid:', len(results_grid), 'results, cost:', grid_time, 'seconds\n')
'''for r in results_grid:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')'''
print("\n|==============================================================|\n")
