
with open('../../data/tn_data.json', 'r') as fin:
    data = fin.read().splitlines(True)
with open('../../data/tn_data.json', 'w') as fout:
    fout.writelines(data[1:])
