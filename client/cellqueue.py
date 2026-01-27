from client.parser import Parser


class CellQueue(Parser):
	def __init__(self, config_file):
		super().__init__(config_file)
		self.queue = []

	def load(self):
		super().load()
		self.validate()

	def validate(self):
		for key in self.config:
			self.queue = self.config[key]

	def get_queue(self):
		return self.queue
