def generate_inverted_index(reviews_dict_list):
    inverted_index = {}
    for i,r in enumerate(reviews_dict_list):
        for t in r['tags']:
            if t not in inverted_index.keys():
                inverted_index[t] = []
            inverted_index[t].append(i)
    return inverted_index


def get_tag_frequency_list(inverted_index):
    tags_frequencies = []
    for t in inverted_index.keys():
        tags_frequencies.append(len(inverted_index[t]))
    
    return sorted(tags_frequencies)