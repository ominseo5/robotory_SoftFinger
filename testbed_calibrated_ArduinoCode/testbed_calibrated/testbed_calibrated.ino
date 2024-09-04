#include "HX711.h"  // HX711 라이브러리를 사용

// 스텝모터 핀 설정
int PUL = 7;  // Pulse pin
int DIR = 6;  // Direction pin
int ENA = 5;  // Enable Pin

// 로드셀 핀 설정
#define LOADCELL_DOUT_PIN  3  // HX711의 DT 핀 연결
#define LOADCELL_SCK_PIN  2   // HX711의 SCK 핀 연결

HX711 scale;

static bool systemRunning = false;
static bool systemStopped = false;

void setup() {
  // 스텝모터 핀 초기화
  pinMode(PUL, OUTPUT);
  pinMode(DIR, OUTPUT);
  pinMode(ENA, OUTPUT);
  digitalWrite(ENA, HIGH);  // 모터 활성화

  // 시리얼 통신 시작
  Serial.begin(115200);

  // 로드셀 초기화
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);  // HX711 초기화
  scale.set_scale(-46655);  // 보정된 스케일 팩터 설정
  scale.tare();  // 영점 조정

}

void loop() {

  // 사용자 입력 처리
  if (Serial.available() > 0) {
    char input = Serial.read();  // 시리얼 모니터에서 입력된 첫 번째 문자 읽기

    if (input == 'l') {  // 'l'로 시작하는 경우 'load' 명령으로 처리
      Serial.println("Starting system...");
      systemRunning = true;
      systemStopped = false;
    }

    if (input == 'q') {  // 'q'가 입력되면 시스템 중지
      Serial.println("Stopping system...");
      systemRunning = false;
      systemStopped = true;
    }
  }

  // 시스템이 실행 중일 때만 동작
  if (systemRunning && !systemStopped) 
  {
    for (int i = 0; i < 5; i++)    //Forward 5 steps
    {
      digitalWrite(PUL, HIGH);
      delayMicroseconds(200);
      digitalWrite(PUL, LOW);
      delayMicroseconds(200);
    }

    // 로드셀 값 10번 측정
    for (int i = 0; i < 10; i++) {
      float weight = scale.get_units(1);  // 1회 측정
      Serial.println(weight, 2);  // 2자리 소수점까지 출력
      delay(200);  // 200ms 간격으로 측정
    }
  }

  // 시스템이 멈추면 아무 작업도 하지 않음
  if (systemStopped) {
    delay(100);
  }
}
