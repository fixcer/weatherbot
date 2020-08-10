import json

from typing import Dict, Text, Any, List, Union, Optional
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from unidecode import unidecode

class ActionWeather(Action):

	def name(self):
		return 'action_weather'


	def run(self, dispatcher, tracker, domain):
		from forecast import getWeather
		loc = tracker.get_slot('location')
		day = tracker.get_slot('day')

		string_to_day = [["hom nay", "bay gio", "luc nay", "ngay bay gio", "ngay luc nay", "hien tai"],
						["ngay mai", "hom sau", "mot ngay sau", "mot ngay nua", "1 ngay sau", "1 ngay nua"],
						["ngay kia", "hai ngay sau", "hai ngay nua", "2 ngay sau", "2 ngay nua"],
						["ba ngay sau", "ba ngay nua", "3 ngay sau", "3 ngay nua"],
						["bon ngay sau", "bon ngay nua", "4 ngay sau", "4 ngay nua"],
						["nam ngay sau", "nam ngay nua", "5 ngay sau", "5 ngay nua"],
						["sau ngay sau", "sau ngay nua", "6 ngay sau", "6 ngay nua"],
						["bay ngay sau", "bay ngay nua", "7 ngay sau", "7 ngay nua"],
						["tam ngay sau", "tam ngay nua", "8 ngay sau", "8 ngay nua"],
						["chin ngay sau", "chin ngay nua", "9 ngay sau", "9 ngay nua"],
						["muoi ngay sau", "muoi ngay nua", "10 ngay sau", "10 ngay nua"]]

		if loc:
			res = getWeather(loc)
			if isinstance(res, list):
				if day:
					day = unidecode(day).lower()
					for i in range(len(string_to_day)):
						if day in string_to_day[i]:
							day = i
							break

					if isinstance(day, str):
						dispatcher.utter_message("Tôi không thể nhận diện được ngày bạn muốn xem")
					else:
						dispatcher.utter_message(res[day])
				else:
					dispatcher.utter_message(res[0])
			else:
				dispatcher.utter_message("Vị trí này ngoài phạm vi của tôi rồi, tiếc quá")
		else:
			dispatcher.utter_message("Mời bạn nhập lại vị trí")
		
		return []
