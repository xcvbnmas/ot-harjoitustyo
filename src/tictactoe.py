import tkinter as tk

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Ristinolla")        
        self.root.resizable(False, False)
        self.buttons = self.create_grid()

    def create_grid(self):
        buttons = []
        for i in range(3):               
            row = []            
            for j in range(3):
                button = tk.Button(self.root, font=('Arial', 20), width=10, height=5, command=lambda i=i, j=j: self.on_click(i, j))
                button.grid(row=i, column=j, sticky='nsew')
                row.append(button)
                           
            buttons.append(row)
            
            self.root.grid_rowconfigure(i, minsize=50)
            self.root.grid_columnconfigure(j, minsize=50)         
            
        return buttons
            

if __name__ == "__main__":
    root = tk.Tk()    
    game = TicTacToe(root)
    root.mainloop()
                   
