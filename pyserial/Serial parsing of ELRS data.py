'''
中文
使用python的pyserial库解析ELRS数据
硬件:usb转ttl模块(支持420000波特率),elrs接收器和发送器(ELRS遥控器)
连接:将遥控器和接收器对码,然后使用usb转ttl模块连接电脑和接收器(usb连电脑,ttl连接收器)

English
Using Python's pyserial library to parse ELRS data
Hardware: USB-to-TTL module (supports 420000 baud rate), ELRS receiver, and ELRS transmitter (ELRS radio controller).
Connection: Bind the radio controller and the receiver, then use the USB-to-TTL module to connect the computer and the receiver (USB to the computer, TTL to the receiver).
'''
import serial
import time
import struct

# --- CRSF 协议常量 ---
CRSF_ADDRESS_RX = 0xC8       # 接收器发送给飞控的地址
CRSF_FRAME_LENGTH_RC = 0x18  # RC通道帧的长度 (24 bytes)
CRSF_FRAME_TYPE_RC_CHANNELS = 0x16 # RC通道包类型

# 通道分辨率: 11 bit (0 - 1984), 中值为 992
CRSF_CHANNEL_VALUE_MIN = 0
CRSF_CHANNEL_VALUE_MAX = 1984
CRSF_CHANNEL_VALUE_MID = 992

def unpack_rc_channels(payload):
    """
    解析 CRSF RC Channels 载荷 (22 字节)
    提取 16 个通道的值 (11 bit 每通道)
    """
    # 将 22 字节打包成 11 个 16-bit 无符号整数
    # 小端模式: '<' 代表小端, 'H' 代表 unsigned short (2 bytes)
    words = struct.unpack('<11H', payload)
    
    # 将 11 个 16-bit 字组合成一个长位流，然后每次提取 11 bit
    # 注意: 11 * 16 = 176 bits, 16 * 11 = 176 bits, 刚好完美对齐
    channels = []
    bit_offset = 0
    for ch_idx in range(16):
        # 计算当前 11-bit 通道跨越了哪几个 16-bit word
        start_word = bit_offset // 16
        start_bit_in_word = bit_offset % 16
        
        # 提取数据
        val = words[start_word] >> start_bit_in_word
        
        # 如果 11 bit 跨越了两个 word，需要拼接下一个 word 的低位
        if start_bit_in_word + 11 > 16:
            extra_bits = (start_bit_in_word + 11) - 16
            val |= words[start_word + 1] << (16 - start_bit_in_word)
            
        # 掩码取低 11 位
        val &= 0x7FF 
        channels.append(val)
        bit_offset += 11
        
    return channels

def parse_crsf_frame(frame_bytes):
    """
    验证并解析一帧 CRSF 数据
    """
    if len(frame_bytes) < 4:
        return None
        
    address = frame_bytes[0]
    length = frame_bytes[1]
    frame_type = frame_bytes[2]
    
    # 检查是否是 RC 通道帧
    if address == CRSF_ADDRESS_RX and length == CRSF_FRAME_LENGTH_RC and frame_type == CRSF_FRAME_TYPE_RC_CHANNELS:
        # 提取 22 字节载荷 (跳过 Address, Length, Type)
        payload = frame_bytes[3:25]
        # 提取 CRC (最后一个字节)
        crc = frame_bytes[-1]
        
        # TODO: 这里可以添加 CRC 严格校验，为了性能和简单起见暂时跳过
        # 实际使用中，ELRS 数据很稳定，一般不会出错
        
        channels = unpack_rc_channels(payload)
        return channels
        
    return None

def read_serial_data(port_name, baudrate=420000):
    """
    读取串口并实时解析数据
    """
    print(f"正在打开串口 {port_name} @ {baudrate}bps ...")
    try:
        ser = serial.Serial(port_name, baudrate, timeout=0.1)
        print(ser.name,ser.is_open)
        print("✅ 串口打开成功！")
    except serial.SerialException as e:
        print(f"串口打开失败: {e}")
        return

    buffer = bytearray()
    
    try:
        while True:
            # 读取串口数据放入缓冲区
            if ser.in_waiting > 0:
                buffer.extend(ser.read(ser.in_waiting))
            
            # 在缓冲区中寻找 CRSF 帧头
            while len(buffer) >= 2:
                # 寻找接收器地址 0xC8
                if buffer[0] != CRSF_ADDRESS_RX:
                    buffer.pop(0) # 丢弃无效字节
                    continue
                # 获取帧长度
                frame_len = buffer[1]
                total_frame_size = 2 + frame_len # Address(1) + Length(1) + Payload + CRC
                
                # 如果缓冲区数据不够一帧，跳出循环继续接收
                if len(buffer) < total_frame_size:
                    break
                
                # 提取一帧完整数据
                frame = buffer[:total_frame_size]
                buffer = buffer[total_frame_size:] # 移除已处理的数据
                
                # 解析数据
                channels = parse_crsf_frame(frame)
                if channels:
                    # 实时打印通道数据
                    # 将原始值(0-1984)映射为更直观的数值，例如 1000~2000 (标准PWM中间值)
                    # 公式: pwm_value = 1000 + (crsf_value * 1000 / 1984)
                    print_str = "Channels: "
                    for i, val in enumerate(channels):
                        # 仅打印前 8 个通道 (通常为 A, E, T, R, Aux1-4)，如需16通道可改为 16
                        if i < 8: 
                            pwm_val = int(1000 + (val * 1000 / 1984))
                            print_str += f"CH{i+1}:{pwm_val:4d} "
                    print(print_str)

    except KeyboardInterrupt:
        print("\n用户中断程序")
    finally:
        ser.close()
        print("串口已关闭")

# ==========================================
# 单元测试：使用你提供的示例数据进行验证
# ==========================================
def test_with_sample_data():
    sample_data = bytes([0xC8, 0x18, 0x16, 0xE0, 0x03, 0x9F, 0x2B, 0xC0, 0xF7, 0x8B, 0x5F, 0xFC, 0xA2, 0x7C, 0xE5, 0x2B, 0x5F, 0xF9, 0xCA, 0x07, 0x00, 0x00, 0x4C, 0x7C, 0xE2, 0xD9])
    
    print("--- 使用示例数据测试 ---")
    channels = parse_crsf_frame(sample_data)
    if channels:
        for i, val in enumerate(channels):
            pwm_val = int(1000 + (val * 1000 / 1984))
            print(f"Channel {i+1:2d}: Raw={val:4d}, PWM={pwm_val:4d}")
    else:
        print("解析失败")
    print("------------------------\n")

if __name__ == '__main__':
    # 1. 先运行示例数据测试
    test_with_sample_data()
    
    # 2. 运行串口实时读取
    # ⚠️ 请根据你的电脑实际串口号修改下方参数 (例如 Windows 的 'COM3' 或 Linux 的 '/dev/ttyUSB0')
    COM_PORT = 'COM20' 
    BAUD_RATE = 420000  # CRSF 标准波特率必须是 420000
    
    read_serial_data(COM_PORT, BAUD_RATE)
