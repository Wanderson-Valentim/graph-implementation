def read_file(file_name):
    data = {
        'information': [],
        'edges': []
    }
    is_first_iteration = True
    
    with open(f'./graphs/{file_name}.txt') as file:
        for line in file:
            if(is_first_iteration):
                is_first_iteration = False
                data['information'] = line.split()
            elif(line == '\n'):
                continue
            else:
                data['edges'].append(line.split())
    
    return data