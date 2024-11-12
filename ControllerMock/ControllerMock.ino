// Имитация реального контроллера 

#define BAUD_RATE 115200    // Скорость передачи данных
#define LED_PIN 9           // Пин, к которому подключен светодиод
#define RESPONSE_DELAY 50   // Задержка перед ответом, мс

bool ledState = false;  // Состояние светодиода (включен/выключен)
int brightness = 100;   // Яркость в процентах (от 0 до 100)

void setup() {
  Serial.begin(BAUD_RATE);
  pinMode(LED_PIN, OUTPUT);
  updateLED();
}

void loop() {
  if (Serial.available() > 0) {
    handleCommand(Serial.readStringUntil('\n'));
  }
}

void updateLED() {
  int pwmValue = ledState ? map(brightness, 0, 100, 0, 255) : 0;
  analogWrite(LED_PIN, pwmValue);
}

void handleCommand(String command) {
  command.trim(); // Удаляем лишние символы

  if (command == "i") {
    respondWithDelay("i");
  } else if (command == "S") {
    ledState = true;
    updateLED(ledState);
    respondWithDelay("S");
  } else if (command == "s") {
    ledState = false;
    updateLED(ledState);
    respondWithDelay("s");
  } else if (command.startsWith("p")) {
    respondWithDelay(command);
    handleBrightnessCommand(command.substring(1));
  } else {
    respondWithDelay("E1");  // Неизвестная команда
  }
}

void respondWithDelay(String message) {
  delay(RESPONSE_DELAY);
  Serial.println(message);
}

void handleBrightnessCommand(String valueStr) {
  int value = valueStr.toInt();
  if (value >= 0 && value <= 100) {
    brightness = value;
    updateLED();
  } else {
    Serial.println("E2");  // Некорректное значение яркости
  }
}
