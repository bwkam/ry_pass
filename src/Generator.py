import random
import string

class Generator:

    SYMBOLS = ["!", "?", "#", "@", "(", ")", "*", "%", "^", "_", "+", "-", "~", "`"]

    def __init__(self, length=10):
        self.length = length


    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length >= 10 and length <= 100:
            self._length = length
            return True
        else:
            raise ValueError("Length error")

    
    def generate(self):
        
        # Start generating random letters
        random_letters = []
        random.seed(5)

        for _ in range(self.length):
            case = random.choice(["upper", "lower"])
            random_letter = random.choice(string.ascii_letters)

            if case == "upper":
                random_letter = random_letter.upper()
            else:
                random_letter = random_letter.lower()

            random_letters.append(random_letter) 

        # Start generating random symbols
        random_symbols = []
        random.seed(9)

        for _ in range(self.length):
            random_symbol = random.choice(Generator.SYMBOLS)
            random_symbols.append(random_symbol)

        # Start generating random integers
        random_ints = []
        random.seed(3)

        for _ in range(self.length):
            random_int = random.randint(0, 9)
            random_ints.append(random_int)
        

        # Start generating the REAL password
        new_pass = ""

        random.seed(random.random)

        for _ in range(self.length):
            choice = random.choice(["letter", "symbol", "int"])

            if choice == "letter":
                new_pass += random.choice(random_letters)
            elif choice == "int":
                new_pass += str(random.choice(random_ints))
            else:
                new_pass += random.choice(random_symbols)

        return new_pass
                
            

    # Instead of using the native constructor, use a function
    @classmethod
    def init(cls):
        length = int(input("Password length: "))
        return cls(length)
    