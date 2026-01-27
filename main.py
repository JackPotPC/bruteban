import os
import threading
import signal
from client.cell import Cell
from client.cellqueue import CellQueue
from server.logmonitor import LogMonitor
from utils import find_file_by_name, setup_logger, get_logger

log = get_logger(__name__)

class BruteBan:
    def __init__(self):
        self.queue = {}
        self.threads = []
        self.log_monitor = LogMonitor()
        self.setup()

    def setup(self):
        log.info("Настройка сервиса...")
        cellqueue = CellQueue("/home/jackpot/projects/Brute-Ban/config/bruteban.conf")
        cellqueue.load()
        cell_queue = cellqueue.get_queue()
        for i in cell_queue:
            cell = Cell(find_file_by_name("/home/jackpot/projects/Brute-Ban/config", i))
            cell.load()
            self.queue[i] = cell.get_config()
        log.info("Сервис настроен.")
        log.info(f"Список сервисов для мониторинга:{self.queue}")

    def start(self):
        log.info("Запуск мониторинга...")
        for cell in self.queue:
            thread = threading.Thread(target=self.log_monitor.monitoring, args=(self.queue[cell],))
            thread.daemon = False
            self.threads.append(thread)
            thread.start()
        log.info("Мониторинг запущен.")


    def stop(self):
        self.log_monitor.stop()
        for thread in self.threads:
            thread.join()


if __name__ == "__main__":
    setup_logger()
    bruteban = BruteBan()
    bruteban.start()