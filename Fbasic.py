
def plus(a, b):
    result = a + b
    return result
    
def minus(a, b):
    result = a - b
    return result
    
def mult(a, b):
    result = a * b
    return result
    
def division(a, b):
    result = a / b
    return result
    
def c_division(a, b):
    result = a // b
    residual = a % b
    return result, residual

def p(a, b):
    result = a ** b
    return result
            

def check_opration(ope):
    if ope == "+": return plus(a, c)
    if ope == "-": return minus(a, c)
    if ope == "*": return mult(a, c)
    if ope == "/": return division(a, c)
    if ope == "//": return c_division(a, c)
    if ope == "**": return p(a, c)






if __name__ == "__main__":
    status = True
    while status:
        try:
            txt = "formul (example -> 2 * 5 | q q q -> Exit):"
            a, b, c = input(txt).split()
            if a == 'q' and b == 'q' and c == 'q':
                break
            a = int(a)
            c = int(c)
            b = str(b)
            result = check_opration(b)
            
            print("The answer is %s" % str(result))
            
        except TypeError:
            print("\nPleas enter a correct data for example 1 * 2 or q q q (\"for exit\") or 9 + 6\n")
        except ValueError:
            print("\nPleas enter a correct Value for example 1 * 2 or q q q (\"for exit\") or 9 + 6\n")
        except ZeroDivisionError:
            print("\ndon't type 0 in // or / \n")
        finally:
            print("\nDebugging was successful\n")

