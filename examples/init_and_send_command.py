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