from nvdaBuiltin.appModules.wwahost import *

class AppModule(AppModule):

	def event_gainFocus(self, obj, nextHandler):
		import tones
		tones.beep(550, 50)
		nextHandler()
