# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from datetime import datetime
import pytz

from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr

wl_session = WolframLanguageSession()


class ActionTellTime(Action):

    def name(self) -> Text:
        return "action_tell_time"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        city = tracker.slots["city"]
        if city == "":
            city = "Berlin"

        wl_session.evaluate(wlexpr('city = Interpreter["City"]["' + city + '"]'))
        tz_spec = wl_session.evaluate(wlexpr('Last@city["TimeZone"]'))

        #dispatcher.utter_message(f"Your tz_spec is '{tz_spec}'.")

        utc_now = pytz.utc.localize(datetime.utcnow())
        loc_now = utc_now.astimezone(pytz.timezone(tz_spec))

        dispatcher.utter_message(f"It is {loc_now.strftime('%H:%M')} in {city}.")

        next_dst_shift = wl_session.evaluate(wlexpr(
            """
            ToString[
                Round@UnitConvert[
                    DateDifference[
                        Now, 
                        city["NextDSTShift"]],
                        MixedUnit[{"Months", "Days", "Hours"}]
                ]
            ]
            """
        ))

        dispatcher.utter_message(f"There, the next DST shift will occur in {next_dst_shift}.")
