
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'NAME', 'NUMBER',
    'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EQUALS',
    'LPAREN', 'RPAREN',
    )

# Tokens
# r 은 Regular Expression을 의미하는 것

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_EQUALS  = r'='
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t


# Ignored characters
t_ignore = " \t"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# 이까지가 scan
# ------------------------------------------------------------
# 여기서부터 parsing 시작
# Parsing rules

# 우선순위가 높을수록 밑으로 간다.
# 모호성을 제거해주기 위함.
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('right', 'UMINUS'),  # right 는 뭐지?
    )

# dictionary of names
# 심볼테이블. 명령형 프로그래밍 언어에서 변수의 동적 할당을 처리하는 방법.
# 변수를 할당할 때 names 안에 dict 타입의 형태로 value 들이 담기게 된다.
# { NAME : expression }
names = { }


# 변수 할당
def p_statement_assign(t):
    'statement : NAME EQUALS expression'
    names[t[1]] = t[3]


def p_statement_expr(t):
    'statement : expression'
    print(t[1])


# 모호성이 있는 RE라서 이렇게 쓰면 안되지만, precedence를 통해서 모호성을 제거해준다.
def p_expression_binop(t):
    """
    expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
    """
    # ('+', t[1], t[3]) -> abstract syntax tree로 표현하는 방법
    if t[2] == '+'  : t[0] = t[1] + t[3]  # 입력스트링(t[2])으로 '+'가 들어오면 t[1]과 t[3]을 더해서 t[0]에 할당하라
    elif t[2] == '-': t[0] = t[1] - t[3]  # c 프로그래밍에서의 $(위치)와 비슷하다.
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

# 간단한 산술식의 경우 위와 같이 표현할 수 있으나
# if문과 같은 복잡한 구조는 abstract syntax tree를 필요로 한다.
# 물론 산술식도 abstract syntax tree로 표현할 수 있다.

def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]


def p_expression_group(t):
    'expression : LPAREN expression RPAREN'
    t[0] = t[2]


def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]


def p_expression_name(t):
    'expression : NAME'
    try:
        t[0] = names[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0


def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
