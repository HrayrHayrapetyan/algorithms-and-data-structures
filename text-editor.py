from Stack import Stack
class TextEditor:
    def __init__(self):
        self.undo=Stack()
        self.redo=Stack()
        self.text=''
    def type_Char(self,value):
        self.undo.push(self.text)
        self.text+=value
        while not self.redo.isEmpty():
            self.redo.pop()

    def Undo(self):
        if not self.undo.isEmpty():
            self.redo.push(self.text)
            self.text=self.undo.pop()
    def Redo(self):
        if not self.redo.isEmpty():
            self.undo.push(self.text)
            self.text=self.redo.pop()
    def view_Text(self):
        print(self.text)
        print()

if __name__=='__main__':
    te=TextEditor()
    te.type_Char('Remember to Buy Groceries ')
    te.type_Char('Meeting at 10:00 ')
    te.type_Char('Meet Bob at 7 ')
    te.view_Text()
    te.Undo()
    te.Undo()
    te.view_Text()
    te.Redo()
    te.Redo()
    te.view_Text()
