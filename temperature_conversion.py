class color:
        bold = '\033[01m'
        blue = '\033[34'
        gold = '\033[33m'
        red = '\033[31m'
        green = '\033[32m'
        cyan = '\033[36m'
        darkgrey = '\033[90m'
def temperature_converter():
        print(color.bold ,color.green,"This Programme Is For Temperature Conversion.\n|For Celcius To Farenheit Type 1:\n|For Farenheit To Celcius Type 2:\n|For Celcius To Kelvin Type 3:\n|For Kelvin To Celcius Type 4:\n|For Farenheit To Kelvin Type 5:\n|For Kelvin To Farenheit Type 6:")
        print("Enter Your Key: ")
        user_input = int(input())
        if user_input == 1:
                user_input1 = float(input("Enter Celcius Temperature: "))
                print(color.cyan,"Your Temperature In Farenheit Is: ", ((user_input1*9)/5)+32)
        elif user_input == 2:
                user_input2 = float(input("Enter Farenheit Temperature: "))
                print(color.cyan,"Your Temperature In Celcius Is: ", ((user_input2-32)*5)/9)
        elif user_input == 3:
                user_input3 = float(input("Enter Celcius Temperature: "))
                print(color.cyan,"Your Temperature In Kelvin Is: ", (user_input3+273))
        elif user_input == 4:
                user_input4 = float(input("Enter Kelvin Temperature: "))
                print(color.cyan,"Your Temperature In Celcius Is: ", ((user_input4-273)))
        elif user_input == 5:
                user_input5 = float(input(("Enter Farenheit Temperatute: ")))    
                print(color.cyan,"Your Temperature In Kelvin Is: ", user_input5+241)
        elif user_input == 6:
                user_input5 = float(input(("Enter Kelvin Temperatute: ")))    
                print(color.cyan,"Your Temperature In Farenheit Is: ", user_input5-241)
        else:
                print(color.red,"You Choose Invalid Key!")
        again()
def again():
        print(color.darkgrey,"Are You Want to Run Again! Type \'Y\' for Yes and \'N\' for No: ")
        user_input = input().upper()
        # user_input = input("Are You Want to Run Again! Type \'Y\' for Yes and \'N\' for No: ").upper()
        if user_input == 'Y':
                temperature_converter()
        elif user_input == 'N':
                print("See You Next Time!!!!")
        else:
                again()
temperature_converter()