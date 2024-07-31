import serial
import time
import csv
import datetime
import os
import pandas as pd
import keyboard

## 주석 추가 연습
# 시리얼 포트 설정
try:
    stm32f7 = serial.Serial('COM15', 115200, timeout=1)  # 포트 이름과 보드레이트 설정
    print("Starting Conversation with Arduino")
except serial.SerialException as e:
    print(f"Error opening serial port: {e}")
    exit()

# 사용자 입력을 받아 아두이노에 전송
SayingTo = input("Enter a message to send (enter 'load' to start): ")
stm32f7.write((SayingTo + '\n').encode())

# 'load' 메시지를 받은 경우에만 데이터 수신 및 CSV 파일 저장 시작
if SayingTo.strip().lower() == "load":
    print("Starting data collection")

    # 현재 날짜와 시간을 얻어 파일 이름 생성
    now = datetime.datetime.now()
    time_string = now.strftime("%y%m%d_%H%M")
    file_path = f"C:/Users/OMS55/OneDrive/Documents/성균관대학교/LAB/FingerForce_data_combine12_new_neg.csv"

    # 디렉토리 경로가 존재하는지 확인하고, 없으면 생성
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # CSV 파일을 생성하고 헤더 작성
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        pressure_finger = input("Enter a pressure, finger type used: ")
        new_column_name = f"Weight_{pressure_finger}"
    else:
        pressure_finger = input("Enter a pressure, finger type used: ")
        new_column_name = f"Weight_{pressure_finger}"
        df = pd.DataFrame()

    # 데이터 수신 및 CSV 파일에 기록 / 데이터량 기준으로 저장할거면 주석제거
    # start_time = time.time()
    # num_data = 400  # 데이터 수집 횟수
    collected_data = []
    # i = 0

    print("press 'q' to stop data collection")
    # 데이터량 기준으로 저장할거면 주석제거
    # while i <= 400:
    #     while stm32f7.in_waiting == 0:
    #         pass
    #
    #     # 시리얼 포트에서 데이터 읽기
    #     SdataPacket = stm32f7.readline().decode('utf-8').strip()
    #     print(f"Received data: {SdataPacket}")  # 수신한 데이터를 출력하여 확인
    while True:
        SdataPacket = stm32f7.readline().decode('utf-8').strip()
        print(f"Received data: {SdataPacket}")  # 수신한 데이터를 출력하여 확인

        while stm32f7.in_waiting == 0:
            if keyboard.is_pressed('q'):
                break
            pass

        if keyboard.is_pressed('q'):
            print("Data collection stopped by user.")
            break

        try:
            weight = float(SdataPacket)
            if weight > 0.5:  # 0 데이터를 무시
                collected_data.append(weight)
                print(format(weight, '.2f'))
                # i += 1
            elif weight < -0.5:
                collected_data.append(-1*weight)
                print(format(-1*weight, '.2f'))

            else:
                print("Received data is zero, ignoring.")
        except ValueError:
            print("Received invalid data packet")


    # 수집한 데이터를 DataFrame에 추가 / 데이터량 시 주석제거
    # if collected_data:
    #     if len(df) < len(collected_data):
    #         df = df.reindex(range(len(collected_data)))
    #     df[new_column_name] = collected_data
    if collected_data:
        new_data = pd.Series(collected_data, name=new_column_name)
        df = pd.concat([df, new_data], axis=1)

    # CSV 파일로 저장
    df.to_csv(file_path, index=False, encoding='utf-8')
    print("Data collection finished. Check file at:", file_path)
else:
    print("Invalid command. Terminating program.")