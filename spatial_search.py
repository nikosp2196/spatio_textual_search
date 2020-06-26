###########################
# PANTELIDIS NIKOS AM2787 #
###########################


def binary_search(mylist, target):
    list_size = len(mylist)
    median = list_size // 2
    try:
        if target > mylist[median][1]:
            result = binary_search(mylist[median+1:], target) + median + 1
        elif target < mylist[median][0]:
            result = binary_search(mylist[:median], target)
        else:
            result = median
    except:
        print("ERROR")
        print(mylist)
        print(target)
        print(list_size)
        return 'LOLA'
    return result


def  create_grid(borders, g_size):
    
    x_range = borders['max_x'] - borders['min_x']
    step_x = x_range / g_size
    y_range = borders['max_y'] - borders['min_y']
    step_y = y_range / g_size

    x_list = []
    y_list = []
    

    for i in range(49):
        x_list.append([i * step_x + borders['min_x'], (i + 1) * step_x + borders['min_x']])
        y_list.append([i * step_y + borders['min_y'], (i + 1) * step_y + borders['min_y']])
    
    x_list.append([x_list[-1][1], borders['max_x']])
    y_list.append([y_list[-1][1], borders['max_y']])

    return x_list, y_list


def add_restaurants_to_grid(x_buckets, y_buckets, restaurants_list):
    n_rows = len(y_buckets)
    n_columns = len(x_buckets)
    grid = []
    for i in range(n_rows):
        grid.append([])
        for j in range(n_columns):
            grid[-1].append([])

    for ir, r in enumerate(restaurants_list):
        x = binary_search(x_buckets, r['x'])
        y = binary_search(y_buckets, r['y'])

        grid[y][x].append(ir)

    return grid


def print_grid_info(borders, grid):
    print_borders_info(borders)
    print_non_empty_cells(grid)


def print_borders_info(borders):
    print('bounds:', borders['min_x'], borders['max_x'], borders['min_y'], borders['max_y'])
    print('widths:', borders['max_x'] - borders['min_x'], borders['max_y'] - borders['min_y'])

def print_non_empty_cells(grid):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if len(grid[i][j]) > 0:
                print(j, i, len(grid[i][j])) 


def spaSearchGrid(r_query, x_list, y_list, grid, restaurants_list):
    x_min_index = binary_search(x_list, r_query[0])
    x_max_index = binary_search(x_list, r_query[1])

    y_min_index = binary_search(y_list, r_query[2])
    y_max_index = binary_search(y_list, r_query[3])
    
    results = []
    for i in range(y_min_index,y_max_index + 1):
        for j in range(x_min_index,x_max_index + 1):
            if len(grid[i][j]) > 0:
                for r in grid[i][j]:
                    if restaurants_list[r]['x'] >= r_query[0] and  \
                        restaurants_list[r]['x'] <= r_query[1] and \
                        restaurants_list[r]['y'] >= r_query[2] and \
                        restaurants_list[r]['y'] <= r_query[3]:
                        results.append(r)

    return results


def spaSearchRaw(r_query, restaurants_list):
    results = []
    for i,r in enumerate(restaurants_list):
        if r['x'] >= r_query[0] and r['x'] <= r_query[1] and r['y'] >= r_query[2] and r['y'] <= r_query[3]:
            results.append(i)
        
    return results