"""Token constants."""
# Auto-generated by Tools/build/generate_token.py

__all__ = ['tok_name', 'ISTERMINAL', 'ISNONTERMINAL', 'ISEOF']

ENDMARKER = 0
NAME = 1
NUMBER = 2
NEWLINE = 3
INDENT = 4
DEDENT = 5
LPAR = 6
RPAR = 7
LSQB = 8
RSQB = 9
COLON = 10
COMMA = 11
SEMI = 12
PLUS = 13
MINUS = 14
STAR = 15
SLASH = 16
VBAR = 17
AMPER = 18
LESS = 19
GREATER = 20
EQUAL = 21
DOT = 22
PERCENT = 23
LBRACE = 24
RBRACE = 25
EQEQUAL = 26
NOTEQUAL = 27
LESSEQUAL = 28
GREATEREQUAL = 29
TILDE = 30
CIRCUMFLEX = 31
LEFTSHIFT = 32
RIGHTSHIFT = 33
DOUBLESTAR = 34
PLUSEQUAL = 35
MINEQUAL = 36
STAREQUAL = 37
SLASHEQUAL = 38
PERCENTEQUAL = 39
AMPEREQUAL = 40
VBAREQUAL = 41
CIRCUMFLEXEQUAL = 42
LEFTSHIFTEQUAL = 43
RIGHTSHIFTEQUAL = 44
DOUBLESTAREQUAL = 45
DOUBLESLASH = 46
DOUBLESLASHEQUAL = 47
AT = 48
ATEQUAL = 49
RARROW = 50
ELLIPSIS = 51
COLONEQUAL = 52
EXCLAMATION = 53
OP = 54
TYPE_IGNORE = 55
TYPE_COMMENT = 56
SOFT_KEYWORD = 57
FSTRING_START = 58
TAGSTRING_START = 59
STRING_START = 60
STRING_MIDDLE = 61
STRING_END = 62
COMMENT = 63
NL = 64
# These aren't used by the C tokenizer but are needed for tokenize.py
ERRORTOKEN = 65
ENCODING = 66
N_TOKENS = 67
# Special definitions for cooperation with parser
NT_OFFSET = 256

tok_name = {value: name
            for name, value in globals().items()
            if isinstance(value, int) and not name.startswith('_')}
__all__.extend(tok_name.values())

EXACT_TOKEN_TYPES = {
    '!': EXCLAMATION,
    '!=': NOTEQUAL,
    '%': PERCENT,
    '%=': PERCENTEQUAL,
    '&': AMPER,
    '&=': AMPEREQUAL,
    '(': LPAR,
    ')': RPAR,
    '*': STAR,
    '**': DOUBLESTAR,
    '**=': DOUBLESTAREQUAL,
    '*=': STAREQUAL,
    '+': PLUS,
    '+=': PLUSEQUAL,
    ',': COMMA,
    '-': MINUS,
    '-=': MINEQUAL,
    '->': RARROW,
    '.': DOT,
    '...': ELLIPSIS,
    '/': SLASH,
    '//': DOUBLESLASH,
    '//=': DOUBLESLASHEQUAL,
    '/=': SLASHEQUAL,
    ':': COLON,
    ':=': COLONEQUAL,
    ';': SEMI,
    '<': LESS,
    '<<': LEFTSHIFT,
    '<<=': LEFTSHIFTEQUAL,
    '<=': LESSEQUAL,
    '=': EQUAL,
    '==': EQEQUAL,
    '>': GREATER,
    '>=': GREATEREQUAL,
    '>>': RIGHTSHIFT,
    '>>=': RIGHTSHIFTEQUAL,
    '@': AT,
    '@=': ATEQUAL,
    '[': LSQB,
    ']': RSQB,
    '^': CIRCUMFLEX,
    '^=': CIRCUMFLEXEQUAL,
    '{': LBRACE,
    '|': VBAR,
    '|=': VBAREQUAL,
    '}': RBRACE,
    '~': TILDE,
}

def ISTERMINAL(x):
    return x < NT_OFFSET

def ISNONTERMINAL(x):
    return x >= NT_OFFSET

def ISEOF(x):
    return x == ENDMARKER
