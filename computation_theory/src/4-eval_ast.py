# -----------------------------------------------------------------------------
# Evaluator of Abstract Syntax Trees
# -----------------------------------------------------------------------------

# python에서 tree를 표현하는 방법에는 튜플이 있다.
# ex) ('*', 2, 3) -> child가 2, 3인 * 노드
# *와 같은 경우는 연산자이기 때문에 string으로 표현해줘야 한다.
# ex) ('+', 1, ('*', 2, 3)) -> child가 1, ('*', 2, 3)인 + 노드


ast1 = ('+', ('NUMBER',10), ('NUMBER',20))    # 10 + 20
ast2 = ('=', 'x',                             # x = 10 + 20
        ('+', ('NUMBER',10), ('NUMBER',20)))
             
ast3 = (';', ('=', 'x', ('+', ('NUMBER',10), ('NUMBER',20))),
             ('+', ('NAME','x'), ('NAME','x'))
       )                                      # x = 10 + 20 ; x + x

ast = ast3

print(ast)

# dictionary of names
names = {}


# 어셈블리 언어로 번역을 하고 싶다면 abstract syntax tree를 통해서 된다.
# 모든 웹 프로그래밍에서 parsing 후, abstract syntax tree를 만든 후에 된다.
# HTML DOM 구조가 AST이다.
def eval(tree):
    if not tree:          return 0      # tree == None
    opr = tree[0]
    if opr == '+':        return eval(tree[1]) +  eval(tree[2])
    elif opr == '-':      return eval(tree[1]) - eval(tree[2])
    elif opr == '*':      return eval(tree[1]) *  eval(tree[2])
    elif opr == '/':      return eval(tree[1]) /  eval(tree[2])
    elif opr == 'UMINUS': return - eval(tree[1])
    elif opr == 'NUMBER': return tree[1]
    elif opr == 'NAME':   return names[tree[1]]
    elif opr == ';':      eval(tree[1]); return eval(tree[2])
    elif opr == '=':      names[tree[1]] = eval(tree[2])
    else: 
        print("unexpeced case : ", tree)

print(eval(ast))


















        

    
