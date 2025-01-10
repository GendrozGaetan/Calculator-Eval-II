class MathFun:

    @classmethod
    def execute(cls, math_request):
        operator = math_request.get_operator()
        ope1 = math_request.get_ope1()
        ope2 = math_request.get_ope2()

        match operator:
            case 'max':
                if ope1 == ope2:
                    raise EqualityException
                else :
                    if ope1 > ope2:
                        print(ope1)
                    else :
                        print(ope2)
            case 'is_sum_even':
                if ope1 % 2:
                    print("The number 1 is paire")
                else :
                    print("The number 1 is impaire")
            case _:
                raise FunOperatorNotSupportedException

class MathFunException(Exception):
    pass

class FunOperatorNotSupportedException(MathFunException):
    print("The operator is invalid")

class EqualityException(MathFunException):
    print("Numbers are the same")