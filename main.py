import os, sys, requests, time, json, ast
from influxdb import InfluxDBClient

sys.getfilesystemencoding()
'UTF-8'


print('\nПрограмма для записи и мониторинга криптовалютных пар с помощью Influxdb и Graphana.')
print('Записи берутся с площадки Bitfinex.')
print('made by Nikita Rulenko\n')

#------------------------------------CONFIG---------------------------------------------------------
dbname = 'bitfinex2'
client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)
client.create_database(dbname)
check = client.get_list_database()
print('Список баз данных: ' + str(check) + '\n')
client.switch_database(dbname)
pairs = ['btcusd', 'ethusd', 'xrpusd', 'ltcusd', 'xmrusd', 'eosusd', 'etcusd', 'omgusd', 'leousd', 'neousd']

#-----------------------------------MAIN_BLOCK-------------------------------------------------------
if __name__ == '__main__':    
    
    while True:
        try:

            for i in pairs:
                url = "https://api.bitfinex.com/v1/pubticker/" + i
                response = requests.request("GET", url)
                params = json.loads(response.text)
                
                mid = params['mid']
                bid = params['bid']
                ask = params['ask']
                last_price = params['last_price']
                low = params['low']
                high = params['high']
                volume = params['volume']
                timestamp = params['timestamp']    

                body = f"bitfinex,pair={i} mid={mid},bid={bid},ask={ask},last_price={last_price},low={low},high={high},volume={volume},timestamp={timestamp}"
                url = f'http://localhost:8086/write?db={dbname}'
                response = requests.post(url, data=body)
                print('POSTED: ' + body)

                time.sleep(6)

        except:
            print("Выполнение прервано!")
            break