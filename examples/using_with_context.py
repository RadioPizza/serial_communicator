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