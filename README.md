# Klipper notification for Line notify
1. สร้าง Line Group ใน line และ invite user ที่ชื่อ LINE Notify เข้ามาใน group
2. เข้าเว็บ https://notify-bot.line.me/ โดยใช้ line account
3. เข้าเว็บ https://notify-bot.line.me/my/ และสร้าง Generate token โดยเลือก group ที่สร้างจากข้อที่ 1
3. Download file ที่ชื่อ line_notify.py ไปใส่ใน klipper/klippy/extras
4. นำ access token ที่ได้จากข้อที่ 2 มาใส่ใน code ด้านล่าง และนำไปไว้ใน printer.cfg ในเว็บ Klipper
```
[line_notify]
access_token: <Put your access token>
```
5. สร้าง macro ไว้สำหรับใช้งานที่จะให้แจ้่งเตีอนจุดต่างๆ
```
[gcode_macro TEST_NOTIFY]
gcode:
  PUSH_LINE_NOTIFY MSG="Printing Done" SILENT=False
```

5. save and restart firmware



====================================================================================
เลี้ยงกาแฟ
PROMPT PAY: 
![alt text](promptpay.png)