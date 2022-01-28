# Ajay Kumar Reddy Arram

file_open = open("Arram.txt","r")  # open file, read-only
file_sorted = open("sorted_file.txt", "w") # open file, write
lines = file_open.readlines()
lines.sort()

for line in lines:
 file_sorted.write(line)

file_open.close()
file_sorted.close()