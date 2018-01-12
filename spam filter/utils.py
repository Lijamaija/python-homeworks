def read_classification_from_file(name):
    f = open(name,'r')
    out_dict = {}
    while True:
        line = f.readline()
        if (line == ''):
            break
        words =  line.split()
        out_dict[words[0]] = words[1]
    f.close()
    return out_dict

def write_classification_to_file(dict, fname):
    f = open(fname, 'w')
    for s in dict:
        line = s + ' ' + dict[s] + '\n'
        f.write(line)
    f.close()
    
    
