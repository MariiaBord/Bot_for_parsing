#https://api.telegram.org/bot749299681:AAH1sR0yVhAaoDNeN6nMLgU5VIhGqR47enw/sendmessage?chat_id=794263297&text=hi
#https://api.telegram.org/bot
#749299681:AAH1sR0yVhAaoDNeN6nMLgU5VIhGqR47enw
#/sendmessage?chat_id=794263297&text=hi

import requests
from time import sleep
import misc
import Parcer2Example

token = misc.token
URL='https://api.telegram.org/bot'+token+'/'
global last_update_id
last_update_id=0

def get_updates():
    url=URL+'getupdates'
    r=requests.get(url) #<Response [200]>
   # print(r.json())
    return r.json()

def get_message():
    #отвечать только на новые сообщения, если id update измнилось
    # получить update_id  каждого обновления
    # записывать его в глобальную переменную и сравнивать с последним в списке result

    data=get_updates()
    last_object=data['result'][-1]
    current_update_id=last_object['update_id']
    global last_update_id

    if last_update_id != current_update_id:
        last_update_id = current_update_id

        chat_id=last_object['message']['chat']['id']#получить из составного словаря з последнего сообщения id
        #print(chat_id)
        message_text=last_object['message']['text']
        #print(message_text)
        message={'chat_id':chat_id,'text':message_text}

        return message
    return None

def send_message(chat_id,text='Wait a second,please...'):
    url=URL+'sendmessage?chat_id={}&text={}'.format(chat_id,text)
    requests.get(url)




def main():
    #d=get_updates()
    #преобразование в удобочитаемый файл
    # with open('updates.json','w') as file:
    #     json.dump(d,file,indent=2,ensure_ascii=False)

    while True:
        answer=get_message()

        if answer!= None:
            chat_id=answer['chat_id']
            text=answer['text']
            if text=='/parser':
                try:
                    Parcer2Example.main()
                    send_message(chat_id,'Done')
                except:
                    send_message(chat_id, 'Fail')
        else:
            continue
        sleep(5)

if __name__=='__main__':
    main()