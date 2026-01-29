import re
from systemd import journal


class LogMonitor:
	def __init__(self):
		pass

	def monitoring(self):
		j = journal.Reader()
		j.add_match(_SYSTEMD_UNIT='sshd.service')
		j.seek_tail()
		j.get_next()
		filter_pattern = re.compile(rf"Failed password", re.IGNORECASE)
		extract_pattern = re.compile(rf"ip", re.IGNORECASE)
		while True:
			j.wait()
			for entry in j:
				message = entry.get("MESSAGE", "")
				print(message)
				if filter_pattern.search(message):
					print("Найдено совпадение")
					extract = extract_pattern.search(message)

l = LogMonitor()
l.monitoring()
