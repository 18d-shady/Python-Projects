word_list = ["proud", "angry", "fire", "redraw", "unbelivable", "seafood", "schooling", "writing", "imprint", "planet", "control", "charger", "light", "line", "fly"]
print(word_list)

while(True):
    print("""
okay, then guess the word with this random letters:""")
    import random
    pi = random.choice(word_list)
    p = random.sample(pi,3)
    print(p)

    ss = input("guess the word: " )

    print(bool(pi == ss))
     

