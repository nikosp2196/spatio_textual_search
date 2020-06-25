###########################
# PANTELIDIS NIKOS AM2787 #
###########################
import loader
import text_search as ts
import sys
import time

path = 'Data\\Restaurants_London_England.tsv'
restaurants_list, borders = loader.load_reviews_to_list(path)

start_time = time.time()
tags_list, bags_of_restaurants = ts.generate_inverted_index(restaurants_list)
if_creation_time = time.time() - start_time

n_of_keywords = len(tags_list)
sorted_frequencies = ts.get_tag_frequency_list(bags_of_restaurants)


print("\n|==============================================================|\n")
print("inverted file creation time:", if_creation_time, "seconds")
print("number of keywords:", n_of_keywords)
print("frequencies:", sorted_frequencies)
print("\n|==============================================================|\n")

q = sys.argv[1:]
start_time = time.time()
result_indexes_raw = ts.kwSearchRaw(q, restaurants_list)
t_raw = time.time() - start_time
print('-->kwSearchRaw:', len(result_indexes_raw), 'results, cost =', t_raw, 'seconds')
'''for i in result_indexes_raw:
    print(restaurants_list[i]['review_id'])
    print('location:', restaurants_list[i]['x'], ',', restaurants_list[i]['y'])
    print('tags:', restaurants_list[i]['tags'], '\n')'''

print("|==============================================================|\n")

start_time = time.time()
result_indexes_if = ts.kwSearchIF(q, tags_list, bags_of_restaurants)
t_if = time.time() - start_time
print('-->kwSearchIF:', len(result_indexes_if), 'results, cost =', t_if, 'seconds')
'''for i in result_indexes_if:
    print(restaurants_list[i]['review_id'])
    print('location:', restaurants_list[i]['x'], ',', restaurants_list[i]['y'])
    print('tags:', restaurants_list[i]['tags'], '\n')'''

print("|==============================================================|\n")