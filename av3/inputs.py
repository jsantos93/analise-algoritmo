def get_entries():
    filenames = ["1000","10000","20000","50000","75000","100000"]
    entries = {}
    for filename in filenames:
        f = open("Entradas/{}.txt".format(filename), "r")
        entry = f.read()
        entry = entry.replace("\n"," ")
        entry = entry.split(" ")
        entries[filename] = [int(i) for i in entry] 
        f.close()
    return entries

def generate_inputs(num_values):
    values = {}
    arr_sorted = [int(x+1) for x in range(num_values)]
    arr_reverse_sorted = [int(x+1) for x in range(num_values)]
    arr_reverse_sorted.reverse()
    values["sorted"] = arr_sorted
    values["reverse_sorted"] = arr_reverse_sorted
    arr_mixed = []
    for i in range(len(arr_sorted)):
        arr_mixed.append(arr_reverse_sorted[i])
        arr_mixed.append(arr_sorted[i])
    values["mixed"] = arr_mixed

    return values