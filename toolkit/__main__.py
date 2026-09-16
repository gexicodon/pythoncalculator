import sys
import toolkit.tokenize as tknz
import toolkit.calculation as clc
if __name__ == "__main__":
    if sys.argv[1] == 'tokenize':
        result = tknz.tokenize(sys.argv[2])  
        print(result)
    if sys.argv[1] == 'calc':
        postfix = clc.infix_to_postfix(tknz.tokenize(sys.argv[2]))
        result = clc.calc(clc.infix_to_postfix(tknz.tokenize(sys.argv[2])))
        print(postfix)
        print(result)