from enum import IntEnum, auto
from dataclasses import dataclass
from sys import exit

def error(string):
    print("Error: ", string)
    exit(1)

class TokType(IntEnum):
    INT = auto()
    IDENT = auto()
    PLUS = auto()
    K_INT = auto()
    SEMICOLON = auto()
    EQUAL = auto()
    EOF = auto()

@dataclass
class Tok():
    type: TokType
    value: object

keywords = {"int": TokType.K_INT}

class Lexer():
    def __init__(self, src):
        self.src = list(src)
        self.curr = 0
        self.toks = []

    def isInt(self, string):
        try:
            int(string)
            return True
        except ValueError:
            return False

    def advance(self):
        self.curr += 1

    def at(self):
        return self.src[self.curr]

    def lex(self):
        tmp = ""
        while self.curr < len(self.src):
            if self.at() == ";":
                self.toks.append(Tok(TokType.SEMICOLON, 0))
                self.advance()

            elif self.at() == "=":
                self.toks.append(Tok(TokType.EQUAL, 0))
                self.advance()

            elif self.at() == "+":
                self.toks.append(Tok(TokType.PLUS, 0))
                self.advance()

            elif self.isInt(self.at()):
                while self.curr < len(self.src) and self.isInt(self.at()):
                    tmp += self.at()
                    self.advance()
                self.toks.append(Tok(TokType.INT, int(tmp)))
                tmp = ""
            
            elif self.at().isalpha():
                while self.curr < len(self.src) and self.at().isalnum():
                    tmp += self.at()
                    self.advance()
                if tmp in keywords:
                    self.toks.append(Tok(keywords[tmp], 0))
                else:
                    self.toks.append(Tok(TokType.IDENT, tmp))
                tmp = ""
                
            elif self.at().isspace():
                self.advance()

            else:
                error(f"Invlaid character: {self.at()}.")
        self.toks.append(Tok(TokType.EOF, 0))
        return self.toks


print(Lexer("int x = 89;").lex())
