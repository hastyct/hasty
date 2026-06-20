from lexer import error

class Node():
    def __repr__(self):
        return "Node()"

class Expr():
    def __repr__(self):
        return "Expr()"

class IntegerExpr(Expr):
    def __init__(self, value: int):
        self.value = value

    def __repr__(self):
        return f"IntNode(value: {self.value})"

class BinaryOpExpr(Expr):
    def __init__(self, left, right, op):
        self.op = op
        self.left = left
        self.right = right

    def __repr__(self):
        return f"BinaryOpNode(op: {self.op}, left: {self.left}, right: {self.right})"

# Binary Operations
#  + - 0

class Parser():
    def __init__(self, toks):
        self.toks = toks
        self.curr = 0
    
    def at(self):
        return self.toks[self.curr]

    def advance(self):
        self.curr += 1

    def expect(self, toktype):
        if self.at().type == toktype:
            ret = self.at()
            self.advance()
            return ret
        else:
            error("Syntax Error.")

    def parse(self):
        pass

    def parse_expr(self):
        left = self.parse_primary()

        while self.at().type == TokType.PLUS:
            op = self.expect(TokType.PLUS)
            right = self.parse_primary()
            left = BinaryOpExpr(left, right, op.value)

        return left

    def parse_primary(self):
        if self.at().type == TokType.INT:
            right = self.expect(TokType.INT)
            return IntegerExpr(right.value)
