import os, sys, requests, time
from keys import API_KEY, API_SECRET_KEY
from influxdb import InfluxDBClient

# using Http
#client = InfluxDBClient(database='dbname')
#client = InfluxDBClient(host='127.0.0.1', port=8086, username='root', password='root', database='dbname')

sys.getfilesystemencoding()
'UTF-8'


print('\nПрограмма для записи и мониторинга криптовалютных пар с помощью Influxdb и Graphana.')
print('Записи берутся с площадки Bitfinex.')
print('made by Nikita Rulenko\n')

dbname = 'testbtdb'
client = InfluxDBClient(host='127.0.0.1', port=8086, database=dbname)
client.create_database(dbname)
check = client.get_list_database()
print('Список баз данных: ' + str(check) + '\n')
client.switch_database(dbname)

path = os.getcwd()
print("Текущая директория: %s" % path)

while 1:
    try:
        key = int(input("Введите 1 для старта скрипта\nВведите 2 чтобы выйти из программы:"))

        if key == 1:

            while 1:
                try:

                    pairs = ['btcusd', 'ethusd', 'xrpusd', 'ltcusd', 'xmrusd', 'eosusd', 'etcusd', 'omgusd', 'leousd', 'neousd']

                    url = "https://api.bitfinex.com/v1/pubticker/ethusd"
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
                    
                    #print(f"btcusd,platf=bitfx mid={mid},bid={bid},ask={ask},last_price={last_price},low={low},high={high},volume={volume},timestamp={timestamp}")
                    body = f"ethusd,platf=bitfx mid={mid},bid={bid},ask={ask},last_price={last_price},low={low},high={high},volume={volume},timestamp={timestamp}"
                    url = f'http://localhost:8086/write?db={dbname}'
                    response = requests.post(url, data=body)
                    print('POSTED: ' + body)

                    time.sleep(6)

                except NameError:
                    print('Экстренный выход! Проверьете наличие интернет-соединения, если вы не прерывали программу вручную.')
                    break

            break

        
        elif key == 2:
            print('Пока!')
            break

        else:
            continue

        break
    except ValueError:
        print("Ошибка! Введите 1 или 2")

hold = input("Press Enter to exit")