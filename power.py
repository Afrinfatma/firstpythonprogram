def power_of_two(tot,param2,param3):
    try:
        print(tot,param2,param3)
        for i in range(tot):
            print("2 raised to the power ", i, " is ", 2 ** i)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    num = int(input("Enter the Total Number of Terms: "))
    power_of_two(param2=6,param3=3,tot=num)
