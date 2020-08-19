## start
* start
  - utter_ask_name

## set_name
* set_name
  - utter_greet

## goodbye
* goodbye
  - utter_goodbye
  - action_restart

## thankyou
* thankyou
  - utter_noworries

## ask ability
* ask_ability
  - utter_show_ability

## praise
* praise
  - utter_happy

## decry
* decry
  - utter_sorry

## ask_forecast_weather
* ask_forecast_weather
  - action_weather

## ask_forecast_humidity
* ask_forecast_humidity
  - action_humidity

## ask_forecast_temperature
* ask_forecast_temperature
  - action_temperature

## New Story

* start
    - utter_ask_name
* set_name{"name":"Toàn"}
    - slot{"name":"Toàn"}
    - utter_greet
* ask_forecast_weather{"location":"Hà Nội"}
    - slot{"location":"Hà Nội"}
    - action_weather
    - slot{"day":null}
* ask_forecast_weather{"day":"hôm nay"}
    - slot{"day":"hôm nay"}
    - action_weather
    - slot{"day":null}
* ask_forecast_weather{"location":"Hồ Chí Minh","day":"ngày mai"}
    - slot{"day":"ngày mai"}
    - slot{"location":"Hồ Chí Minh"}
    - action_weather
    - slot{"day":null}
* praise
    - utter_happy

## New Story

* start
    - utter_ask_name
* set_name{"name":"Toàn"}
    - slot{"name":"Toàn"}
    - utter_greet
* ask_forecast_weather{"day":"hôm nay"}
    - slot{"day":"hôm nay"}
    - action_weather
    - slot{"day":null}
* ask_forecast_temperature{"location":"Hà Nội"}
    - slot{"location":"Hà Nội"}
    - action_temperature
    - slot{"day":null}
* ask_forecast_humidity{"day":"ngày mai"}
    - slot{"day":"ngày mai"}
    - action_humidity
    - slot{"day":null}
* ask_forecast_humidity{"day":"ngày mai","location":"Hồ Chí Minh"}
    - slot{"day":"ngày mai"}
    - slot{"location":"Hồ Chí Minh"}
    - action_humidity
    - slot{"day":null}
* praise
    - utter_happy
