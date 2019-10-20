NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']

def dedup_and_title_case_names(names):
    names = list(dict.fromkeys(names))
    names = [names.title() for names in names]
    
    return names
        
def sort_by_surname_desc(names):
    names = dedup_and_title_case_names(names)
    names = sorted(names, key = lambda x: x.split()[1], reverse = True)
    
    return names
    
def shortest_first_name(names):
    names = dedup_and_title_case_names(names)
    name_dict = []
    for i in names:
        i = i.split()
        name_dict.append({'name': i[0], 'surname': i[1]})
    short_name_sort = sorted(name_dict, key = lambda k: len(k['name']))
    return short_name_sort[0]['name']
