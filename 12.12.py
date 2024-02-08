# with open("text1.txt", "r") as file:
#     file = file.readlines()



# first_row = file[:1]
# first_row = first_row[0].split('\n')
# first_row = first_row[0].split(',')
# new_file = []
# for i in file[1:]:
#     new_file += [i.split(',')]



# max_pop = max_lat = max_log = min_pop =  []
# max = max2 = max3 = 0 
# min = new_file[1][1]
# for line in new_file:
#     if float(line[1]) > max:
#         max = float(line[1])
#         max_pop = [f"max pop:{max}", line[0]]
#     if float(line[2]) > max2:
#         max2 = float(line[2])
#         max_lat = [f"max lat:{max2}", line[0]]
#     if float(line[1]) < float(min):
#         min = float(line[1])
#         min_pop = [f"min pop:{min}", line[0]]
#     print(i)

# overall = min_pop + max_pop + max_lat

"""
1 mashq
"""

import os 
import sys 
current_dir = os.getcwd()
print(os.listdir(current_dir))

print(list(os.walk(current_dir)))

print(sys.platform)

print(list(os.scandir(current_dir)))