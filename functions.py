def returnUpercase(file):
    file = open(file, 'r')
    filecontent = ''
    for lines in file:
        filecontent = filecontent + file.readline()
    filecontentupper = filecontent.upper()
    return filecontentupper

def date_sort(file):
	data = open(file, "r")
	lines = []
	data_dict = {}
	for line in data:
		line = line.strip()
		lines.append(line.split())
	for line in lines:
		date = line[1]
		magnitude = line[0]
		if date in data_dict:
			data_dict[date].append(magnitude)
		else:
			data_dict[date] = [magnitude]
	return data_dict

def dicctionary_to_list(dict):
    list = []
    keys = dict.keys()
    keycount = 0
    for key in keys:
        list.insert(keycount, [key])
        values = dict[key]
        for item in values:
            list[keycount].append(item)
        keycount += 1
    return list
