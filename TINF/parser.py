import scanner

# E -> +EE| -EE| *EE| /EE| %EE| =EE| <EE| >EE| <>EE| <=EE| >=EE| id| zahl
def E(tokens):
    # +EE| -EE| *EE| /EE| %EE| =EE| <EE| >EE| <>EE| <=EE| >=EE
    if(scanner.nextTokenIsOperator(tokens, "all")):
        if(E(tokens)):
            if(E(tokens)):
                return True
    # zahl
    elif(scanner.nextTokenIsNumber(tokens)):
        return True
    # id
    elif(scanner.nextTokenIsWord(tokens)):
        return True
    return False

# s2-> if E then S;| id:=E;| goto zahl;| read(id);| write (E);| begin S s1
def s2(tokens):
    # if E then S;
    if(scanner.nextTokenIsKeyword(tokens, "if")):
        if(E(tokens)):
            if(scanner.nextTokenIsKeyword(tokens, "then")):
                if(S(tokens)):
                    if(scanner.nextTokenIsOperator(tokens, ";")):
                        return True
    # id:=E;
    elif(scanner.nextTokenIsWord(tokens)):
        if(scanner.nextTokenIsOperator(tokens, ":=")):
            if(E(tokens)):
                if(scanner.nextTokenIsOperator(tokens, ";")):
                    return True
    # goto zahl;
    elif(scanner.nextTokenIsKeyword(tokens, "goto")):
        if(scanner.nextTokenIsNumber(tokens)):
            if(scanner.nextTokenIsOperator(tokens, ";")):
                return True
    # read(id);| write (E);
    elif(scanner.nextTokenIsKeyword(tokens, "read") or scanner.nextTokenIsKeyword(tokens, "write")):
        if(scanner.nextTokenIsOperator(tokens, "(")):
            if(scanner.nextTokenIsWord(tokens)):
                if(scanner.nextTokenIsOperator(tokens, ")")):
                    if(scanner.nextTokenIsOperator(tokens, ";")):
                        return True
    # begin S s1
    if(scanner.nextTokenIsKeyword(tokens, "begin")):
        if(S(tokens)):
            if(s1(tokens)):
                return True
    return False

# s1-> Ss1| end;
def s1(tokens):
    # Ss1
    if(S(tokens)):
        if(s1(tokens)):
            return True
    # end;
    elif(scanner.nextTokenIsKeyword(tokens, "end")):
        if(scanner.nextTokenIsOperator(tokens, ";")):
            return True
    return False

# S -> :zahl s2| s2
def S(tokens):
    # :zahl s2
    if(scanner.nextTokenIsOperator(tokens, ":")):
        if(scanner.nextTokenIsNumber(tokens)):
            if(s2(tokens)):
                return True
    # s2
    elif(s2(tokens)):
        return True
    return False

# P -> prog id; begin Ss1
def P(tokens):
    # prog id; begin Ss1
    if(scanner.nextTokenIsKeyword(tokens, "prog")):
        if(scanner.nextTokenIsWord(tokens)):
            if(scanner.nextTokenIsOperator(tokens, ";")):
                if(scanner.nextTokenIsKeyword(tokens, "begin")):
                    if(S(tokens)):
                        if(s1(tokens)):
                            return True
    return False

# The Parser gets all tokens from the Scanner and sends him to definition
# No Error: "The input works fine!!!"
# Error: "Your Program doesnt work! Error is at position ${index}, with token: ${tokens[0]}"
# Where index is the token index that was wrong, and tokens[0] is the token itself
def parse(codeToParse):
    tokens = scanner.scan(codeToParse)
    if(P(tokens)):
        print("The input works fine!!!")
    else:
        print("Your Program doesnt work! Error is at position", scanner.index, "with token:", tokens[0])