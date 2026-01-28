import subprocess
import os
from pathlib import Path

class Action():
	def __init__(self, action, action_dir):
		self.action = action / action_dir
		self._file_exists()
		self._file_executable()

	def _file_exists(self):
		if self.action.exists():
			return
		else:
			raise FileNotFoundError(f"Файл не найден.")

	def _file_executable(self):
		if os.access(self.action, os.X_OK):
			return
		else:
			raise PermissionError(f"{self.action} is not executable")

	def execute_action():
		subprocess.run(["bash", self.action], check=True)

