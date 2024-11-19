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