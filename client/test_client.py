from cell import Cell
from cellqueue import CellQueue
from action import Action

from pathlib import Path

def find_file_by_name(directory: str, filename: str) -> Path | None:
    path = Path(directory)

    for file in path.iterdir():
        if file.is_file() and file.name == filename:
            return file.resolve()

    return None

def main():
	queue = {}
	cellqueue = CellQueue('/home/jackpot/projects/Brute-Ban/config/bruteban.conf')
	cellqueue.load()
	cell_queue = cellqueue.get_queue()        
	for i in cell_queue:
		cell = Cell(find_file_by_name("/home/jackpot/projects/Brute-Ban/config", i))
		cell.load()
		queue[i] = cell.get_config()
	print(queue)
if __name__ == "__main__":
	main()