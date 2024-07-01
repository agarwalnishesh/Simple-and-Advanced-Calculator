from simple_calculator import SimpleCalculator
from stack import Stack

class AdvancedCalculator(SimpleCalculator):
    def __init__(self):
        """
        Call super().__init__()
        Instantiate any additional data attributes
        """
        super().__init__()
        pass

    def evaluate_expression(self, input_expression):
        """
        Evaluate the input expression and return the output as a float
        Return a string "Error" if the expression is invalid
        """
        try:
            tokens = self.tokenize(input_expression)
            if self.check_brackets(tokens):
                result = self.evaluate_list_tokens(tokens)
                self.history.insert(0, (input_expression, result))
                return result
            else:
                return "Error"
        except:
            return "Error"

        pass

    def tokenize(self, input_expression):
        """
        convert the input string expression to tokens, and return this list
        Each token is either an integer operand or a character operator or bracket
        """
        # s = ''
        # Lis=[]
        # self.expression = input_expression
        # self.expression = self.expression.strip()
        # L=self.expression.split()
        # for i in L:
        # 	if i in '(){}+-/*':
        # 		Lis.append(i)
        # 	else:
        # 		for j in '0123456789':
        # 			if j==i:
        # 				s=s+i
        # 				continue
        # 			if s!='':
        # 				Lis.append(int(s))
        # 				s=''
        # Lis = list(filter(None,Lis))
        # return Lis
        s = ''
        lis = []
        self.expression = input_expression.replace(" ", "")  # Remove whitespaces
        for token in self.expression:
            if token in '(){}+-/*':
                if s != '':
                    lis.append(int(s))
                    s = ''
                lis.append(token)
            else:
                s = s + token
        if s != '':
            lis.append(int(s))
        return lis	
        pass		

    def check_brackets(self, list_tokens):
        """
        check if brackets are valid, that is, all open brackets are closed by the same type 
        of brackets. Also () contain only () brackets.
        Return True if brackets are valid, False otherwise
        """

        obj = Stack()
        brackets = {'(': ')', '{': '}'}
        open_brackets = set(brackets.keys())
        closed_brackets = set(brackets.values())
        for token in list_tokens:
            if token in open_brackets:
                obj.push(token)
            elif token in closed_brackets:
                if obj.is_empty() or brackets[obj.peek()] != token:
                    return False
                obj.pop()
        return obj.is_empty()

        pass

    def evaluate_list_tokens(self, list_tokens):
        open_brackets = {"{", "("}
        close_brackets = {"}", ")"}
        operators = {"+", "-", "*", "/"}

        operator_stack = Stack()
        operand_stack = Stack()

        for token in list_tokens:
            if isinstance(token, int):
                operand_stack.push(token)
            elif token in operators:
                operator_stack.push(token)
            elif token in close_brackets:
                while not operator_stack.is_empty() and operator_stack.peek() not in open_brackets:
                    op = operator_stack.pop()
                    op1 = operand_stack.pop()
                    op2 = operand_stack.pop()
                    result = super().evaluate_expression(str(op2) + str(op) + str(op1))
                    if result == "Error":
                        return "Error"
                    operand_stack.push(result)
                operator_stack.pop()  # Pop the opening bracket

        while not operator_stack.is_empty():
            op = operator_stack.pop()
            op1 = operand_stack.pop()
            op2 = operand_stack.pop()
            result = super().evaluate_expression(str(op2) + str(op) + str(op1))
            if result == "Error":
                return "Error"
            operand_stack.push(result)

        return operand_stack.peek()

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples
        The order is such that the most recently evaluated expression appears first 
        """
        return [(expr, result) for expr, result, _ in self.history[::-1] if result != "Error"]
        pass

