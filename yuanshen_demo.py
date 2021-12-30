from time import sleep
import threading
import serial

#按键16进制键值
E = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x14]  # 字母e
Q = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x20]  # 字母q
num_1 = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x1E, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2A]  # 英文数字区 1
num_2 = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2B]  # 英文数字区 2
num_3 = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C]  # 英文数字区 3
num_4 = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x00, 0x00, 0x21, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2D]  # 英文数字区 4
shift = [0x57, 0xAB, 0x00, 0x02, 0x08, 0x20, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x2C]  # 右边 shift
release = [0x57, 0xab, 0x00, 0x02, 0x08] + [0x00] * 8 + [0x0c]


#按下函数
def press(x, t=0):
    serial.write(bytes(x))
    sleep(t)
    serial.write(bytes(release))
	
#延时函数	
def delay(t):
    sleep(1/1000*t)
	
#按下并延时
def keyPress(x):
    delay(50)
    # print("按下%s键\n" % x)
    press(x, 0.05)
    delay(50)
	
	
#默认x=0点击左键， x=1单击右键
def click (x=0,t=0):
    cmd = [0x57, 0xAB, 0x00, 0x04, 0x07, 0x02]
    data = [x+1,  0x00, 0x00, 0x00, 0x00, 0x00]
    sum_m = 0x10+x
    data.append(sum_m)
    m = cmd + data
    m_release = [0x57, 0xAB, 0x00, 0x04, 0x07, 0x02, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x0f]
    serial.write(bytes(m))
    sleep(t)
    serial.write(bytes(m_release))
    return True


# 莫甘娜自动战斗 X表示战斗循环次数
def skill_ice(x):
	keyPress(F)
    for i in range(1, x + 1):
        print("<<第%d战斗回合>>" % i)
        print('切换角色1-莫娜')
        keyPress(num_1)
        keyPress(E)  # delay(100)
        print('莫娜-释放E技能')  # 后摇400 cd 12
        keyPress(E)
        keyPress(Q)  # delay(400)
        keyPress(Q)  # delay(400)
        print('莫娜-释放Q技能')  # 后摇1800 cd 15
        keyPress(Q)
        for a in range(0, 1800, 150):  # delay(1800)
            press(num_2)
            click(0)
            press(F)
            delay(150)

        keyPress(num_2)
        print('切换角色2甘雨-甘雨')
        for b in range(0, 300, 150):
            press(E)
            click(0)
            press(F)
            delay(150)
        print('甘雨-释放E技能')  # 后摇400 cd 10
        keyPress(E)
        for bb in range(0, 400, 150):
            press(Q)
            click(0)
            press(F)
            delay(150)
        print('甘雨-释放Q技能')  # 后摇2000 cd 15
        keyPress(Q)
        for bbb in range(0, 2000, 150):  # delay(2000)
            press(num_3)
            click(0)
            press(F)
            delay(150)

        keyPress(num_3)
        print('切换角色3-温蒂')
        for c in range(0, 300, 150):
            press(E)
            click(0)
            press(F)
            delay(150)
        print('温蒂-释放E技能')  # 后摇300 cd 6
        keyPress(E)
        for cc in range(0, 300, 150):
            press(Q)
            click(0)
            press(F)
            delay(150)
        print('温蒂-释放Q技能')  # 后摇1500 cd 15
        keyPress(Q)
        for ccc in range(0, 1500, 150):
            press(num_4)
            click(0)
            press(F)
            delay(150)

        keyPress(num_4)
        print('切换角色4-七七')
        for d in range(0, 300, 150):
            press(E)
            click(0)
            press(F)
            delay(150)
        print('七七-释放E技能')  # 后摇600 cd 30-15
        keyPress(E)
        for dd in range(0, 1000, 150):
            press(Q)
            click(0)
            press(F)
            delay(150)
        print('七七-释放Q技能')  ##后摇1200 cd 20-15
        keyPress(Q)
        for ddd in range(0,2000,150):
            press(shift)
            press(F)
            click(0)
            delay(25)
            press(F)
            click(0)
            delay(25)
            press(num_1)
#串口回显
def rcv_data():
    while True:
        rcv=serial.readline()
        rcv=rcv.decode()
        print(rcv)
		
#打开串口		
serial=serial.Serial("/dev/ttyUSB0", 115200)
th=threading.Thread(target=rcv_data)
th.setDaemon(True)
th.start()
if serial.isOpen():
    print("串口打开成功：",serial.name)
while 1:
	for i in range(-5,1):
		print(-i)
		sleep(1)
    skill_ice(5)
    sleep(50)


#
