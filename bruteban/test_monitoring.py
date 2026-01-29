import re
from systemd import journal


class LogMonitor:
	def __init__(self):
		pass

	def monitoring(self):
		j = journal.Reader()
		j.add_match(_SYSTEMD_UNIT='sshd.service')
		j.get_next()
		while True:
			j.wait()
			for entry in j:
				message = entry.get("MESSAGE", "")
				print(message)

l = LogMonitor()
l.monitoring()


#