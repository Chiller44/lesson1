from pickletools import long1

myfile = 'workfile.txt'

with open('workfile.txt', 'r') as file, open('workfile1.txt', 'w') as file2:
    text_file = file.readlines()
    #for i in text_file:
    #   if len(i) > 5:
    #       file2.write(i)
    for line in file:
        words = line.split()
        longwords = [word for word in words if len(word) > 5]
        file2.write(" ".join(longwords))
print(text_file)
print(type(text_file))
#print(text_file[9])


