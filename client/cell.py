from client.parser import Parser

class Cell(Parser):
	def __init__(self, config_file):
		super().__init__(config_file)

	def load(self):
		super().load()

	def get_config(self):
		return self.config