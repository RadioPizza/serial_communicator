from serial_communicator import SerialCommunicator

with SerialCommunicator(port='COM3', baudrate=115200, timeout=1.0) as comm:
    response = comm.read_response()
    if response:
        print(f"Получен ответ: {response}")
    else:
        print("Нет данных для чтения или произошла ошибка.")