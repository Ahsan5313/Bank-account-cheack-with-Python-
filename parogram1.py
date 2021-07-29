class Account():
    def __init__(self, owener, blance):
        self.owener = owener
        self.blance = blance

    def deposite(self, myDesposite):
        self.blance = self.blance + myDesposite
        print(f" my deposite {self.blance}")

    def widthDraw(self, draw):
        if self.blance >= draw:
            self.blance = self.blance - draw
            print(f'You have widthDraw {draw} form your account')
            print(f"My current blance is {self.blance}")




My_obj = Account('Ahsan', 1000)
My_obj.deposite(5000)
My_obj.widthDraw(2000)
