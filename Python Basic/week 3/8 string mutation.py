def mutate_string(string,position,char):
    l=list(string)
    l[position]=char
    string=''.join(l)
    print(string)

string=str(input())
l=list(string)
position=int(input())
char=str(input())

mutate_string(string,position,char)