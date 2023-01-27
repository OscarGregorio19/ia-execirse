import csv

with open('magic.csv', newline='') as File:  
    reader = csv.reader(File)
    f = open("catalogo_magic_affinity.sql","w+")
    cont = 1
    for row in reader:
        query = f"""INSERT INTO reino.ct_magic_affinity(
	        id, name, description, status)
	        VALUES ({cont}, '{row[0]}', '{row[0]}', 1);\n"""
        f.write(query)
        cont += 1
    f.close()