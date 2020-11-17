import matplotlib.pyplot as plt
from agent import Agent
from trading_simulator import Simulator

def plot(objct):
    plt.cla()
    hist = objct.hist[objct.s_time:objct.t]
    x = hist.index.values
    y = list(hist['Close'])
    
    plt.xlim(objct.hist.index.values[0], objct.hist.index.values[-1])
    plt.title('NTN (6472)')
    plt.gcf().autofmt_xdate()
    plt.grid()
    plt.plot(x, y)

def print_result(obj, bpw, hold):
    print(obj.t.strftime("%Y-%m-%d"), 
          '{:<5}'.format(str(obj.stock_price_t)), 
          f'Agent: (BuyPower, Stock)=({bpw:.0f}, {hold})')
    
if __name__ == "__main__":
    s_time = '2020-01-11' # 取引開始日
    e_time = '2020-11-11' # 取引終了日
    sim = Simulator(s_time, e_time) # シミュレーター生成
    agent = Agent()                 # エージェント生成
    
    buy_pw_agent        = 100000 # 買い付け余力
    stockholdings_agent = 0      # 保有株式数
    
    while(sim.e_time > sim.t):
        sim.next_day()
        date = sim.t.strftime("%Y-%m-%d")
        price = sim.stock_price_t
        if price != 'None': # 土日，祝日はスキップ
            # エージェントの意思決定
            agent.make_decision(price, 
                                buy_pw_agent, 
                                stockholdings_agent,
                                date)
            # 取引
            if agent.action == 'BUY':
                tmp_bp = buy_pw_agent - agent.volume * price
                tmp_sh = stockholdings_agent + agent.volume
                if tmp_bp > 0 and tmp_sh > 0:
                    buy_pw_agent = tmp_bp
                    stockholdings_agent = tmp_sh
                
            elif agent.action == 'SELL':
                tmp_bp = buy_pw_agent + agent.volume * price
                tmp_sh = stockholdings_agent - agent.volume
                if tmp_bp > 0 and tmp_sh > 0:
                    buy_pw_agent = tmp_bp
                    stockholdings_agent = tmp_sh
                
            else:
                pass
        
        print_result(sim, buy_pw_agent, stockholdings_agent)
    
    outcome = buy_pw_agent + stockholdings_agent * price
    print('Result:', f'{outcome:.0f}yen')
    plot(sim)
    
    