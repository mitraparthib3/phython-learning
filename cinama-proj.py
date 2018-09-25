flims = {
    "finding dory": [3, 5],
    "scoobydoo": [3, 10],
    "tarzan": [10, 5],
    "MIB": [10, 2]
};

while 1 == 1:
    whatMovie = input("Hello there!, thanks for chossing your cinama, what would you like to watch today? :").strip();
    if whatMovie in flims:
        userAge = int(input("great choice, lets see how old are you:").strip());
        if (userAge >= flims[whatMovie][0]) and (flims[whatMovie][1] >= 1):
            print("you can watch it!")
            transactionApproval = input("Do want to buy a ticket of this movie, type yes or no?").strip().lower()
            if transactionApproval == 'yes':
                flims[whatMovie][1] = flims[whatMovie][1] - 1;
                print('your ticket is booked')
                print(flims);
            else:
                print("its alright, you can choose another movie")
        else:
            print("sorry you cannot watch this movie :(")
    else:
        print("Opps! looks like we dont have the movie yet!")
