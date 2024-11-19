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