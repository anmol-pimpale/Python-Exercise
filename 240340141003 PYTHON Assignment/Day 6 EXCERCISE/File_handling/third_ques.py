#Write a program to read from a file and modify eacf of its line
# by pre-pending each line with "DIOT-" 

# ex: 
# i/p : hello
#       good morning  

# o/p:      DIOT-hello
#           DIOT-good morning

# with  open('/home/hpcap/Desktop/abc.txt', 'r') as file1,open('/home/hpcap/Desktop/abc.txt', 'w') as file2:
#     for line in file1:
#         file2.write("DIOT-" + line)



# input_file_handle = open("my_file.txt","r")
# contents_in_list = []

# for input_line in input_file_handle:
#     contents_in_list.append(input_line)
# input_file_handle.close()

# input_file_handle = open("my_file.txt","w")    
# for list_input_line in contents_in_list:
#         input_file_handle.write("HPCAP "+list_input_line)


with open('/home/hpcap/Desktop/abc.txt', 'r') as file1:
    lines = file1.readlines()

with open('/home/hpcap/Desktop/abc.txt', 'w') as file2:
    for line in lines:
        file2.write("IDOT-" + line + "\n")