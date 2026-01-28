import re
from systemd import journal

from utils import get_logger
from bruteban.action import Action

log = get_logger(__name__)


class LogMonitor:
	def __init__(self):
		pass

	def start(self):
		self.monitoring()

	def monitoring(self, cell, action_dir):
		j = journal.Reader()
		j.add_match(_SYSTEMD_UNIT=cell['systemd_unit_name'])
		j.seek_tail()
		j.get_next()
		filter_pattern = re.compile(rf"{cell['filter']}", re.IGNORECASE)
		extract_pattern = re.compile(rf"{cell['extract']}", re.IGNORECASE)
		action = Action(cell['action'], action_dir)
		while True:
			j.wait()
			for entry in j:
				message = entry.get("MESSAGE", "")
				log.info(message)
				if filter_pattern.search(message):
					log.warning("Найдено совпадение")
					extract = extract_pattern.search(message)
					action.execute_action()
