import menu
from shared_stats import my_instance

class TheShop:
    def __init__(self, pointsSub = 0, DP = False):
        self.pointsMulti = pointsSub
        self.DP = DP

    def open_shop(self):
        shop_menuz = menu.PygameMenu(["Double Points: 25", "--", "Back"])
        selected_option = shop_menuz.run()

        if selected_option == "Double Points: 25":
            self.my_stats = my_instance
            self.pts = self.my_stats.POINTS
            #pts = int(pts)
            if self.pts >= 25:
                self.DP = True
                return -1
            else:
                print("not enough funds")
                #print(self.pts)
                return 1
        else:
            return 1

    def multiply(self):
        if self.DP == True:
            return 2
        else:
            return 1
        