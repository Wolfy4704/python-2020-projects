#Best freinds
#1/21
#Brayden Woodard

class Bestie:
    num_messages = 0

    def chat(input):
        Bestie.num_messages = Bestie.num_messages + 1
        if (Bestie.num_messages > 3):
            print("Im too tired")
            return

        input = str.lower(input)

        if "ride" in input:
            print("sure ill give you a ride")
        elif "call" in input:
            print("ill call you later")
        else:
            print("you are a mystery to me")