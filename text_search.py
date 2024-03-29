###########################
# PANTELIDIS NIKOS AM2787 #
###########################


def generate_inverted_index(reviews_dict_list):
    tags_list = []
    bags_of_restaurants = []

    for i_r,r in enumerate(reviews_dict_list):
        for t in r['tags']:
            new_tag = True
            for i_st,st in enumerate(tags_list):
                if st == t:
                    new_tag = False
                    break
            if new_tag:
                tags_list.append(t)
                bags_of_restaurants.append([])
                bags_of_restaurants[-1].append(i_r)
            else:
                bags_of_restaurants[i_st].append(i_r)

    tags_list, bags_of_restaurants = zip(*sorted(zip(tags_list, bags_of_restaurants)))

    return tags_list, bags_of_restaurants


def get_tag_frequency_list(bags_of_restaurants):
    tags_frequencies = []
    for b in bags_of_restaurants:
        tags_frequencies.append(len(b))
    
    return sorted(tags_frequencies)


def kwSearchIF(text_list, tags_list, bags_list):

    if_indexes = merge_join(text_list, tags_list)
    if if_indexes == -1:
        return []

    r_intersection = set(bags_list[if_indexes[0]])
    if len(if_indexes) > 1:
        for i in range(1, len(if_indexes)):
            r_intersection = r_intersection.intersection(bags_list[if_indexes[i]])

    return list(r_intersection)


def merge_join(q, tag_list):
    q = sorted(q)
    q_ptr = 0
    t_ptr = 0
    results = []
    while q_ptr < len(q) and t_ptr < len(tag_list):
        if q[q_ptr] == tag_list[t_ptr]:
            results.append(t_ptr)
            q_ptr += 1
            t_ptr += 1
        elif q[q_ptr] > tag_list[t_ptr]:
            t_ptr += 1
        else:
            return -1
    return results


def kwSearchRaw(text_list, restaurants_list):
    results = []
    for i,r in enumerate(restaurants_list):
        valid_review = True
        for q in text_list:
            if q not in r['tags']:
                valid_review = False
                break
        
        if valid_review:
            results.append(i)
    
    return results