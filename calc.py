class ArbitraryPrecisionCalculator:
    """
    Arbitrary Precision Calculator

    Purpose and Scope:
    This class provides a solution for performing arithmetic operations on arbitrarily large integers in environments where native support is unavailable. It replicates basic arithmetic functionality by using strings to represent numbers, avoiding the limitations of standard integer types. The calculator is designed for both practical use cases and as a demonstration of algorithmic problem-solving.

    Key Features:
    - Supports addition, subtraction, multiplication, division, modulo, exponentiation, and factorial.
    - Handles arbitrarily large integers through manual digit-by-digit operations.
    - Includes a REPL (Read-Eval-Print Loop) interface for interactive use.

    Design Highlights:
    - Numbers are represented as strings, enabling precision and scalability for large values.
    - Core arithmetic operations are implemented from scratch, ensuring independence from built-in libraries.
    - Robust handling of edge cases, such as division by zero and negative results.

    Methods:
        - add(a, b): Adds two numbers represented as strings.
        - subtract(a, b): Subtracts two numbers represented as strings.
        - multiply(a, b): Multiplies two numbers represented as strings.
        - divide(a, b): Divides two numbers represented as strings, returning quotient.
        - modulo(a, b): Computes the modulo of two numbers represented as strings.
        - exponentiate(base, exp): Computes base^exp using repeated multiplication.
        - factorial(n): Computes the factorial of a number represented as a string.
        - repl(): Starts a REPL (Read-Eval-Print Loop) for the calculator.

    """

    def add(self, a, b):
        """Adds two numbers represented as strings."""
        a, b = str(a), str(b)
        max_len = max(len(a), len(b))
        a, b = a.zfill(max_len), b.zfill(max_len)

        carry = 0
        result = []
        for i in range(max_len - 1, -1, -1):
            digit_sum = int(a[i]) + int(b[i]) + carry
            carry = digit_sum // 10
            result.append(str(digit_sum % 10))
        if carry:
            result.append(str(carry))
        return ''.join(result[::-1])

    def subtract(self, a, b):
        """Subtracts two numbers represented as strings."""
        a, b = str(a), str(b)
        if a == b:
            return "0"
        negative = False
        if len(a) < len(b) or (len(a) == len(b) and a < b):
            a, b = b, a
            negative = True
        b = b.zfill(len(a))

        result = []
        borrow = 0
        for i in range(len(a) - 1, -1, -1):
            diff = int(a[i]) - int(b[i]) - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            result.append(str(diff))
        while result and result[-1] == "0":
            result.pop()
        res = ''.join(result[::-1])
        return f"-{res}" if negative else res

    def multiply(self, a, b):
        """Multiplies two numbers represented as strings."""
        a, b = str(a), str(b)
        result = [0] * (len(a) + len(b))
        for i in range(len(a) - 1, -1, -1):
            for j in range(len(b) - 1, -1, -1):
                mul = int(a[i]) * int(b[j])
                sum = mul + result[i + j + 1]
                result[i + j + 1] = sum % 10
                result[i + j] += sum // 10
        result = ''.join(map(str, result)).lstrip('0')
        return result or '0'

    def divide(self, a, b):
        """Divides two numbers represented as strings and returns the quotient."""
        a, b = str(a), str(b)
        if b == "0":
            raise ValueError("Division by zero is undefined.")
        if a == "0":
            return "0"

        dividend = 0
        quotient = []
        for digit in a:
            dividend = dividend * 10 + int(digit)
            quotient.append(str(dividend // int(b)))
            dividend %= int(b)
        return ''.join(quotient).lstrip('0') or '0'

    def modulo(self, a, b):
        """Computes the modulo of two numbers represented as strings."""
        a, b = str(a), str(b)
        if b == "0":
            raise ValueError("Modulo by zero is undefined.")
        dividend = 0
        for digit in a:
            dividend = dividend * 10 + int(digit)
            dividend %= int(b)
        return str(dividend)

    def exponentiate(self, base, exp):
        """Computes base^exp using repeated multiplication."""
        base, exp = str(base), int(exp)
        if exp == 0:
            return "1"
        result = "1"
        for _ in range(exp):
            result = self.multiply(result, base)
        return result

    def factorial(self, n):
        """Computes the factorial of a number represented as a string."""
        result = "1"
        for i in range(2, int(n) + 1):
            result = self.multiply(result, str(i))
        return result

    def repl(self):
        """Starts a REPL for the calculator."""
        print("Arbitrary Precision Calculator")
        print("Type 'exit' or 'quit' to leave the REPL.")
        while True:
            try:
                expr = input(">> ").strip()
                if expr.lower() in ('exit', 'quit'):
                    break
                # Very basic parsing: split by whitespace
                parts = expr.split()
                if len(parts) == 3:
                    a, op, b = parts
                    if op == '+':
                        print(self.add(a, b))
                    elif op == '-':
                        print(self.subtract(a, b))
                    elif op == '*':
                        print(self.multiply(a, b))
                    elif op == '/':
                        print(self.divide(a, b))
                    elif op == '%':
                        print(self.modulo(a, b))
                    elif op == '^':
                        print(self.exponentiate(a, b))
                elif len(parts) == 2 and parts[0] == 'fact':
                    print(self.factorial(parts[1]))
                else:
                    print("Invalid input!")
            except Exception as e:
                print(f"Error: {e}")

# Run the calculator
if __name__ == "__main__":
    calc = ArbitraryPrecisionCalculator()
    calc.repl()
