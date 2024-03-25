from tkinter import*
import random as r 
root = Tk()
root.title("Colour Randomizer")
root.geometry("600x600")


cn = Label(root, font= "Ariel")
cn.place(relx = 0.5, rely= 0.5, anchor = CENTER)

sl = Label(root, text ="Score :  ")
sl.place(relx= 0.3, rely = 0.2, anchor = CENTER)

input_value = Entry(root)
input_value.place(relx = 0.5, rely = 0.65, anchor = CENTER)

class Game:
    
    def __init__(self):
        self.__score = 0
        
    def UpdateGame(self):
        self.text = ["RED", "BLUE", "GREEN", "PINK", "BLACK", "YELLOW"]
        self.random_number_for_text = r.randint(0, 5)
        self.colour = ["red", "blue", "green", "pink", "black", "yellow"]
        self.random_number_for_colour = r.randint(0, 5)
        cn["text"]= self.text[self.random_number_for_text]
        cn["fg"]= self.colour[self.random_number_for_colour]
    
    def __Update_score(self, input_value):
        if(input_value == self.colour[self.random_number_for_colour]):
            self.__score = self.__score + r.randint(0,10)
            sl["text"] = "Score : " + str(self.__score)
            
    def get_user_value(self, input_value):
        self.__Update_score()


def getInput():
    value = input_value.get()   
    input_value.delete(0, END)      
        
        
    
        
        
obj1 = Game()
obj1.get_user_value(value)
obj1.UpdateGame()

b1 = Button(root, text="Start", command = "UpdateGame", bg= "yellow")
b1.place(relx = 0.5, rely = 0.8, anchor= CENTER)
root.mainloop()