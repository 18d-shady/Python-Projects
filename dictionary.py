#dictionary that allows users to store keys and values
d = {}

def get_values():
    #input key
    keyInput = input('write a new word: ')
    keys = d.keys()
    #to check if the file already exist
    if keyInput in keys:
        overwrite = input('This word already exist. Overwrite? yes or no: ')
        if overwrite.lower() == 'yes':
            # input value
            valInput = input('write the definition: ')
            d[keyInput] = valInput
        elif overwrite.lower() == 'no':
            get_values()
    else:
        #input value
        valInput = input('write the definition: ')
        d[keyInput] = valInput
            
def ask_dict():
    #ask to view the whole dictionary
    askDict = input('View ur dictionary? yes or no: ')
    if askDict.lower() == 'yes':
        print(d)
        #to add another word or exist
        add_or_exit = input('Add another word? view? or close? ')
        if add_or_exit.lower() == 'add':
            user_dictionary()
        elif add_or_exit.lower() == 'close':
            exit(user_dictionary)
        else:
            # ask the user to view the recent word input
            ask = input('Do u want to view any word? yes or no: ')
            if ask.lower() == 'yes':
                choice = input('type the word: ')
                print(d[choice.lower()])
                ask_dict()
            elif ask.lower() == 'no':
                ask_dict()

    elif askDict == 'no':
        viewWords = input('view ur dictionary words? yes or no: ')
        if viewWords.lower() == 'yes':
            keys = d.keys()
            print(k)
        elif viewWords.lower() == 'no':
            add_or_exit = input('Add another word? view? or close? ')
            if add_or_exit.lower() == 'add':
                user_dictionary()
            elif add_or_exit.lower() == 'close':
                exit(user_dictionary)
            else:
                # ask the user to view the recent word input
                ask = input('Do u want to view any word? yes or no: ')
                if ask.lower() == 'yes':
                    choice = input('type the word: ')
                    print(d[choice.lower()])
                    ask_dict()
                elif ask.lower() == 'no':
                    ask_dict()
        
def user_dictionary():
    get_values()
    add_or_exit = input('Add another word? view? or close? ')
    if add_or_exit.lower() == 'add':
        user_dictionary()
    elif add_or_exit.lower() == 'close':
        exit(user_dictionary)
    else:
        # ask the user to view the recent word input
        ask = input('Do u want to view any word? yes or no: ')
        if ask.lower() == 'yes':
            choice = input('type the word: ')
            print(d[choice.lower()])
            ask_dict()
        elif ask.lower() == 'no':
            ask_dict()


if __name__ == '__main__':
    user_dictionary()
