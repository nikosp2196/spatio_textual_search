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
float_q = [float(i) for i in q]
if float_q[0] < borders['min_x'] or float_q[1] > borders['max_x'] or \
    float_q[2] < borders['min_y'] or float_q[3] > borders['max_y']:
    print('INPUT OUT OF BORDERS.\n PLEASE RERUN THE SCRIPT WITH A RECTANGLE THAT IS CONTAINED IN THE BORDERS:')
    print(borders)
    exit()

start_time = time.time()
results_raw = ss.spaSearchRaw(float_q, restaurants_list)
raw_time = time.time() - start_time
print("\n|==============================================================|\n")
print('-->spaSearchRaw:', len(results_raw), 'results, cost:', raw_time, 'seconds\n')
for r in results_raw:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')


start_time = time.time()
results_grid = ss.spaSearchGrid(float_q, x_list, y_list, grid, restaurants_list)
grid_time = time.time() - start_time
print("\n|==============================================================|\n")
print('spaSearchGrid:', len(results_grid), 'results, cost:', grid_time, 'seconds\n')
for r in results_grid:
    print(restaurants_list[r]['review_id'])
    print('location:', restaurants_list[r]['x'], ',', restaurants_list[r]['y'])
    print('tags:', restaurants_list[r]['tags'], '\n')
print("\n|==============================================================|\n")
