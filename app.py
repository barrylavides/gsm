from flask import Flask, render_template
import serial, time, glob
import json
from pprint import pprint

app = Flask(__name__)

# msisdn = [
#         {
#             "key": "9065953802",
#             "val": "/dev/tty.usbmodem14121"
#         },
#         {
#             "key": "9065202073",
#             "val": "/dev/tty.usbmodem14111"
#         },
#         {
#             "key": "9051663819",
#             "val": "/dev/tty.usbmodem14141"
#         },
#         {
#             "key": "9055183859",
#             "val": "/dev/tty.usbmodem14113"
#         },
#         {
#             "key": "9158065758",
#             "val": "/dev/tty.usbmodem14123"
#         },
#         {
#             "key": "9052297974",
#             "val": "/dev/tty.usbmodem14115"
#         },
#         {
#             "key": "9055878592",
#             "val": "/dev/tty.usbmodem14145"
#         },
#         {
#             "key": "9052650638",
#             "val": "/dev/tty.usbmodem14125"
#         },
#         {
#             "key": "9052275285",
#             "val": "/dev/tty.usbmodem14117"
#         },
#         {
#             "key": "9055326093",
#             "val": "/dev/tty.usbmodem14127"
#         },
#         {
#             "key": "9055852144",
#             "val": "/dev/tty.usbmodem14147"
#         }
#     ]
msisdn = [
    {
        "key": "9055326093",
        "val": "/dev/tty.usbmodem14127"
    },
    {
        "key": "9051663819",
        "val": "/dev/tty.usbmodem14141"
    }
]

def _parse_cpbr_row(s):
    """Parses a cpbr row data into a dictionary."""
    index, number, type, name = s.strip('+CPBR: ').split(',')
    return {
        'index': int(index),
        'number': number.replace('"', '').rstrip(),
        'type': int(type),
        'name': name.replace('"', '').rstrip(),
    }

def _parse_cpbr(s):
    """Parses cpbr response."""
    s = s.strip().rstrip()
    _numbers = []
    for l in s.split('\n'):
        if l[:6] == '+CPBR:':
            _numbers.append(_parse_cpbr_row(l))
    return _numbers


def sim_msisdn(str_port):
    ser = serial.Serial()
    ser.port = str_port
    ser.baudrate = 115200
    ser.timeout = 1
    
    ser.open()
    ser.write('AT+CPBS=SM\r')

    time.sleep(0.5)
    ser.write('AT+CPBR=1,100\r')

    time.sleep(0.5)
    res = ser.readall()

    print str_port

    numbers = _parse_cpbr(res)

    for num in numbers:
        if num['name'] == 'My Number':
	    return num['number']
    # return res

def read_inbox(str_port):
    ser = serial.Serial()
    ser.port = str_port
    ser.baudrate = 115200
    ser.timeout = 1
    
    ser.open()
    time.sleep(0.5)
    ser.write('AT+CMGF=1\r')
    time.sleep(0.5)
    ser.write('AT+CMGL=ALL\r')
    # ser.write('AT+CMGR=2\r')

    sms = ser.readall()

    # print sms.strip('+CMGL: ').split(',')
    print '===================================='
    print str_port
    print '===================================='
    return sms
    

def delete_sms(str_port):
    ser = serial.Serial()
    ser.port = str_port
    ser.baudrate = 115200
    ser.timeout = 1
    
    ser.open()

    # time.sleep(1)
    # ser.write(b'AT+CMGD=1\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=2\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=3\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=4\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=5\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=6\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=7\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=8\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=9\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=10\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=11\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=12\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=13\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=14\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=15\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=16\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=17\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=18\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=19\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=20\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=21\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=22\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=23\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=24\r')
    time.sleep(1)
    ser.write(b'AT+CMGD=25\r')
    # time.sleep(1)
    # ser.write(b'AT+CMGD=26\r')
    # time.sleep(0.5)
    # ser.write(b'AT+CMGD=27\r')
    time.sleep(0.5)

    res = ser.readall()
    return res


def balance(str_port):
    ser = serial.Serial()
    ser.port = str_port
    ser.baudrate = 115200
    ser.timeout = 1
    
    ser.open()
    time.sleep(0.5)

    # bal_type = '222'
    # ser.write(b'AT+CMGS="'+ bal_type +'"\r')
    # time.sleep(0.5)
    # ser.write('BAL'.encode() + b"\r")

    time.sleep(0.5)
    ser.write(b'AT+CUSD=1,"*143*4#"\r')
    time.sleep(0.5)

    time.sleep(0.5)
    ser.write(chr(26))
    time.sleep(0.5)

    res = ser.readall()

    return res

def send_sms(str_port, recipient, message):
    ser = serial.Serial()
    ser.port = str_port
    ser.baudrate = 115200
    ser.timeout = 1
    
    ser.open()

    time.sleep(0.5)
    ser.write('AT+CMGF=1\r')
    time.sleep(0.5)
    ser.write('AT+CMGS="%s"\r' % recipient)
    time.sleep(0.5)
    ser.write('%s\r' % message)
    ser.write(chr(26))

    res = ser.readall()

    return res

@app.route('/', methods=['GET'])
def index():
    sms = read_inbox('/dev/tty.usbmodem14141')
    sms_row = sms.split('+CMGL: ')
    unique_sender = []
    vote = {
        'ONE': 0,
        'TWO': 0,
        'THREE': 0,
        'FOUR': 0,
        'FIVE': 0,
    }

    sms_desc = []

    for x in sms_row:
        if 'BOTO' in x:
            sms_desc.append(x.split('\r'))
            # Get sender
    #         sender = x.split('"REC READ",')[1].split(',,')[0].replace('"','')

    #         if sender not in unique_sender:
    #             unique_sender.append(sender)
    #             print sender
                
    #             if 'ONE' in x.split('BOTO')[1]:
    #                 vote['ONE'] += 1
    #             elif 'TWO' in x.split('BOTO')[1]:
    #                 vote['TWO'] += 1
    #             elif 'THREE' in x.split('BOTO')[1]:
    #                 vote['THREE'] += 1
    #             elif 'FOUR' in x.split('BOTO')[1]:
    #                 vote['FOUR'] += 1
    #             elif 'FIVE' in x.split('BOTO')[1]:
    #                 vote['FIVE'] += 1
    
    for u in reversed(sms_desc):
        print u
        sender = u[0].split('"REC READ","')[1].split(',,')[0].replace('"','')

        if sender not in unique_sender:
            unique_sender.append(sender)

            if 'ONE' in u[1]:
                vote['ONE'] += 1
            elif 'TWO' in u[1]:
                vote['TWO'] += 1
            elif 'THREE' in u[1]:
                vote['THREE'] += 1
            elif 'FOUR' in u[1]:
                vote['FOUR'] += 1
            elif 'FIVE' in u[1]:
                vote['FIVE'] += 1

    print unique_sender
    print vote

    return render_template('index.html')

# print sim_msisdn('/dev/tty.usbmodem14121')
# delete_sms('/dev/tty.usbmodem14147')
# print balance('/dev/tty.usbmodem14141')



# print sim_msisdn('/dev/tty.usbmodem14145')
# print sim_msisdn('/dev/tty.usbmodem14113')

# for i in glob.glob('/dev/tty.usb*'):
# for i in msisdn:
    # print sim_msisdn(i)
    # print read_inbox(i['val'])

# Send SMS
recipient = ['09159422627']

# for j in recipient:
#     print send_sms('/dev/tty.usbmodem14141', j, 'sample msg')


if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0'
    )