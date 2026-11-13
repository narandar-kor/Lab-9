class Calculator():
    def __init__(self,num1,num2):
        self.num1 = num1
        self.num2 = num2
    def Addition(self):
        sum=self.num1+self.num2
        print(f"The Sum of both numbers is -> {sum}")
    def Subtraction(self):
        subtract = self.num1-self.num2
        print(f"The Subtraction of both numbers is -> {subtract}")
    def Multiplication(self):
        multiply = self.num1*self.num2
        print(f"The Multiplication of both numbers is -> {multiply}")
    def Division(self):
        divide = self.num1/self.num2
        print(f"The Division of both numbers is -> {divide}")

object1 = Calculator(9,7)

object1.Addition()
object1.Subtraction()
object1.Division()
object1.Multiplication()
