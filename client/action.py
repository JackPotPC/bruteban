import subprocess

from client.parser import Parser

class Action(Parser):
	def __init__(self, action):
		super().__init__()
		self.action = action
		self.shell = True

	def get_action():
		self.load_config(self.action)
		self.read_file()

	def execute_action():
		subprocess.run(["bash", self.action], check=True)

