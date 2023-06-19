import os

# def extract_entity_name(filename):
#     return filename.split('.')[0];

# for meta_file in os.listdir('./data/meta-data/'):
#     print(extract_entity_name(meta_file))

def read_meta_data(path):
    data = open(path, "rt")
    
    meta_data = []

    for line in data:
        print(line)
        line_data = line.split("\t")
        meta_data.append((line_data[0], line_data[1], line_data[2]))
    
    data.close()

    return meta_data

entity = read_meta_data('data/meta-data/Instituicao.txt')

#print(entity)
