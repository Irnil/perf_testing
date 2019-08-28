import os, sys, requests, time
from influxdb import InfluxDBClient

sys.getfilesystemencoding()
'UTF-8'


print('\nПрограмма для записи и мониторинга криптовалютных пар с помощью Influxdb и Graphana.')
print('Записи берутся с площадки Bitfinex.')
print('made by Nikita Rulenko\n')

#------------------------------------CONFIG---------------------------------------------------------
dbname = 'testbtdb'
client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)
client.create_database(dbname)
check = client.get_list_database()
print('Список баз данных: ' + str(check) + '\n')
client.switch_database(dbname)
pairs = ['btcusd', 'ethusd', 'xrpusd', 'ltcusd', 'xmrusd', 'eosusd', 'etcusd', 'omgusd', 'leousd', 'neousd']

#-----------------------------------MAIN_BLOCK-------------------------------------------------------
if __name__ == '__main__':    
    
    while 1:
        try:

            for i in pairs:
                url = "https://api.bitfinex.com/v1/pubticker/" + i
                response = requests.request("GET", url)
                mid, bid, ask, last_price, low, high, volume, timestamp = response.text.split(',')
                            
                mid = mid.split(':')[1] #takes second elem of split
                mid = mid[1:-1]         #removes first ad last symbol
                            
                bid = bid.split(':')[1]
                bid = bid[1:-1]
                            
                ask = ask.split(':')[1]
                ask = ask[1:-1]
                            
                last_price = last_price.split(':')[1]
                last_price = last_price[1:-1]
                            
                low = low.split(':')[1]
                low = low[1:-1]
                            
                high = high.split(':')[1]
                high = high[1:-1]
                            
                volume = volume.split(':')[1]
                volume = volume[1:-1]
                            
                timestamp = timestamp.split(':')[1]
                timestamp = timestamp[1:-2]
                
                body = f"{i},platf=bitfx mid={mid},bid={bid},ask={ask},last_price={last_price},low={low},high={high},volume={volume},timestamp={timestamp}"
                url = f'http://localhost:8086/write?db={dbname}'
                response = requests.post(url, data=body)
                print('POSTED: ' + body)

                time.sleep(6)

        except:
            print("Выполнение прервано!")
            break

