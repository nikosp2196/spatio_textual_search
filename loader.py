import csv
import copy

def load_reviews_to_list(path):
    reviews = []
    borders = {
        'min_x': 100000,
        'max_x': -100000,
        'min_y': 100000,
        'max_y': -100000
    }
    '''min_x = 10000
    max_x = -10000
    min_y = 10000
    max_y = -10000'''

    with open(path) as tsv_file:
        read_tsv = csv.reader(tsv_file, delimiter='\t')
        for row in read_tsv:
            review_id = row[0]
            
            tmp_location = row[1].split(": ")
            x,y = tmp_location[1].split(",")
            x = float(x)
            y = float(y)
            update_borders(borders, x, y)
            
            
            tmp_tags = row[2].split(": ")
            tags_list = tmp_tags[1].split(",")
            
            tmp_review_dict = {
                'review_id': review_id,
                'x': x,
                'y': y,
                'tags': tags_list
            }
            reviews.append(tmp_review_dict)
    

    return reviews, borders


def update_borders(borders, current_x, current_y):
    
    if current_x > borders['max_x']:
        borders['max_x'] = current_x
    
    if current_x < borders['min_x']:
        borders['min_x'] = current_x

    if current_y > borders['max_y']:
        borders['max_y'] = current_y
    
    if current_y < borders['min_y']:
        borders['min_y'] = current_y