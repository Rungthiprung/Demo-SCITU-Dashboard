# Sci-TU Report Dahsboard and Management
เว็บแอปพลิเคชันสำหรับกระดานสรุปข้อมูลเพื่อการบริหารจัดการและการแก้ปัญหา ภายในคณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยธรรมศาสตร์ขึ้น เพื่อให้เป็นประโยชน์ต่อบุคลากรทั้งฝ่ายผู้บริหาร และหัวหน้างานฝ่ายต่างๆที่รับผิดชอบดูแลภายในมหาวิทยาลัย โดยเว็บแอปพลิเคชันนี้สามารถทำให้ผู้ใช้เห็นถึงภาพรวมของปัญหาที่เกิดขึ้นภายในคณะได้อย่างน่าสนใจ ถูกต้อง ครบถ้วนสมบูรณ์ สื่อความหมายออกมาได้อย่างชัดเจน และมีข้อมูลที่เป็นปัจจุบัน  อีกทั้งยังรวมไปถึงการรวบรวมการทำงานของเจ้าหน้าที่ในแต่ละฝ่าย ทำให้เห็นถึงประวัติการทำงานช่วยให้เห็นถึงการทำงานจริง ทางทีมผู้จัดทำคาดหวังว่าแอปพลิเคชันนี้จะเป็นประโยชน์ต่อหน่วยงานและบุคลากรภายในคณะวิทยาศาสตร์และเทคโนโลยี มหาวิทยาลัยธรรมศาสตร์
<br />
## ตรวจเช็ค python version 
ก่อนจะทำการติดตั้งเราต้องตรวจเช็ค version ของ python และ pip ก่อน เพราะถ้าหาก version ไม่ได้ตรงก็อาจจะไม่สามารถรันไฟล์บางตัวได้ สามารถไปที่ cmd(command prompt) และใช้คำสั่ง

`python -V`

`pip -V`

> **_NOTE:_**  python ควรเป็น python 3.9.7  และ pip 21.3.1 จะเหมาะต่อการติดตั้งโปรเจคนี้ 

<br />
## มาเริ่มต้นการสร้างสภาพเเวดล้อม
หลังจากที่เราได้ version ของ pyhon และ pip ตามที่ต้องการแล้ว ต่อไปจะเป็นการสร้าง virtual environment  ซึ่ง Virtualenv จะสร้าง environment ใหม่ขึ้นมา ที่มีแต่ตัว Python เปล่าๆ แล้วเวลาเราติดตั้ง library อะไรไปมันก็จะเก็บไว้ใน Folder ของ environment แต่ละงานก็จะไม่มาปนกัน เรียกง่ายๆก็คือ สร้างสภาพแวดล้อมให้เหมาะกับการใช้งานโปรเจคนี้นั่นเอง

`python -m venv venv`

เป็นคำสั่งสร้าง Virtualenv โดย venv ตัวหลังจะเป็นชื่อที่เราสามารถตั้งสภาพแวดล้อมของเรา/สามารถเปลี่ยนแปลงได้ตามที่ต้องการ 
จากนั้น cd เข้าไปใน venv และใช้คำสั่ง

`scripts\activate`

เป็นเหมือนการเปิดประตูเข้าไปในสภาพแวดล้อมนี้ เพื่องานหรือติดตั้งไฟล์ install library นั่นเอง 
> **_Q:_** แล้วเราจะทราบได้อย่างไรว่าเข้าสู่ Virtualenv เรียบร้อย? 
> **_A:_** ให้ดูตรงข้างหน้าไดเรกเทอรี่ จะมีวงเล็บชื่อของ Virtualenv ที่เราตั้งไว้
> `(venv) D:\Demo\venv `

จากนั้นนำโฟลเดอร์ (sci_tu_dashboard) ที่ดาวน์โหลดไว้มาใส่ในโฟลเดอร์ venv ใช้คำสั่งด้านล่างนี้ เพื่อเป็นการติดตั้ง library ที่ตัวงานนี้ต้องการใช้ (cd เข้าไปในโฟลเดอร์งานก่อนรันคำสั่ง)

`pip install -r requirment.txt`

ตอนนี้เราก็จะมีสภาพแวดล้อมที่เหมาะสมต่อตัวงานแล้วลองเปิดอีดิเตอร์เพื่อตรวจดูโครงสร้างของตัวงานได้ ต่อไปเราจะต้องมาจัดการกับฐานข้อมูลต่อ

<br />
## ฐานข้อมูล MySQL
เนื่องจากตัวงานนี้ใช้ MySQL เป็นฐานข้อมูลดังนั้น เราจะต้องมี MySQL workbench ก่อน จากนั้นเราจะสร้าง schema ที่ชื่อว่า sci_dashboard_database เตรียมไว้
> **Note:**  เปิดเอดิเตอร์เข้าไปที่ sci_tu_dashboard/settings_local.py เพื่อแก้ไข user และ password ของคุณให้ตรงกับ MySQL workbench 

เราจะใช้2คำสั่งต่อไปนี้ คือ python manage.py makemigrations เป็นการแปลงโมเดลของเราให้เป็น schema ของฐานข้อมูล และคำสั่งที่ 2 คือ python manage.py migrate เป็นคำสั่งยืนยันการ migrate ตัว schema ทั้งหลายเหล่านี้ลงไปสู่ฐานข้อมูล หรือเป็นการสร้างตารางนั่นเอง

    python manage.py makemigrations
    python manage.py migrate

เมื่อเข้าไปดูที่ MySQL workbench ก็จะเห็นว่าตารางต่างๆถูกสร้างลงใน schema sci_dashboard_database เรียบร้อยร้อย ซึ่งตอนนี้ก็ยังเป็นตารางเปล่าๆ ยังไม่มีข้อมูล ดังนั้นต่อไปเราจะมา ดาวน์โหลดข้อมูลลงฐานข้อมูลกัน


	python manage.py loaddata building.json
	python manage.py loaddata reportType.json
	python manage.py loaddata accountdata.yaml
	python manage.py loaddata roomdata.yaml
	python manage.py loaddata reportdata.yaml

เรียงลำดับการรันคำสั่งตามด้านบน ข้อมูลที่มีอยู่ก็จะถูกดาวน์โหลดไปไว้ที่ฐานข้อมูลเรียบร้อย
<br />
## สร้าง username เพื่อเข้าสู่ระบบ
เมื่อคุณมีโปรเจคนี้คุณก็คือ superuser ดังนั้นจะใช้คำสั่ง

`python manage.py createsuperuser`

เพื่อทำการสร้าง username และ password เมื่อเรียบร้อยแล้วเราจะมาลอง runserver เพื่อเปิดตัวเว็บไซต์กัน

`python manage.py runserver`

ไปที่ http://127.0.0.1:8000/ ก็จะได้ส่วนของหน้าเข้าสู่ระบบของเว็บแอปพลิเคชัน sci-tu report dashboard and management มาและเมื่อเข้าสู่ระบบจะเห็นว่าคงเกิด error อยู่เนื่องจากเรายังไม่ได้ setting group นั่นเอง

ดังนั้นเราจะไปสร้าง group ที่ http://127.0.0.1:8000/admin/ โดยจะสร้างกลุ่มทั้งหมด 3 กลุ่ม 
1. scitu-admin
2. scitu-chief
3. scitu-staff

จากนั้นไปที่ user > (usernameของเรา) > เลื่อนลงมายัง group เพื่อ add group ตัวเองเป็น scitu-admin > save 
ตอนนี้เมื่อเรากับไปที่หน้าเว็บไซต์ก็จะสามารถเห็นหน้าแดชบอร์ด เป็นอันเรียบร้อย


<br />

## Code-base structure


```bash
< PROJECT ROOT >
   |
   |-- auth_app/
   |    |-- _pycache_/
   |	|-- backends/
   |	|-- migrations/
   |    |   |-- ict_authen.py
   |    |
   |    |-- admin.py
   |	|-- apps.py
   |    |-- models.py
   |	|-- tests.py
   |    |-- views.py
   |
   |-- sci_dashboard_app/
   |    |-- _pycache_/
   |	|-- dash_apps/
   |	|-- fixtures/                           # for run to mySQL database
   |    |   |-- accountdata.yaml                # account officer data
   |    |   |-- building.json                   # building data
   |    |   |-- report.csv                      # report data from google sheet
   |    |   |-- report.py                       # clean report data
   |    |   |-- reportdata.yaml                 # report data 
   |    |   |-- reportType.json                 # report type data
   |    |   |-- roomdata.yaml                   # room data
   |    |   
   |    |-- migrations/
   |	|-- templates/                          # Templates used to render pages
   |    |   |-- dashboard/
   |    |   |   |-- dashboard.html
   |    |   |  
   |    |   |-- home/
   |    |   |   |-- admin_home.html
   |    |   |   |-- chief_home.html
   |    |   |   |-- staff_home.html
   |    |   |  
   |    |   |-- includes/
   |    |   |   |-- scripts.html
   |    |   | 
   |    |   |-- officer/
   |    |   |   |-- detailofficer.html
   |    |   |   |-- ITstaff.html
   |    |   |   |-- maintenance.html
   |    |   |   |-- roomcaretaker.html
   |    |   |   |-- supervisor.html
   |    |   |   
   |    |   |-- registation/
   |    |   |   |-- login.html
   |    |   |   
   |    |   |-- summary_report/
   |    |   |   |-- bylocation.html
   |    |   |   |-- bystatus.html
   |    |   |   |-- location-datails-type.html
   |    |   |   |-- location-datails.html
   |    |   |   |-- pending.html
   |    |   |   |-- received.html
   |    |   |   |-- start.html
   |    |   |   |-- success.html
   |    |   |   
   |    |   |-- base.html
   |    |   
   |	|-- __init__.py
   |    |-- admin.py
   |	|-- apps.py
   |	|-- decorators.py
   |    |-- models.py                           # go to act as the interface of data
   |	|-- tests.py
   |	|-- urls.py                             # store all links of the project and functions to call
   |    |-- view_admin.py
   |	|-- view_chief.py
   |	|-- view_staff.py
   |    |-- views.py
   |	 	
   |-- sci_tu_dashboard/
   |    |-- _pycache_/
   |	|-- __init__.py                         # It is a python package
   |	|-- asgi.py
   |	|-- routing.py
   |	|-- settings_local.py                   # setting database and ICT-auth
   |	|-- settings.py                         # Django app bootstrapper
   |	|-- urls.py                             # Define URLs served by all apps/nodes
   |	|-- wsgi.py                             # Start the app in production
   |	
   |-- static/
   |    |-- <css, JS, images>                   # CSS files, Javascripts files
   |
   |-- .coverage
   |-- CREATE
   |-- README.md
   |-- requirements.txt                         # Development modules
   |-- manage.py                                # Start the app - Django default start script
   |
   |-- ************************************************************************
```
<br />