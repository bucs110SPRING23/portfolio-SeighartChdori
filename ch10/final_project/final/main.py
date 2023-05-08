from random_quotes import Random_quotes
from random_facts import Random_facts

def main() :
    """
    Initialzes all other classes along with calling them
    arguments: None
    return: Quote or Fact
    """
    running = True
    while running :
        answer = int(input("Hello!\nWould you like to hear a random fact or a random quote?\nEnter either 0 for fact or 1 for quote or 2 for no thanks\n"))
        if answer == 0 :
            while running :
                print(Random_facts().__str__()['text'])
                answer = str(input("Would you like another? yes or no\n"))
                if answer == "yes" :
                    running = True
                elif answer == "no" :
                    running = False
        elif answer == 1 :
            while running :
                print(Random_quotes().__str__()['quote'] + " - " +Random_quotes().__str__()['character'])
                answer = str(input("Would you like another? yes or no\n"))
                if answer == "yes" :
                    running = True
                elif answer == "no" :
                    running = False
        elif answer == 2 :
            running = False

    if running == False :
        print("Understood! Have a great rest of your day!")

main()