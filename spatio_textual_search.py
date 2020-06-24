
###########################
# PANTELIDIS NIKOS AM2787 #
###########################
from spatial_search import *
from text_search import *

# THESE FILE CONTAINS THE FUNCTIONS OF PART 3 AND 
# SOME OF THE TEXTUAL AND SPATIAL SEARCH FUNCTIONS
# BUT APPROPRIATELY MODIFIED TO PIPELINE THE RESULTS
# OF THE FIRST SEARCH IN THE SECOND SEARCH TO FILTER
# THEM 


def kwSpaSearchIF(r_query, t_query, tags_list, bags_of_restaurants, x_list, y_list, grid, restaurants_list):
    tags_results = kwSearchIF(t_query, tags_list, bags_of_restaurants)
    final_results = spaSearchGridAfterIF(r_query, tags_results, x_list, y_list, grid, restaurants_list)
    return final_results


def kwSpaSearchGrid(r_query, t_query, tags_list, bags_of_restaurants, x_list, y_list, grid, restaurants_list):
    grid_results = spaSearchGrid(r_query,x_list,y_list,grid,restaurants_list)
    print("GRID",grid_results[0])
    final_results = kwSearchIFAfterGrid(t_query, tags_list, bags_of_restaurants, grid_results)
    return final_results


def kwSearchIFAfterGrid(text_list, tags_list, bags_list, grid_results):
    s_text_list = sorted(text_list)

    if_indexes = merge_join(s_text_list, tags_list)
    print(if_indexes)
    if if_indexes == -1:
        return []

    r_intersection = set([r for r in bags_list[if_indexes[0]] if r in grid_results])
    if len(if_indexes) > 1:
        for i in range(1, len(if_indexes)):
            r_intersection = r_intersection.intersection([r for r in bags_list[if_indexes[i]] if r in grid_results])

    return list(r_intersection)


def spaSearchGridAfterIF(r_query, tags_results, x_list, y_list, grid, restaurants_list):

    x_min_index = binary_search(x_list, r_query[0])
    x_max_index = binary_search(x_list, r_query[1])

    y_min_index = binary_search(y_list, r_query[2])
    y_max_index = binary_search(y_list, r_query[3])
        
    results = []
    for i in range(y_min_index,y_max_index + 1):
        for j in range(x_min_index,x_max_index + 1):
            if len(grid[i][j]) > 0:
                for r in grid[i][j]:
                    if r in tags_results and \
                        restaurants_list[r]['x'] >= r_query[0] and \
                        restaurants_list[r]['x'] <= r_query[1] and \
                        restaurants_list[r]['y'] >= r_query[2] and \
                        restaurants_list[r]['y'] <= r_query[3]:
                        results.append(r)

    return results