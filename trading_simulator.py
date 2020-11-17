import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import pandas.tseries.offsets as offsets
        
class Simulator:
    def __init__(self, s_time, e_time):
        self.s_time = np.datetime64(s_time + 'T00:00:00.000000000') # シミュレータ開始時間
        self.e_time = np.datetime64(e_time + 'T00:00:00.000000000') # シミュレータ終了時間
        self.t      = self.s_time                                   # シミュレータ現在時刻
        
        self.ticker = yf.Ticker("6472.T") #NTN
        self.hist = self.ticker.history(period="max")[self.s_time:self.e_time]
        
        self.stock_price_t = 'None' # 株価
        
    def next_day(self):
        self.t = offsets.Day(1).apply(self.t)
        price = list(self.hist['Close'].loc[self.hist.index.values == np.datetime64(self.t)])
        
        if len(price) > 0:
            self.stock_price_t = price[0]
        else:
            self.stock_price_t = 'None'

if __name__ == "__main__":
    def print_hist(objct):
        print(objct.hist)
        print(type(objct.hist))
        print(objct.hist.dtypes)
        print(type(objct.hist.index.values))
    
    def plot(objct):
        plt.cla()
        hist = objct.hist[objct.s_time:objct.t]
        x = hist.index.values
        y = list(hist['Close'])
        
        # plt.ylim(200, 360)
        plt.xlim(objct.hist.index.values[0], objct.hist.index.values[-1])
        plt.title('NTN (6472)')
        plt.gcf().autofmt_xdate()
        plt.grid()
        plt.plot(x, y)
    
    s_time = '2020-01-11'
    e_time = '2020-11-11'
    
    sim = Simulator(s_time, e_time)
    sim.next_day()
    plot(sim)
    
    # print_hist(sim)
    