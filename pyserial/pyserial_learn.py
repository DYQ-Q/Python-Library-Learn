import serial
import time

COM_PORT = 'COM20'  # 你用来发送的端口
BAUD_RATE = 9600

try:
    with serial.Serial(port=COM_PORT, baudrate=BAUD_RATE, timeout=0.1) as com:
        print(f"✅ {com.name} 打开成功！")
        print("📝 请在下方输入要发送的内容，按回车发送。(输入 'quit' 退出)")
        
        while True:
            # 1. 阻塞等待用户输入
            user_input = input("请输入 >> ")
            
            # 2. 退出判断
            if user_input.lower() == 'quit':
                print("退出程序")
                break
                
            # 3. 将输入的字符串加上换行符，编码为字节并发送
            # 加换行符是因为大多数串口设备靠 \n 来判断一条指令结束
            send_data = (user_input + '\n').encode('utf-8')
            com.write(send_data)
            print(f"✅ 已发送: {user_input}")
            
            # 4. 稍微等一下，给接收端一点处理和回复的时间
            time.sleep(0.1)

except serial.SerialException as e:
    print(f"❌ 串口打开失败: {e}")
except KeyboardInterrupt:
    print("\n用户主动中断程序")
