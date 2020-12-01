def change_rations(rations):
    print("your current rations are", rations)
    options = ["full", "half","quarter"]
    while true:
        user = input("What are your rations? full, half, or quarter.")
        
        if user == "quarter":
            return "quarter"
        elif user == "half":
            return half
        else:
            return full 
