# Python-Web-PostgrestSQL
 โปรเจค นี้ทำการสร้างเว็บที่พัฒนาด้วย Python Flask และใช้ฐานข้อมูล Database PostgreSQL เพื่อจัดเก็บและแสดงข้อมูลภาพยนตร์ จุดประสงค์หลักคือเพื่อแสดงความสามารถในการสร้างเว็บแอปพลิเคชันพื้นฐานที่มีการเชื่อมต่อและดึงข้อมูลจากฐานข้อมูลมาแสดงในรูปแบบตารางบนหน้าเว็บ

โปรเจกต์ประกอบด้วย 2 หน้าหลัก: หน้าข้อมูลนักศึกษา (/) หน้าแสดงข้อมูลภาพยนตร์ (/movie) 
```bash
Python-Web-PostgrestSQL
├── app.py
├── __pycache__
│   ├── query_db.cpython-313.pyc
│   └── query_db.cpython-38.pyc
├── query_db.py
├── README.md
├── static
│   ├── 1.gump.png
│   ├── 2.shutter.png
│   ├── 3.green.png
│   ├── 4.ryan.png
│   ├── 5.catchme.png
│   └── 6.me.jpg
└── templates
    ├── index.html
    └── movie.html
```
ขั้นตอนการพัฒนาเว็บด้วย Flask 
1. ติดตั้ง Flask
```bash
   pip install flask
```
2. สร้างไฟล์หลัก web.py
```bash
ใช้ Flask ในการสร้าง route ของแต่ละหน้า เช่น /, /movie
```
3. สร้าง Template (HTML)
```bash
สร้างโฟลเดอร์ชื่อ templates เพื่อเก็บไฟล์หน้าเว็บทั้งหมด เช่น index.html, movie.html
```
4. สร้าง ฟลอเดอร์ static เพื่อเก็บรูปภาพ เช่น
```bash
1.gump.png 2.shutter.png 3.green.png 
4.ryan.png 5.catchme.png 6.me.jpg
```
5. เชื่อมโยง HTML กับ Flask ด้วย render_template() และ request.form เพื่อ รับค่าจากแบบฟอร์ม (POST)
6. การรันเว็บแอปพลิเคชัน เปิด Command Prompt หรือ Terminal แล้วพิมพ์:
```bash
sudo python3 web.py
```
7. หากสำเร็จ จะเห็นข้อความ (ในเว็บนี้กำหนดให้ใช้ Port 80 ถ้าไม่กำหนด port ต้องใส่ Default Port :5000)
```bash
* Running on http://127.0.0.1:80/
* Running on http://127.0.0.1:5000/  กรณี ไม่กำหนด port
```




