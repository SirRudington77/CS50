def shorterTweets():
    # user input and inital values
    usersTweet = input("What is your tweet?: ")
    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    newTweet = ""
    # reviece the input, check through the list
    for tweet in usersTweet:
        # if the letters are not in the list of vowels, put into new string
        if tweet not in vowels:
            newTweet += tweet
    # returns the shorten tweet
    print(newTweet)

shorterTweets()