def split_and_join(line):
    line=line.split(" ")
    line='-'.join(line)
    return line
input_str=str(input())
print(split_and_join(input_str))