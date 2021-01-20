#Robot
#01/21
#Brayden Woodard

class Robot:
    name = "mr.roboto"
    thank_you = "domo arigato"

    def thanks():
        print(Robot.thank_you + ", " + Robot.name)




Robot.thanks()
Robot.thank_you = "thankee kindly"
Robot.name = "T-1000"
Robot.thanks()