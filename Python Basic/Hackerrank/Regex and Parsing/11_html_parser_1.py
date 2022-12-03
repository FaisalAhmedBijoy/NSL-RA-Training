"""

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Found a start tag  :", tag
    def handle_endtag(self, tag):
        print "Found an end tag   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Found an empty tag :", tag

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed("<html><head><title>HTML Parser - I</title></head>"
            +"<body><h1>HackerRank</h1><br /></body></html>")

"""


"""
Sample Input

2
<html><head><title>HTML Parser - I</title></head>
<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>
Sample Output

Start : html
Start : head
Start : title
End   : title
End   : head
Start : body
-> data-modal-target > None
-> class > 1
Start : h1
End   : h1
Empty : br
End   : body
End   : html

"""
"""


from html.parser import HTMLParser 

class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
                print("Start :", tag)
                for attr in attrs:
                        print('->', attr[0], '>', attr[1])

        def handle_endtag(self, tag):
                print("End   :", tag)

        def handle_startendtag(self, tag, attrs):
                print("Empty :", tag)
                for attr in attrs:
                        print('->', attr[0], '>', attr[1])

MyHTMLParser().feed('\n'.join([input() for _ in range(int(input()))]))

"""

from html.parser import HTMLParser 

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for attr in attrs:
            print ("->", attr[0], ">", attr[1])
    def handle_endtag(self, tag):
        print ("End   :", tag)
    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for attr in attrs:
            print ("->", attr[0], ">", attr[1])

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
n=int(input())
for _ in range(n):
    parser.feed(input())
# parser.feed("<html><head><title>HTML Parser - I</title></head>"
#             +"<body><h1>HackerRank</h1><br /></body></html>"
#             +"<body data-modal-target class='1'><h1>HackerRank</h1><br /></body></html>")