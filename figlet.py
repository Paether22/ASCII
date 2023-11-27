import sys
from pyfiglet import Figlet
import random

def main():
    #decrlaring f to use the Figlet module
    f = Figlet()
    fonts = f.getFonts()

    #without terminal arguments print the text in a random style
    if len(sys.argv) == 1:
        i = input("Input: ")
        f.setFont(font=random.choice(fonts))
        print("Output:",f.renderText(i), sep="\n")

    #print the text with a choosen style
    elif len(sys.argv) == 3:
        if sys.argv[1] in ['-f','--font'] and sys.argv[2] in fonts:
            i = input("Input: ")
            f.setFont(font=sys.argv[2])
            print("Output:",f.renderText(i), sep="\n")
        else:
            sys.exit("Invalid usage")
    else:
        sys.exit("Invalid usage")

if __name__ == "__main__":
    main()
