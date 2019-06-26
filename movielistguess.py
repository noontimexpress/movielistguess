movielist = []

firstmovie = input("Enter a movie: ")
movielist.append(firstmovie)
secondmovie = input("Please enter another movie: ")
movielist.append(secondmovie)

like = int(input("Which one do you like better? " + firstmovie + " or " + secondmovie + "? " + "Please press 1 or 2: "))

if like != 1:
    movielist.reverse()


def sortme():
    x = 1
    print(movielist)
    newmovies = input("Please enter another movie: ")
    compare = int(input("Which one do you like better? " + newmovies + " or " + movielist[0] + "? " + "Please press 1 or 2: "))
    if compare == 1:
        movielist.insert(0,newmovies)
        print(movielist)
        sortme()
    else:
        def recursive(x):
            compare = int(input("Which one do you like better? " + newmovies + " or " + movielist[x] + "? " + "Please press 1 or 2: "))
            if compare == 1:
                movielist.insert(x, newmovies)
                print(movielist)
                sortme()
            else: 
                print(movielist)
                if x == len(movielist) - 1:
                    movielist.append(newmovies)
                    sortme()
                else:
                    x = x + 1               
                    recursive(x)
        recursive(x)

sortme()




