class Agent:
    def __init__(self):
        self.action = 'WAIT' # 行動
        self.volume = 0      # 買（売）株式数
    
    def make_decision(self, price, buy_pw, hold, date):
        if price < 200:
            self.action = 'BUY'
            self.volume = 300
        elif price > 225:
            self.action = 'SELL'
            self.volume = 300
        else:
            self.action = 'WAIT'
            self.volume = 0