from ply.lex import lex
tokens = [ 'NUM1', 'NUM2', 'NUM3', 'EQ', 'ASSGN' ]
literals = [ '*', '+', '-' ]
t_ignore = ' \t\n'
# Token specifications (as regexs)
t_NUM1   = r'[0-5]+'
t_NUM2   = r'[0-9]+'   #r'\d+'
# t_NUM3 = r'([0-9])+'
t_EQ     = r'='
t_ASSGN  = r'=='
lexer = lex()
data = '''
12345 26 + 8 * 10 + -207 *2 = ==
'''
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)