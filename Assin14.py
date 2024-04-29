path1 = 'file1.txt'  # Replace 'source.txt' with the path to the source file
path2= 'file2.txt'  #f Replace 'destination.txt' with the path to the destination file

path1 = open("file1.txt", 'r')
path2= open("file2.txt", 'w')

for line in path1:
    print(readline(line))
    
path1.close()
path2.close()

#print(f"Contents of '{s}' copied to '{destination_file_path}' successfully.")

