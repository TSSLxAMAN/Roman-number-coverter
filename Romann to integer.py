def format_checker(roman_number):
    correct = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for i in roman_number:
        if i.upper() not in correct:
            return False
    return True        

def R2I_converter(roman_number):
    sum = 0
    notations = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}    
    prev_value = 0
    for i in reversed(roman_number):
        value = notations.get(i, 0)
        if value < prev_value:
            sum = sum - value
        else:
            sum = sum + value
        prev_value = value 
    return sum
    

print('''Welcome to the Romam number converter ''')
while True:
    roman_number = input("Enter the Roman Number : ")
    re = format_checker(roman_number)
    if re == True:
        result_value = R2I_converter(roman_number.upper())
        print(result_value)
    else:
        print("Invalid Input (the entered value is not roman number)")

