class menuBox:
    def __init__(self, x, y, box_wid, box_hei, displayText, thisfunction, showBorder = True):
        self.xPos = x
        self.yPos = y
        self.box_wid = box_wid
        self.box_hei = box_hei
        self.displayText = displayText
        self.dothis = thisfunction
        self.showBorder = showBorder
    
    def show(self):
        rectMode(CENTER)
        #textMode(CENTER)
        textAlign(CENTER)
        textSize(36)
        
        if (self.showBorder == False):
            noStroke()
        else:
            stroke(0)
        
        # Commands to display
        fill('#FFFFFF')
        rect(self.xPos, self.yPos, self.box_wid, self.box_hei)
        
        fill('#FF0000')
        text(self.displayText, self.xPos, self.yPos + 15)
    
    def clicked(self):
        box_clicked = False
        # If statements to detect a click of the box
        if (mouseX <= self.xPos+(self.box_wid/2) and mouseX >= self.xPos-(self.box_wid/2)):
            if (mouseY <= self.yPos+(self.box_hei/2) and mouseY >= self.yPos-(self.box_hei/2)):
                box_clicked = True
                
        return box_clicked
