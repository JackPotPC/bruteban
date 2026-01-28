from bruteban.bruteban import BruteBan
from utils import setup_logger

if __name__ == "__main__":
    setup_logger()
    bruteban = BruteBan()
    bruteban.start()