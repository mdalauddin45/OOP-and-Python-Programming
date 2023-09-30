class Calculator:
    brand = 'Casio MS990'
    def add(self, num1,num2):
        return num1+num2
    def sub(self, num1,num2):
        return num1-num2
    def mul(self, num1,num2):
        return num1*num2
    def div(self, num1,num2):
        return num1/num2
    
    
my_calculator = Calculator()
print(my_calculator.add(10,2))
print(my_calculator.sub(10,2))
print(my_calculator.mul(10,2))
print(my_calculator.div(10,2))