import json

def Dictionary(device_info):

    device={}
    device['Hostname']=device_info[0]
    device['Software_Type']=device_info[1]
    device['Software Version']=device_info[2]
    device['Hardware']=device_info[3]

    return device

device_info=[]
test=[]
dev={}

while True:
    hostname = input('Enter hostname of the device: ')
    if len(hostname)>=20:
        print('hostname is invalid, number of characters exceeded')
        break

    device_info.append(hostname)

    soft_type = input('Enter Software Type: ')
    if len(soft_type)>=6:
        print('Software type is invalid, number of characters exceeded')
        break

    device_info.append(soft_type)

    soft_ver = input('Enter Software version: ')
    if len(soft_ver)>=10:
        print('Software version is invalid, maximum number of characters exceeded')
        break

    device_info.append(soft_ver)

    hardware = input('Enter Hardware Reference: ')
    if len(hardware)>=10:
        print('Hardware reference is invalid, maximum number of characters exceeded')
        break

    device_info.append(hardware)

    #Transforma la lista en diccionario para guardar la infor del dispositivo
    device_dict=Dictionary(device_info)
    
    #Lista de todos los dispositivos
    test.append(device_dict)

    #Dictionario de lista
    dev['Devices'] = test

    cont=input('Do you want to register a new devices YES(Y) NO(N): ')
    if cont=='N' or cont == 'n':
        break


with open('database.json','w') as file:
    json.dump(dev,file,indent=4)





