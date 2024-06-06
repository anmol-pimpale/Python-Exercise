#4: Write a program to read from a file, pre-pending each line with "DIOT-" 
# and write to the different file 



input_file_handle = open("/home/hpcap/Desktop/abc.txt","r")
output_file_handle = open("/home/hpcap/Desktop/modified_file.txt","w")

for input_line in input_file_handle:
    modified_input_line = "HPCAP "+input_line
    output_file_handle.write(modified_input_line)


input_file_handle.close()    
output_file_handle.close()  

