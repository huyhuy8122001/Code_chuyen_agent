from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


from datetime import datetime
import json
import re
import random

from agents_db import list_agent
from REGEX import create_pattern

class ActionHandOver(Action):
    def name(self) -> Text:
        return "action_handover"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        list_agent_id = []
        list_agent_name = []
        agent_obj = []

        agents = list_agent()

        current_name_agent = next(tracker.get_latest_entity_values("agent"), None)
        #print(current_name_agent)
        if current_name_agent == None:
            dispatcher.utter_message(response="utter_handover")
            return

        for i in range(len(agents)):
            pattern = create_pattern(agents[i]['name'])
            if re.search(pattern, current_name_agent,flags=re.I):
                #dispatcher.utter_message('id: {}'.format(agents[i]['id']))
                list_agent_id.append(agents[i]['id'])

        if len(list_agent_id) == 0:
            dispatcher.utter_message("Không tìm thấy agent @@")
        else:
            dispatcher.utter_message("id: {}".format(random.choice(list_agent_id)))


        # print(current_name_agent)
        print(list_agent_id)
