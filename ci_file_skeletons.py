import sublime, sublime_plugin

class ControllerNamePromptCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Enter Controller Name: ", "Controller", 
			self.on_done, None, None)
		pass

	def on_done(self, text):
		view = self.window.new_file()
		view.set_name(text.lower() + ".php")
		view.run_command("insert_snippet", 
			{ "name": "Packages/CI_File_Skeletons/ci_controller.sublime-snippet" 
			})
		view.run_command("insert", {"characters": text.capitalize()})
		view.run_command("next_field")
		view.run_command("insert", {"characters": text.lower()})
		sublime.status_message(sublime.installed_packages_path())

class ModelNamePromptCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Enter Model Name: ", "Model", 
			self.on_done, None, None)
		pass

	def on_done(self, text):
		view = self.window.new_file()
		view.set_name(text.lower() + "_model.php")
		view.run_command("insert_snippet", 
			{ "name": "Packages/CI_File_Skeletons/ci_model.sublime-snippet"})
		view.run_command("insert", {"characters": text.capitalize()})
		view.run_command("next_field")
		view.run_command("insert", {"characters": text.lower()})
		sublime.status_message(sublime.installed_packages_path())

class MigrationNamePromptCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("Enter Migration Name: ", "000_migration", 
			self.on_done, None, None)
		pass

	def on_done(self, text):
		view = self.window.new_file()
		view.set_name(text.lower() + ".php")

		split = text[4:]
		view.run_command("insert_snippet", 
			{ "name": "Packages/CI_File_Skeletons/ci_migration.sublime-snippet" 
			})
		view.run_command("insert", {"characters": split.capitalize()})
		view.run_command("next_field")
		view.run_command("insert", {"characters": text.lower()})
		sublime.status_message(sublime.installed_packages_path())