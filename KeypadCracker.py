import inventory
from inventory.Item import FixtureSpec

class KeypadCracker(FixtureSpec):

    def __init__(self):
        super().__init__()

    def use(self):
        try:
            print(f"KEYPAD CODE: {self.first_half()}{self.second_half()}")
        except NameError:
            print("Looks like calculation is missing a digit.")
        except Exception as err:
            print(f"Looks like something else is wrong. Here's the error:\n{err}")
  
    def first_half(self, first_digit: int = 0, second_digit: int = 0) -> str:

        ###################################################
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        #Prompt user to enter a number (1-12) from the keyboard
        user_prompt = input("Enter a number between 1 and 12: ")
        print(user_prompt)
        #Convert birth_month to integer; store as birth_month_number
        birth_month_number = int(birth_month)

        # TODO: Create separate variable to keep track of alterations to 
        #       birth_month_number -- we need the original for the final
        #       calculation!
        store_birth_month_number = birth_month_number
        # TODO: Multiply our running_number by 3
        calculation = running_number / 3
        # TODO: Add 6 to our running_number
        calculation =+ 6

        # TODO: Divide running_number by 3

        # TODO: Substract birth_month_number FROM running_number, store
        #       as a separate variable to input into the keypad

        # TODO: To derive the second digit, subtract 1 from the first digit
        
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        ###################################################

        return f"{first_digit}{second_digit}"

    def second_half(self, third_digit: int = 0, fourth_digit: int = 0) -> str:

        ###################################################
        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        # TODO: Prompt user to enter a number (1-31) from the keyboard
    
        # TODO: Convert birthday to integer; store as birth_day_number

        # TODO: Create separate variable to keep track of alterations to 
        #       birth_day_number -- we need the original for the final
        #       calculation!

        # TODO: Add 1 to running_number

        # TODO: Mulitiply running_number by 2 (doubling it)

        # TODO: Add 4 to running_number

        # TODO: Divide running_number by 2

        # TODO: Subtract birth_day_number from running_number

        # TODO: Set aside the current value of running_number as the
        #       third_digit of the code

        # TODO: Multiply running_number by 2 (double it)

        # TODO: Add 3 to running_number

        ## WORK HERE -- MATCH INDENTATION LEVEL OF THIS COMMENT
        ###################################################

        fourth_digit = running_number % 5
        return f"{third_digit}{fourth_digit}"

def main():
    obj = KeypadCracker()
    obj.use()

if __name__ == "__main__":
    main()
