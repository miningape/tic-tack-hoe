from text_box import menuBox

class menu:
    def __init__(self):
        self.game_running = False
        self.current_menu = 1
        self.boxes = []
        
    def winner(self, who):
        self.winState = "{0} was the winner!".format(who)
        
    def reset(self, width, height):
        self.boxes = []
        self.boxes.append(menuBox(width/2, height/2 - 50, 100, 50, self.winState, 1, False))
        self.boxes.append(menuBox(width/2, height/2, 100, 50, "Menu", 1))
        
    def mainMenu(self, width, height):
        self.boxes = []
        self.boxes.append(menuBox(width/2, height/2, 100, 50, "Play", 0))
        self.boxes.append(menuBox(width/2, height/2 + 75, 200, 50, "Options", 2))
        
    def options(self, width, height):
        self.boxes = []
        self.boxes.append(menuBox(width/2, height/2, 200, 50, "width:" + str(width), 2))
        self.boxes.append(menuBox(width/2 - 200, height/2, 50, 50, "<", 2.1))
        self.boxes.append(menuBox(width/2 + 200, height/2, 50, 50, ">", 2.2))
        self.boxes.append(menuBox(width/2, height/2 + 75, 200, 50, "height: "+ str(height), 2))
        self.boxes.append(menuBox(width/2 - 200, height/2 + 75, 50, 50, "<", 2.3))
        self.boxes.append(menuBox(width/2 + 200, height/2 + 75, 50, 50, ">", 2.4))
        self.boxes.append(menuBox(width/2, height/2 + 150, 200, 50, "Back", 1))
    
    def show(self):
        for i in range(len(self.boxes)):
            self.boxes[i].show()
        
    def localdelay(self, ms):
        time = millis()
        while (millis() - time < ms):
            pass
        
    def input(self):
        self.current_menu = floor(self.current_menu)
        
        if (mousePressed == True):
            for i in range(len(self.boxes)):
                if (self.boxes[i].clicked()):
                    self.current_menu = self.boxes[i].dothis
                    self.localdelay(300)
                    
        return self.current_menu
    
    
    def manualMenu(self, menuChoice):
        self.current_menu = menuChoice
    
