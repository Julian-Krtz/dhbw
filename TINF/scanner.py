import re #module for regex

# language:
#
# words:     a-z,A-z, f.e. Hello
# numbers:    0-9,     f.e. 977
# keywords:  if, then, goto, begin, end ,prog,read, write
# operators: +, -, *, /, %, (, ), =, >, >=, <, <=, <>, ; ,:, :=
#
# CH(2):
# T(G) = {words, numbers, Keywords, Operators}
# Z(G) = {P, S, s1, s2, E}
# S(G) = P
# P(G) =
# P -> prog id; begin Ss1
# S -> :zahl s2| s2
# s1-> Ss1| end;
# s2-> if E then S;| id:=E;| goto zahl;| read(id);| write (E);| begin S s1
# E -> +EE| -EE| *EE| /EE| %EE| =EE| <EE| >EE| <>EE| <=EE| >=EE| id| zahl


# create tokens based on: words, numbers, keywords, operators
regex = r'^if|then|goto|begin|end|prog|read|write|\:\=|\<\=|\>\=|\<\>|[a-zA-Z]+|\d+|\+|\-|\/|\*|\%|\(|\)|\=|\>|\<|\:|\;| $'

# all keywords of the language
keywords = ["if", "then", "goto", "begin", "end", "prog", "read", "write"]

# all operators of the language
op = [":=", "<=", ">=", "<>", "+", "-", "/", "*", "%", "(", ")", "=", ">", "<", ":", ";"]

# Checks for all letters
id = r'^[a-zA-Z]+$'
# Checks for every number
zahl = r'^\d+'

# index to tell user wich token gave the error
index = 0

# scan, scans the text and creates tokens based on the regex and returns them
def scan(str):
    tokens = re.findall(regex, str, re.MULTILINE)
    return tokens

#checks if the next token is a number and removes it from the token list
def nextTokenIsNumber(tokens):
    global index
    if(re.match(zahl, tokens[0])):
        tokens.pop(0)
        index += 1
        return True
    return False

#checks if the next token is a word and removes it from the token list
def nextTokenIsWord(tokens):
    global index
    if(re.match(id, tokens[0]) and not (tokens[0] in keywords)):
        tokens.pop(0)
        index += 1
        return True
    return False

#checks if the next token is a operator and removes it from the token list
def nextTokenIsOperator(tokens, operator):
    global index
    if((operator == "all" and tokens[0] in op) or (tokens[0] == operator)):
        tokens.pop(0)
        index += 1
        return True
    return False

#checks if the next token is a keyword and removes it from the token list
def nextTokenIsKeyword(tokens, keyword):
    global index
    if(tokens[0] == keyword):
        tokens.pop(0)
        index += 1
        return True
    return False