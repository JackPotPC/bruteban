import threading
from pathlib import Path
from bruteban.cell import Cell
from bruteban.cellqueue import CellQueue
from bruteban.logmonitor import LogMonitor
from utils import find_file_by_name, setup_logger, get_logger

log = get_logger(__name__)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CONFIG_DIR = PROJECT_ROOT / "config"
CONFIG_FILE = CONFIG_DIR  / "bruteban.conf"
ACTION_DIR = PROJECT_ROOT / "scripts"


class BruteBan:
    def __init__(self):
        self.queue = {}
        self.threads = []
        self.log_monitor = LogMonitor()
        self.setup()

    def setup(self):
        log.info("Настройка сервиса...")
        cellqueue = CellQueue(CONFIG_FILE)
        cellqueue.load()
        cell_queue = cellqueue.get_queue()
        for i in cell_queue:
            cell = Cell(find_file_by_name(CONFIG_DIR, i))
            cell.load()
            self.queue[i] = cell.get_config()
        log.info("Сервис настроен.")
        log.info(f"Список сервисов для мониторинга:{self.queue}")

    def start(self):
        log.info("Запуск мониторинга...")
        for cell in self.queue:
            thread = threading.Thread(target=self.log_monitor.monitoring, args=(self.queue[cell], ACTION_DIR,))
            thread.daemon = False
            self.threads.append(thread)
            thread.start()
        log.info("Мониторинг запущен.")


    def stop(self):
        self.log_monitor.stop()
        for thread in self.threads:
            thread.join()