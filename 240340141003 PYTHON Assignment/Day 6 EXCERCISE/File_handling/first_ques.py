#1: write a program to take some text lines from the user and write it to the file

print("Enter some text lines (type 'quit' to stop):")
with open('/home/hpcap/Desktop/abc.txt', 'w') as file1:
        while True:
            user_input = input("Enter a line of text (or 'quit' to stop): ")
            if user_input.lower() == 'quit':
                break
            file1.write(user_input + "\n")
