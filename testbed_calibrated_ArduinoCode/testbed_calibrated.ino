#include "HX711.h"

#define DOUT 4
#define CLK 2

HX711 scale(DOUT, CLK);
float calibration_factor = -46655;
bool start_measurement = false; // 측정 시작 여부

void setup() {
  Serial.begin(115200); // Python 코드와 일치하도록 시리얼 통신 속도를 115200으로 설정
  scale.set_scale(calibration_factor); // 초기 캘리브레이션 값 설정
  scale.tare(); // 무게 초기화
}

void loop() {
  if (Serial.available() > 0) {
    String command = Serial.readStringUntil('\n');
    if (command == "load") {
      start_measurement = true;
      Serial.println("Measurement started");
    }
  }

  if (start_measurement) {
    // 로드셀의 현재 무게를 읽음
    float weight = scale.get_units();

    // 측정된 데이터를 시리얼 포트로 전송
    Serial.print(weight, 2); // 소수점 둘째 자리까지 전송
    Serial.print(" ");
    Serial.println();
    delay(100); // 0.1초 대기
  }
}
