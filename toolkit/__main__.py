import sys

import toolkit.calculation as clc
import toolkit.converter as cnv
import toolkit.tokenize as tknz
from toolkit.errors import EmptyExpressionError, InvalidCommandError
from toolkit.help import print_help


def main():
    if sys.argv[1] == "calc":
        if sys.argv[2] == "":
            raise EmptyExpressionError("Ошибка: выражение пустое")
        if len(sys.argv) != 3:
            raise InvalidCommandError("Ошибка: команда введена неверно")
        result = clc.calc(clc.infix_to_postfix(tknz.tokenize(sys.argv[2])))
        print(result)
    elif sys.argv[1] == "convert":
        if len(sys.argv) != 7:
            raise InvalidCommandError("Ошибка: команда введена неверно")
        else:
            result = cnv.convert(sys.argv[2], sys.argv[4], sys.argv[6])
            print(result)
    elif sys.argv[1] == '--help':
        print_help()
    else:
        raise InvalidCommandError("Неизвестная команда! Введите python -m toolkit --help для получения справки")


if __name__ == "__main__":
    main()

