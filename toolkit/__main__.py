import sys

import toolkit.calculation as clc
import toolkit.converter as cnv
import toolkit.tokenize as tknz
from toolkit.errors import EmptyExpressionError, InvalidCommandError


def main():
    if sys.argv[1] == "tokenize":
        result = tknz.tokenize(sys.argv[2])
        print(result)
    if sys.argv[1] == "postfix":
        result = tknz.tokenize(sys.argv[2])
        print(clc.infix_to_postfix(result))
    if sys.argv[1] == "calc":
        if sys.argv[2].strip():
            raise EmptyExpressionError("Ошибка: выражение пустое")
        if len(sys.argv) != 3:
            raise InvalidCommandError("Ошибка: команда введена неверно")
        result = clc.calc(clc.infix_to_postfix(tknz.tokenize(sys.argv[2])))
        print(result)
    if sys.argv[1] == "convert":
        if len(sys.argv) != 7:
            raise InvalidCommandError("Ошибка: команда введена неверно")
        else:
            result = cnv.convert(sys.argv[2], sys.argv[4], sys.argv[6])
            print(result)

if __name__ == "__main__":
    main()
    print(sys.argv)
