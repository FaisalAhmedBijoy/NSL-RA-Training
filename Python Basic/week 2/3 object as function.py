# a function can be treated as a variable
def add_explanation(line):
    return line
update_explanation=add_explanation
print(update_explanation('Hello world'))
print(update_explanation)

# variable as a function parameter
def beatify(text):
    return text + '!!'
def make_line(func,word):
    return 'hello ' + func(word)
print(make_line(beatify,'world'))