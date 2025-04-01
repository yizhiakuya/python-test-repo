class Calculator:
    """
    简单的计算器类，用于演示
    """
    def add(self, a, b):
        """加法"""
        return a + b
        
    def subtract(self, a, b):
        """减法"""
        return a - b
        
    def multiply(self, a, b):
        """乘法"""
        return a * b
        
    def divide(self, a, b):
        """除法"""
        if b == 0:
            raise ValueError("除数不能为零")
        return a / b

if __name__ == "__main__":
    calc = Calculator()
    print(f"1 + 2 = {calc.add(1, 2)}")
    print(f"5 - 3 = {calc.subtract(5, 3)}")
    print(f"4 * 6 = {calc.multiply(4, 6)}")
    print(f"8 / 2 = {calc.divide(8, 2)}")