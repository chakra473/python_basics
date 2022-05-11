# importing random module to generate random coupon numbers
import random
class Coupon:
    def __init__(self,n,d):
        """
        :param n: number of distinct coupon number
        :param d: digits of distinct coupon number
        """
        self.n = n
        self.d = d


    def select_digits(self):
        """
        this function logic is to assign how many random coupon digits we need to generate
        :return: start value and end value to specify the range in random int method
        """
        if self.d == 5:
            a = 10000
            b = 99999
            return a,b
        elif self.d == 6:
            a = 100000
            b = 999999
            return a,b
        elif self.d == 7:
            a = 1000000
            b = 9999999
            return a,b
        elif self.d == 8:
            a = 10000000
            b = 99999999
            return a,b
        elif self.d == 9:
            a = 100000000
            b = 999999999
            return a,b
        elif self.d == 10:
            a = 1000000000
            b = 9999999999
            return a,b
        elif self.d == 2:
            a = 10
            b = 18
            return a,b
        raise ValueError("invalid number")


    def generate_coupon(self):
        """
        this function generates distinct coupon numbers
        :return: list of total distinct coupon numbers and total random number needed to have all distinct numbers
        """
        try:
            coupon_list=[]
            c,d=self.select_digits()
            i = 0
            j = 0
            while i < self.n:
                coupon_generator=random.randint(c,d+1)
                if not coupon_list.__contains__((coupon_generator)):#only enter the condition if list does not contains values of random number i.e.only new number enters to the list;
                    coupon_list.append(int(coupon_generator))#adds the random number to the list
                    i +=1
                else:
                    j +=1
            total = i + j#counts total random number needed to have all distinct numbers
            print_total =f" total random number needed to have all distinct numbers ={total}"
            return print_total +"\n"+ str(coupon_list)
        except ValueError as err:
            print(err)



if __name__ == "__main__":
    num = int(input("enter how many random numbers do you need to generate distinct coupon number: "))
    digits = int(input("enter how many digits you need to generate distinct coupon number: "))
    coupon = Coupon(num,digits)#creating object of the class Coupon
    print(coupon.generate_coupon())#calling the generate_coupon method/function
