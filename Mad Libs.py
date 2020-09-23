#Brayden woodard
#9/20
#Mad Lib

noun1 = input("Enter a noun.\n") #0
pronoun1 = input("Enter a pronoun.\n") #1
noun2 = input("Enter another noun. \n") #2
emotion1 = input("Enter an emotion ending in ful.\n") #3 
action1 = input("Enter an action.\n") #4
object1 = input("Enter an object.\n") #5
noun3 = input("Enter a noun.\n") #6
adjective1 = input("Enter an adjective.\n") #7
noun4 = input("Enter a plural noun.\n") #8
emotion2 = input("Enter a emotion ending in ful.\n") #9
sound1 = input("Enter a sound affect.\n") #10
song1 = input("Enter a song name.\n") #11

madlib = str.format("""Once upon a time there was a lovely
                         {0}. But {1} had an {2}
                         upon {1} of a {3} sort which could 
                         only be broken by love's first {4} 
                         {1} was locked away in a castle guarded 
                         by a terrible {5}-breathing {6}. 
                         Many {7} {8} had attempted to 
                         free {1} from this {9} prison, 
                         but non prevailed. {1} waited in the 
                         dragon's keep in the highest room of 
                         the tallest tower for {1} true love 
                         and true love's first {4}. (laughs) 
                         Like that's ever gonna happen. What 
                         a load of - ({10})
 
               {11}- played by Smashmouth begins to play. Shrek goes about his 
               day. While in a nearby town, the villagers get together to go 
               after the ogre.""", noun1, pronoun1, noun2, emotion1, action1, object1, noun3, adjective1, noun4, emotion2, sound1, song1)
print(madlib)
