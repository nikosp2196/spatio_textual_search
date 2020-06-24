###########################
# PANTELIDIS NIKOS AM2787 #
###########################
import loader
import spatial_search as ss
import sys


path = 'Data\\Restaurants_London_England.tsv'
restaurants_list, borders = loader.load_reviews_to_list(path)

start_time = ss.time.time()
x_list, y_list = ss.create_grid(borders,50)
grid = ss.add_restaurants_to_grid(x_list, y_list, restaurants_list)
grid_creation_time = ss.time.time() - start_time


print("\n|==============================================================|\n")
print("-->grid creation time:", grid_creation_time, "seconds")
ss.print_grid_info(borders,grid)

q = sys.argv[1:]
float_q = [float(i) for i in q]

results_raw, raw_time = ss.spaSearchRaw(float_q, restaurants_list)

print("\n|==============================================================|\n")
print('-->spaSearchRaw:', len(results_raw), 'results, cost:', raw_time, 'seconds\n')
for r in results_raw:
    print(r['review_id'])
    print('location:', r['x'], ',', r['y'])
    print('tags:', r['tags'], '\n')


results_grid, grid_time = ss.spaSearchGrid(float_q, x_list, y_list, grid, restaurants_list)
print("\n|==============================================================|\n")
print('spaSearchGrid:', len(results_grid), 'results, cost:', grid_time, 'seconds\n')
for r in results_grid:
    print(r['review_id'])
    print('location:', r['x'], ',', r['y'])
    print('tags:', r['tags'], '\n')
print("\n|==============================================================|\n")
