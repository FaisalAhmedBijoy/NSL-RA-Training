import textwrap

def wrap(string, max_width):
    line=textwrap.wrap(string,max_width)
    return line

if __name__ == '__main__':
    text=str(input())
    max_width=int(input())
    elements=wrap(text,max_width)
    for i in elements:
        print(i)