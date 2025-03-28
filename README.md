[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![PyPI Version](https://img.shields.io/pypi/v/serial-communicator)](https://pypi.org/project/serial-communicator/)
[![Python Versions](https://img.shields.io/pypi/pyversions/serial-communicator)](https://pypi.org/project/serial-communicator/)
[![Downloads](https://img.shields.io/pypi/dm/serial-communicator)](https://pypi.org/project/serial-communicator/)

# Serial Communicator

Модуль для Python-проектов, обеспечивающий взаимодействие с микроконтроллером через COM-порт.

## Содержание

* [Описание](#chapter-0)
* [Требования](#chapter-1)
* [Установка](#chapter-2)
* [Использование](#chapter-3)
* [Дополнительные советы](#chapter-4)
* [Тестирование](#chapter-5)
* [Обратная связь](#chapter-6)

<a id="chapter-0"></a>

## Описание

Serial Communicator упрощает процесс установления связи с микроконтроллерами или другими устройствами через последовательный порт, предоставляет удобные для использования функции, позволяет абстрагироваться от деталей работы с COM-портом.

- Основан на `pySerial`
- Отправка команд без ожидания ответа
- Отправка команд с ожиданием ответа от контроллера
- Чтение команд от контроллера
- Автопоиск подключенного контроллера по всем доступным портам
- Гибкая настройка ретраев и таймаутов

<a id="chapter-1"></a>

## Требования

- Python 3.6 или выше
- pySerial

Для установки `pySerial` используйте следующую команду:

```bash
pip install pySerial
```

<a id="chapter-2"></a>

## Установка

Вы можете установить модуль напрямую с помощью `pip`:

```bash
pip install serial-communicator
```

Или клонировать репозиторий и установить из исходников:

```bash
git clone https://github.com/RadioPizza/serial_communicator.git
cd serial_communicator
pip install .
```

<a id="chapter-3"></a>

## Использование

Класс `SerialCommunicator` предназначен для взаимодействия с устройствами через последовательный порт. Ниже представлены примеры того, как можно использовать этот класс в вашем проекте.

### Инициализация и отправка команды

```Python
from serial_communicator import SerialCommunicator

# Параметры подключения
port_name = 'COM3'       # Замените на соответствующий порт
baudrate = 115200        # Скорость передачи данных
timeout = 1.0            # Таймаут чтения в секундах

# Создаем экземпляр SerialCommunicator
comm = SerialCommunicator(port=port_name, baudrate=baudrate, timeout=timeout)

# Отправляем команду и ожидаем ответ
command = "i"
expected_response = "OK"

success = comm.send_command(command, expected_response)
if success:
    print("Команда успешно отправлена и получен ожидаемый ответ.")
else:
    print("Не удалось получить ожидаемый ответ от устройства.")

# Закрываем соединение
comm.close()
```

### Использование в блоке with

Рекомендуется использовать контекстный менеджер `with` для автоматического закрытия порта независимо от того, произошла ошибка или нет.

```Python
from serial_communicator import SerialCommunicator

# Параметры подключения
port_name = 'COM3'
baudrate = 115200
timeout = 1.0

# Использование контекстного менеджера
with SerialCommunicator(port=port_name, baudrate=baudrate, timeout=timeout) as comm:
    command = "i"
    expected_response = "OK"

    success = comm.send_command(command, expected_response)
    if success:
        print("Команда успешно отправлена и получен ожидаемый ответ.")
    else:
        print("Не удалось получить ожидаемый ответ от устройства.")
```

### Автоматический поиск контроллера

Если вы не знаете, к какому порту подключено устройство, вы можете использовать cтатический метод `find_controller_port` для автоматического поиска.

```Python
from serial_communicator import SerialCommunicator

# Поиск порта с подключенным контроллером
port = SerialCommunicator.find_controller_port(
    command="i",
    expected_response="i",
    baudrate=115200,
    timeout=1.0,
    retries=5,
    delay=1.0,
    delay_between_ports=1.0
)

if port:
    print(f"Контроллер найден на порту: {port}")
    # Подключаемся к найденному порту
    with SerialCommunicator(port=port, baudrate=115200, timeout=1.0) as comm:
        # Дополнительные действия с устройством
        pass
else:
    print("Контроллер не найден.")
```

### Чтение ответа без отправки команды

Иногда необходимо просто прочитать данные из порта без отправки какой-либо команды.

```Python
from serial_communicator import SerialCommunicator

with SerialCommunicator(port='COM3', baudrate=115200, timeout=1.0) as comm:
    response = comm.read_response()
    if response:
        print(f"Получен ответ: {response}")
    else:
        print("Нет данных для чтения или произошла ошибка.")
```

### Обработка исключений

Для более надежной работы рекомендуется обрабатывать возможные исключения, связанные с последовательным портом.

```Python
from serial_communicator import SerialCommunicator
import serial

try:
    with SerialCommunicator(port='COM3', baudrate=115200, timeout=1.0) as comm:
        command = "i"
        expected_response = "OK"
        success = comm.send_command(command, expected_response)
        if success:
            print("Команда успешно отправлена и получен ожидаемый ответ.")
        else:
            print("Не удалось получить ожидаемый ответ от устройства.")
except serial.SerialException as e:
    print(f"Ошибка при работе с последовательным портом: {e}")
```
<a id="chapter-4"></a>

## Дополнительные советы

### Проверка доступных портов

Вы можете использовать `serial.tools.list_ports` для получения списка всех доступных последовательных портов.

```Python
import serial.tools.list_ports

ports = serial.tools.list_ports.comports()
for port in ports:
    print(f"Найден порт: {port.device}")
```

### Настройка логирования

Класс SerialCommunicator может использовать модуль logging для вывода отладочной информации. Настройте логирование в своем основном скрипте, если необходимо.

```Python
import logging

logging.basicConfig(level=logging.INFO)
```

<a id="chapter-5"></a>

## Тестирование

Для проверки и демонстрации работы модуля `Serial Communicator` в репозитории предусмотрен мок-контроллер, имитирующий поведение реального устройства. Он расположен в папке `ControllerMock` и представлен скетчем Arduino — `ControllerMock.ino`. С его помощью вы сможете протестировать функции модуля.

<a id="chapter-6"></a>

## Обратная связь

Мы всегда рады вашим предложениям и идеям по улучшению нашего проекта! Вы можете принять участие в его развитии следующими способами:

- Сообщите о найденных ошибках. Если вы обнаружили баг, пожалуйста, создайте **Issue**, указав в описании проблему, используемое оборудование и программное обеспечение. Это поможет нам быстро найти и исправить ошибку.

- Внесите свои предложения. Если у вас есть идеи по улучшению проекта, не стесняйтесь делиться ими!

- Отправьте **Pull Request**. Если вы решили внести улучшения или исправления непосредственно в коде, создайте **Pull Request**. Мы с удовольствием рассмотрим ваши изменения.

Ваши комментарии и участие помогут нам сделать проект лучше! Спасибо за вашу поддержку!

<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/RadioPizza/serial_communicator/blob/main/LICENSE
