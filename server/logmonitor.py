from systemd import journal
from utils import get_logger


log = get_logger(__name__)


class LogMonitor:
	def __init__(self):
		# self.stream = stream
		# self.action = action
		# self.bantime = bantime
		# self.regex = regex
		pass

	def start(self):
		self.monitoring()

	def monitoring(self, cell):
		j = journal.Reader()
		j.add_match(_SYSTEMD_UNIT=cell['systemd_unit_name'])
		j.seek_tail()
		j.get_next()
		while True:
			j.wait()
			for entry in j:
				message = entry.get("MESSAGE", "")
				print(message)
				match = self.regex.search(log_line)
				if match:
					log.warning("Найдено совпадение")
					self.action
