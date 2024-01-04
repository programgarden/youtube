import FinanceDataReader as fdr
import talib

# 누적 수익률
cumulative_earing_rate = 0.0
# 현재 보유 주식의 구매 가격
cur_buy_price = 0

# 종목 코드들 가져오기
def get_codes():
    stocks = fdr.StockListing("KRX")
    codes = stocks['Code'].tolist()
    return codes

# 모든 종목의 종가 가져오기
def get_close_prices(codes):
    for code in codes:
        period_prices = fdr.DataReader(code, start="2015", end="2022")
        closes = period_prices["Close"].dropna()
        
        # closes가 비어있지 않으면 처리
        if not closes.empty:
            cross_buy_sell(code, closes)
        else:
            print(f"Code {code} has all NaN data. Skipping...")
        
# 이동평균선 골든크로스이면 매수, 데드크로스이면 매도 구하기
def cross_buy_sell(code, closes):
    global cumulative_earing_rate, cur_buy_price

    short_ma = talib.SMA(closes, timeperiod=120)
    long_ma = talib.SMA(closes, timeperiod=240)
    
    # shift로 전날에는 골든크로스 직전이었는지 확인한다.
    buy = (short_ma > long_ma) & (short_ma.shift(1) <= long_ma.shift(1))
    sell = (short_ma < long_ma) & (short_ma.shift(1) >= long_ma.shift(1))
    
    for date in buy.index:
        if buy[date]:
            cur_buy_price = closes[date]
            print(f"Date: {date}, Code: {code}, buy: {cur_buy_price}, Action: Buy")
        elif sell[date]:
            sell_price = closes[date]
            
            if(cur_buy_price > 0):
                rate = earn_rate(cur_buy_price, sell_price)
                cumulative_earing_rate += round(rate, 2) - 5  # 수익률 누적
                cur_buy_price = 0
                
            print(f"Date: {date}, Code: {code}, sell: {sell_price}, Action: Sell")
    
    cur_buy_price = 0
        
        
# 세금과 수수료 제외한 단순한 수익률 공식
def earn_rate(buy_price, sell_price):
    return ((sell_price - buy_price) / buy_price) * 100

codes = get_codes()
get_close_prices(codes)

print(f"코스피, 코스닥 전체: {len(codes)}개, 수익률 누적: {round(cumulative_earing_rate, 2)}")
