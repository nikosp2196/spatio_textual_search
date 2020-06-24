

def binary_search(mylist, target):
    list_size = len(mylist)
    median = list_size // 2
    #print(mylist)
    try:
        if target > mylist[median][1]:
            result = binary_search(mylist[median+1:], target) + median + 1
        elif target < mylist[median][0]:
            result = binary_search(mylist[:median], target)
        else:
            result = median
    except:
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
        print()
        grid[y][x].append(ir)

    return grid