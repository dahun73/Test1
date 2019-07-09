write_string = "Hello\nwrite_sample text file\n"

with open("write_sample.txt", 'w') as handle:
    handle.write(write_string)
