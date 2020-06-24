import loader
import text_search as ts
import sys


path = 'Data\\Restaurants_London_England.tsv'
restaurants_list, borders = loader.load_reviews_to_list(path)

tags_list, bags_of_restaurants = ts.generate_inverted_index(restaurants_list)

n_of_keywords = len(tags_list)
sorted_frequencies = ts.get_tag_frequency_list(bags_of_restaurants)

print("number of keywords:", n_of_keywords)
print("frequencies:", sorted_frequencies)

q = sys.argv[1:]

result_indexes_raw, t_raw = ts.kwSearchRaw(q, restaurants_list)
print('kwSearchRaw:', len(result_indexes_raw), 'results, cost =', t_raw, 'seconds')
for i in result_indexes_raw:
    print(restaurants_list[i]['review_id'])
    print('location:', restaurants_list[i]['x'], ',', restaurants_list[i]['y'])
    print('tags:', restaurants_list[i]['tags'], '\n')

print("==============================================================\n")

result_indexes_if, t_if = ts.kwSearchIF(q, tags_list, bags_of_restaurants)
print('kwSearchIF:', len(result_indexes_if), 'results, cost =', t_if, 'seconds')
for i in result_indexes_if:
    print(restaurants_list[i]['review_id'])
    print('location:', restaurants_list[i]['x'], ',', restaurants_list[i]['y'])
    print('tags:', restaurants_list[i]['tags'], '\n')


print(borders)