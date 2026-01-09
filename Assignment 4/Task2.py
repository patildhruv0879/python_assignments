write_file = open("Output.txt", 'w')
data=input("Enter text to write to the file: ")
write_file.write(data)
print("Data written to 'Output.txt' successfully.")
write_file.close()


file= open("Output.txt", 'a')
data2=input("Enter additional text to append to the file: ")
file.write("\n"+data2)
print("Data appended to 'Output.txt' successfully.")
file.close()

file= open("Output.txt", 'r')
print("Final contents of the file:")
for line in file:
    print(line.strip()) 