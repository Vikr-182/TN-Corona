file = open("../../data/tn_data.json","r")
string = file.read()
string = "Data = \n" + string
file.close()
file2 = open("../../data/tn_data.json","w")
#file2 = open("../../data/data.json","w")
file2.write(string)
