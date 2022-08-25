num=int(input("Enter any number:"))
divisor=int(input("Enter the divisor"))
def quotient_rem(num,divisor):
    return (num//divisor,num%divisor)
if __name__=='__main__':
    print(quotient_rem(num,divisor))

