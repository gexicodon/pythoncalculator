def tokenize(expr):
    i = 0
    tokens = []
    while i < len(expr):
        if expr[i] == ' ' or expr[i] == '\t':
            i += 1
            continue
        elif expr[i] in '0123456789' and i < len(expr):
            num = ''
            while i < len(expr) and expr[i] in '0123456789':
                num += expr[i]
                i += 1
            if i < len(expr) and expr[i] in '.':
                num += expr[i]
                i += 1
                while i < len(expr) and expr[i] in '0123456789':
                    num += expr[i]
                    i += 1
            tokens.append(("NUMBER", num))

        elif i < len(expr) and expr[i] == '-':
            prev = tokens[-1] if tokens else None
            if prev is None or prev[0] in ("OPERATOR", "LEFT_P"):
                tokens.append(("OPERATOR", "neg"))
            else:
                tokens.append(("OPERATOR", "-"))
            i += 1


        elif i < len(expr) and expr[i] in '+*/':
            tokens.append(("OPERATOR", expr[i]))
            i += 1
            
        elif i < len(expr) and expr[i] == '(':
            tokens.append(("LEFT_P", expr[i]))
            i += 1
        elif i < len(expr) and expr[i] == ')':
             tokens.append(("RIGHT_P", expr[i]))
             i += 1       
        else: raise ValueError(f"Неизвестный символ: {expr[i]!r}")
        
    return tokens