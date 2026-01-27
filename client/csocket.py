import socket

class ClientSocket:
    def __init__(self):
        self.csoket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = 'localhost'
        self.port = 12345
        self.response = False

    def connect(self):
        """Создание TCP соединения."""
        logging.info(f"Подключение к {self.host}:{self.port}...")
        try:
            self.csoket.connect((self.host, self.port))
            logging.info("Подключение установлено.")
        except Exception as e:
            logging.error(f"Ошибка при подключении: {e}")
            raise  # Прерываем выполнение, если подключение не удалось

    def transmit(self, message):
        """Передача параметров конфигурационных файлов."""
        logging.info(f"Отправка данных: {message}")
        try:
            self.csoket.send(message.encode())
            data = self.csoket.recv(1024).decode()
            logging.info(f"Ответ от сервера: {data}")
            self.response = True
        except Exception as e:
            logging.error(f"Ошибка передачи данных: {e}")

    def close_transmit(self):
        """Закрытие соединения."""
        if self.response:
            logging.info("Закрытие соединения с сервером.")
            self.csoket.close()