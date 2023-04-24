import menu
class TheShop:
    def __init__(self, pointsMulti = 1, DP = False):
        self.pointsMulti = pointsMulti
        self.DP = DP

    def open_shop(self):
        shop_menuz = menu.PygameMenu(["Double Points: 25", "--", "Back"])
        selected_option = shop_menuz.run()

        if selected_option == "Double Points: 25":
            self.pointsMulti = 2
            self.DP = True
            print(self.DP)
            return -1
        else:
            return 1

    def multiply(self):
        if self.DP == True:
            print(self.DP)
            return 2
        else:
            print(self.DP)
            return 1
        

