import csv


def load_reviews_to_list(path):
    reviews = []
    with open(path) as tsv_file:
        read_tsv = csv.reader(tsv_file, delimiter='\t')
        for row in read_tsv:
            review_id = row[0]
            
            tmp_location = row[1].split(": ")
            x,y = tmp_location[1].split(",")
            
            tmp_tags = row[2].split(": ")
            tags_list = tmp_tags[1].split(",")
            
            tmp_review_dict = {
                'review_id': review_id,
                'x': float(x),
                'y': float(y),
                'tags': tags_list
            }
            reviews.append(tmp_review_dict)
    return reviews