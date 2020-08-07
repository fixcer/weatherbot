import json

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class ActionWeather(Action):

	def name(self):
		return 'action_weather'


	def run(self, dispatcher, tracker, domain):
		from forecast import getWeather
		loc = tracker.get_slot('location')
		if loc:
			res = getWeather(loc)
			if isinstance(res, list):
				dispatcher.utter_message(res[0])
			else:
				dispatcher.utter_message("Vị trí này ngoài phạm vi của tôi rồi, tiếc quá")
		else:
			dispatcher.utter_message("Mời bạn nhập lại vị trí")
		
		return []
