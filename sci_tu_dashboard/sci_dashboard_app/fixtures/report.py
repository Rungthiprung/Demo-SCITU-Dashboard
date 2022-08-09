import csv
import yaml
from yaml.loader import SafeLoader
import json

def checkRoom2(room) :
    with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\roomdata.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        lc2 = []
        listId = []
        i = -1
        for x in data :
            if(x.get("building_id")==2) :
                lc2.append(x.get("name"))
                listId.append(x.get("id")) 
        for x in lc2 :
            i = i + 1
            if(room==x) :
                return listId[i]
            elif(room!=x) :
                r = room.split(" ")
                if(r[1]==x) :
                    return listId[i]

def checkRoom3(room) :
    with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\roomdata.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        lc3 = []
        listId = []
        i = -1
        for x in data :
            if(x.get("building_id")==3) :
                lc3.append(x.get("name"))
                listId.append(x.get("id")) 
        for x in lc3 :
            i = i + 1
            if(room==x) :
                return listId[i]
            elif(room!=x) :
                r = room.split(" ")
                if(r[1]==x) :
                    return listId[i]

def checkRoom4(room) :
    with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\roomdata.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        lc4 = []
        listId = []
        i = -1
        for x in data :
            if(x.get("building_id")==4) :
                lc4.append(x.get("name"))
                listId.append(x.get("id")) 
        for x in lc4 :
            i = i + 1
            if(room==x) :
                return listId[i]
            elif(room!=x) :
                r = room.split(" ")
                if(r[1]==x) :
                    return listId[i]

def checkRoom5(room) :
    with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\roomdata.json', encoding="utf-8") as json_file:
        data = json.load(json_file)
        lc5 = []
        listId = []
        i = -1
        for x in data :
            if(x.get("building_id")==5) :
                lc5.append(x.get("name"))
                listId.append(x.get("id")) 
        for x in lc5 :
            i = i + 1
            if(room==x) :
                return listId[i]
            elif(room!=x) :
                r = room.split(" ")
                if(r[1]==x) :
                    return listId[i]

def taker(name):
    with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\accountdata.yaml') as t:
        taker = yaml.load(t, Loader=SafeLoader)
        for x in taker:
            fullName = x.get('fields').get('firstname') + ' ' + x.get('fields').get('lastname')
            if(name == fullName):
                return x.get('pk')

with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\report.csv', encoding="utf-8") as f:
    reader = csv.reader(f)

    data = []
    count = 1
    lc2 = 0
    for row in reader:
        count = count + 1
        lc2 = lc2+1

        print("ห้องจากreport: "+row[5])
        room = row[5].split(" ")
        if(room[0]=="ห้อง"):
            row[5]=row[5]
        elif(room[0]!="ห้อง"):
            row[5]="ห้อง "+row[5]
        
        if(row[4] == 'บร.2'):
            row[4] = 2
            roomid = checkRoom2(row[5])
        elif(row[4] == 'บร.3'):
            row[4] = 3
            roomid = checkRoom3(row[5])
        elif(row[4] == 'บร.4'):
            row[4] = 4
            roomid = checkRoom4(row[5])
        elif(row[4] == 'บร.5'):
            row[4] = 5
            roomid = checkRoom5(row[5])
        else :
            row[4] = "ไม่สามารถระบุได้"
            roomid = None


        if(roomid==None):
            row[5] = "ไม่สามารถระบุได้"
        if(roomid==1 or roomid==2 or roomid==3):
            room = row[5].split(" ")
            row[5] = room[1]

        print("id: "+str(roomid)+" อาคาร: "+str(row[4])+" ห้อง: "+row[5])
        print(" ")

        if(row[8] != "-"):
            row[8] = taker(row[8])
        else :
            row[8] = 'null'

        rowday = row[0].split('T')
        rowtime = rowday[1].split('.')
        row[0] = rowday[0] + " " + rowtime[0]

        if(row[6] == 'เสร็จสิ้น'):
            row[6] = 'success'
        elif (row[6] == 'รับเรื่องแล้ว'):
            row[6] = 'received'
        elif (row[6] == 'กำลังดำเนินการ'):
            row[6] = 'pending'
        elif (row[6] == 'เริ่มต้น'):
            row[6] = 'start'
        
        if(row[3] == 'ไอทีและอินเทอร์เน็ต'):
            row[3] = '1'
        elif(row[3] == 'สื่อการเรียนการสอน'):
            row[3] = '2'
        elif(row[3] == 'ระบบไฟฟ้า'):
            row[3] = '3'
        elif(row[3] == 'ระบบประปา'):
            row[3] = '4'
        elif(row[3] == 'ระบบโทรศัพท์'):
            row[3] = '5'
        elif(row[3] == 'ระบบเครื่องปรับอากาศ'):
            row[3] = '6'
        elif(row[3] == 'วัสดุภายในห้อง'):
            row[3] = '7'
        elif(row[3] == 'ความสะอาดและความปลอดภัย'):
            row[3] = '8'
        elif(row[3] == 'อาคารและสิ่งแวดล้อม'):
            row[3] = '9'
        elif(row[3] == 'อื่นๆ'):
            row[3] = '10'

        date = row[9].split(" ")
        if(len(list(date)) <= 2):
            row[9] = " "
        elif(len(list(date)) >= 3):
            if(date[2] == 'Jan'):
                date[2] = "01"
            elif(date[2] == 'Feb'):
                date[2] = '02'
            elif(date[2] == 'Mar'):
                date[2] = '03'
            elif(date[2] == 'Apr'):
                date[2] = '04'
            elif(date[2] == 'May'):
                date[2] = '05'
            elif(date[2] == 'Jun'):
                date[2] = '06'
            elif(date[2] == 'Jul'):
                date[2] = '07'
            elif(date[2] == 'Aug'):
                date[2] = '08'
            elif(date[2] == 'Sep'):
                date[2] = '09'
            elif(date[2] == 'Oct'):
                date[2] = '10'
            elif(date[2] == 'Nov'):
                date[2] = '11'
            elif(date[2] == 'Dec'):
                date[2] = '12'
            row[9] = "%s-%s-%s %s" % (date[3], date[2],date[1],date[4])
       

    #     data.append({
    #             'model': 'sci_dashboard_app.report',
    #             'pk': count,
    #             'fields': {
    #                 'reportID': row[1],
    #                 'building': row[4],
    #                 'room': row[5],
    #                 'takecareBy': row[8],
    #                 'creatorname': row[7],
    #                 'timestamp': row[0],
    #                 'statusReport': row[6],
    #                 'description': row[2],
    #                 'image': row[11],
    #                 'type': row[3],
    #                 'lastModified': row[9]
    #             }
    #         }
    #     )
    # with open('D:\\Demo\\venv\\sci_tu_dashboard\\sci_dashboard_app\\fixtures\\reportdata.yaml', 'w') as outfile:
    #     yaml.dump(data, outfile, default_flow_style=False,sort_keys=False)