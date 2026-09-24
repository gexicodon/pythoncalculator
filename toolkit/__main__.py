import sys

import toolkit.calculation as clc
import toolkit.tokenize as tknz
import toolkit.converter as cnv

if __name__ == "__main__":
    if sys.argv[1] == 'tokenize':
        result = tknz.tokenize(sys.argv[2])  
        print(result)
    if sys.argv[1] == 'postfix':
        result = tknz.tokenize(sys.argv[2])
        print(clc.infix_to_postfix(result))
    if sys.argv[1] == 'calc':
        if sys.argv[2] == "":
            raise Exception("Выражение пустое")
        result = clc.calc(clc.infix_to_postfix(tknz.tokenize(sys.argv[2])))
        print(result)
    if sys.argv[1] == 'convert':
        if len(sys.argv) != 7:
            raise Exception("Команда введена неверно")
        else:
            result = cnv.convert(sys.argv[2], sys.argv[4], sys.argv[6])
            print(result)

        