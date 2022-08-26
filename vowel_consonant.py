def vowel_consonant(c):
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        print("\nIt is a Vowel")
    elif c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
        print("\nIt is a Vowel")
    else:
        print("\nIt is a Consonant")

if __name__=='__main__':
    c=int(input("Enter the Character: "))
    vowel_consonant(c)



