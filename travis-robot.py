known_user = ["Alice", "Bob", "Claire", "Dan"]

while True:
    print("Hi my name is Travis");
    name=input("What is your name ? :").strip().capitalize();
    if name in known_user: #in method finds and returns bollean
        print("Hello {}! Come on in!".format(name));
        print("Lets remove your RSVP!")
        known_user.remove(name)
    else:
        print("Oops! I didnot find you")
        add_me = input("WOuld you like me to add you ? :").lower()
        if add_me == 'y':
            your_name = input("What is your name ? :").strip().capitalize();
            known_user.append(your_name)
            print("You are on board {}".format(your_name));
        
