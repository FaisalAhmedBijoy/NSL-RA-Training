from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        # print ("Comment  :", data)
        # single line comment and multi line comment
     
     
        if '\n' in data:
            print (">>> Multi-line Comment",data,sep='\n')
            # print(data)
        else:
            print (">>> Single-line Comment",data,sep='\n')
            # print(data)
        

    def handle_data(self, data):
        if data =='\n':
            pass
        else:
            print (">>> Data", data, sep='\n')


# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n=int(input())
number_of_lines = ""
for _ in range(n):
    number_of_lines += input().rstrip()+'\n'

# print(number_of_lines)
parser.feed(number_of_lines)
