# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
import pandas as pd 
from rasa_sdk import Action, Tracker
import numpy as np
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
from .db import create_connection_now
import re


class ValidateSimpleTicketForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_simple_ticket_form"

    def validate_ticketid(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `ticketid` value."""
        a=tracker.latest_message.get("text")
        uu = tracker.get_slot("url")
        print(uu)
    
        match = re.search("(http://[\d\.]+:\d+)", uu)
        if match:
            url = match.group(1)
            print(match.group(1))
        print(a)
        print(url)
        ticket = int(slot_value)
        print(ticket)
        try:
            conn = create_connection_now(url)
            query = f"select ticket_id,summary,user_name, assign_user_name,description,assign_user_name_to, status from ticket_system.vm_tik_status_report where ticket_id={ticket} order by assign_date desc limit 1"
            cursor = conn.cursor()
            cursor.execute(query,(ticket))
            result = cursor.fetchone()
            print('hi',result)
            # return {"requested_slot": None}
            msg = f"**Ticket id**: {result[0]}\n \n **Summary**:{result[1]}\n \n **User**:{result[2]}\n \n **Raised by**:{result[3]}\n \n **Description**: {result[4]}\n \n **Assigned to**:{result[5]}\n \n **Status**:{result[6]}"
            dispatcher.utter_message(text=msg)
            return {"ticketid": slot_value}
    
            # conn = create_connection()
        except:
            msg = "Problem with connection"
            dispatcher.utter_message(text=msg)
        return[]
        



        # query = f"select ticket_id,summary,user_name, assign_user_name,description,assign_user_name_to, status from ticket_system.vm_tik_status_report where ticket_id={ticket} order by assign_date desc limit 1"
        # cursor = conn.cursor()
        # cursor.execute(query,(ticket))
        # result = cursor.fetchone()
        # print('hi',result)



        # return {"requested_slot": None}



        # msg = f"**Ticket id**: {result[0]}\n \n **Summary**:{result[1]}\n \n **User**:{result[2]}\n \n **Raised by**:{result[3]}\n \n **Description**: {result[4]}\n \n **Assigned to**:{result[5]}\n \n **Status**:{result[6]}"
        # dispatcher.utter_message(text=msg)
        # return {"ticketid": slot_value}
    

# Import required libraries





class ActionTicketDetails(Action):

    def name(self) -> Text:
        return "action_ticket_details"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        empid = tracker.get_slot("empCode")
        print(empid)
        name = tracker.get_slot("empName")
        print(name)
        uu = tracker.get_slot("url")
        # url = uu[0:21]
        print(uu)
        msg = f"Hello! {name}, your employee id is {empid} "
        dispatcher.utter_message(text=msg)
        msg = f"Getting the ticket details"
        dispatcher.utter_message(text=msg)

        return []
    



class ActionTicketSummary(Action):

    def name(self) -> Text:
        return "action_ticket_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        empid = tracker.get_slot("empCode")
        print(empid)
        name = tracker.get_slot("empName")
        print(name)
        uu = tracker.get_slot("url")
        # url = uu[0:21]
        print(uu)
        msg = f"Hello! {name}, your employee id is {empid} "
        dispatcher.utter_message(text=msg)
        msg = f"Getting the ticket summary"
        dispatcher.utter_message(text=msg)

        return []


class ActionLeaveBalance(Action):

    def name(self) -> Text:
        return "action_leave_balance"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        empid = tracker.get_slot("empCode")
        print(empid)
        name = tracker.get_slot("empName")
        print(name)
        uu = tracker.get_slot("url")
        # url = uu[0:21]
        print(uu)
        msg = f"Hello! {name}, your employee id is {empid} "
        dispatcher.utter_message(text=msg)
        msg = f"Getting the leave balance"
        dispatcher.utter_message(text=msg)

        return []




class ActionHolidayList(Action):

    def name(self) -> Text:
        return "action_holiday_list"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        empid = tracker.get_slot("empCode")
        print(empid)
        name = tracker.get_slot("empName")
        print(name)
        uu = tracker.get_slot("url")
        # url = uu[0:21]
        print(uu)
        msg = f"Hello! {name}, your employee id is {empid} "
        dispatcher.utter_message(text=msg)
        msg = f"Getting the holiday List"
        dispatcher.utter_message(text=msg)

        return []




from rasa_sdk.events import AllSlotsReset, SlotSet

class ActionResetAllSlots(Action):

    def name(self):
        return "action_reset_all_slots"

    def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slots = []
        slots_to_keep = ["empCode", "empName","url"]
        for key, value in tracker.current_slot_values().items():
            if value is not None and key not in slots_to_keep:
                slots.append(SlotSet(key=key, value=None))

        return slots
# from rasa_sdk.forms import FormValidationAction

# class ticketFormAction(Action):
#     def name(self) -> Text:
#         return "ticket_form"

#     def run(
#         self, dispatcher, tracker, domain
#     ) -> List[Dict[Text, Any]]:
#         return [FormAction("ticket_form")]

# class ConfirmPizzaOrder(Action):
#     def name(self) -> Text:
#         return "confirm_ticket_order"

#     def run(
#         self, dispatcher, tracker, domain
#     ) -> List[Dict[Text, Any]]:
#         ticket = tracker.get_slot("ticket_id")
#         # user = tracker.get_slot("user_id")
#         # quantity = tracker.get_slot("quantity")

#         message = f"the ticket id and user id are {ticket} {user} {pizza_type}. "
#         dispatcher.utter_message(message)

#         return []


# class ValidateTicketForm(Action):
#     def name(self) -> Text:
#         return "validate_ticket_form"

#     def run(
#         self, dispatcher, tracker, domain
#     ) -> List[Dict[Text, Any]]:
#         slots_to_validate = ["ticket_id"]
#         for slot_name in slots_to_validate:
#             if tracker.slots.get(slot_name) is None:
#                 dispatcher.utter_message(template=f"utter_ask_{slot_name}")
#                 return [SlotSet("requested_slot", slot_name)]

#         return [SlotSet("requested_slot", None)]

        

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import UserUtteranceReverted
# from rasa_sdk.executor import CollectingDispatcher

# class ActionDefaultFallback(Action):
    # """Executes the fallback action and goes back to the previous state
    # of the dialogue"""

    # def name(self) -> Text:
    #     return ACTION_DEFAULT_FALLBACK_NAME

    # async def run(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> List[Dict[Text, Any]]:
    #     dispatcher.utter_message(template="my_custom_fallback_template")

        # Revert user message which led to fallback.
        # return [UserUtteranceReverted()]

    # def validate_pizza_type(
    #     self,
    #     slot_value: Any,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: DomainDict,
    # ) -> Dict[Text, Any]:
    #     """Validate `pizza_type` value."""

    #     if slot_value not in ALLOWED_PIZZA_TYPES:
    #         msg = "I don't recognize that pizza."
    #         msg += f"We only serve {'/'.join(ALLOWED_PIZZA_TYPES)}."
    #         dispatcher.utter_message(msg)
    #         return {"pizza_type": None}
    #     dispatcher.utter_message(text=f"OK! You want to have a {slot_value} pizza.")
    #     return {"pizza_type": slot_value}


# class ActionAssetDetails(Action):

#     def name(self) -> Text:
#         return "action_asset_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         empid = tracker.get_slot("empCode")
#         print(empid)
#         name = tracker.get_slot("empName")
#         print(name)
#         uu = tracker.get_slot("url")
#         url = uu[0:21]
#         print(url)
#         msg = f"Hello! Your name is {name} and your id id {empid} "
#         dispatcher.utter_message(text=msg)

#         return []


    
# class ActionAttendanceDetails(Action):

#     def name(self) -> Text:
#         return "action_attendance_details"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         empid = tracker.get_slot("empCode")
#         print(empid)
#         name = tracker.get_slot("empName")
#         print(name)
#         uu = tracker.get_slot("url")
#         url = uu[0:21]
#         print(url)
#         msg = f"Hello! Your name is {name} and your id id {empid} "
#         dispatcher.utter_message(text=msg)
#         return []
    
    
# def generate_pdf(name, email, message):
#     # Set up the canvas
#     c = canvas.Canvas(name+".pdf", pagesize=letter)

#     # Draw the text on the canvas
#     c.drawString(100, 750, "Name: {}".format(name))
#     c.drawString(100, 700, "Email: {}".format(email))
#     c.drawString(100, 650, "Message: {}".format(message))

#     # Save the PDF file
#     c.save()


# class ActionRole(Action):

#     def name(self) -> Text:
#         return "action_role"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         empid = tracker.get_slot("empCode")
#         print(empid)
#         email = empid
        
#         name = tracker.get_slot("empName")
#         print(name)
#         uu = tracker.get_slot("url")
#         # url = uu[0:21]
#         message = uu
#         url = uu
#         print(url)
#         df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
#         generate_pdf(name, email, message)
#         df.to_csv('payslip.csv')
#         # pdflink = 
#         pdflink = f"<a href= 'C:/Aman/ras/HRMS_Bot/{name}.pdf' download>Download PDF</a>"
#         # pdflink = f"file:///C:/Aman/ras/HRMS_Bot/{name}.pdf"
#         if name == 'Amandeep':
#             buttons = [{"title": "Contact Details", "payload": "/contact_details"},
#                        {"title": "Asset Details", "payload": "/asset_details"},
#                        {"title": "Ticket Details", "payload": "/ticket_details"},
#                        {"title": "Attendance Details", "payload": "/attendance_details"},
#                    {"title": "Leave Details", "payload": "/leave_details"}]
#             msg = f"Hello! {name}. What would you like to know ?  "
#             dispatcher.utter_message(text=msg, buttons=buttons)
#             dispatcher.utter_message(text=pdflink)
#             return []
#         else:
#             pass
#         buttons = [{"title": "Attendance Details", "payload": "/attendance_details"},
#                    {"title": "Leave Details", "payload": "/leave_details"}]
#         msg = f"Hello! {name}. What would you like to know ? "
#         dispatcher.utter_message(text=msg, buttons=buttons)

#         return []

# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.events import UserUtteranceReverted
# from rasa_sdk.executor import CollectingDispatcher

# class ActionDefaultFallback(Action):
#     """Executes the fallback action and goes back to the previous state
#     of the dialogue"""

    # def name(self) -> Text:
    #     return ACTION_DEFAULT_FALLBACK_NAME

    # async def run(
    #     self,
    #     dispatcher: CollectingDispatcher,
    #     tracker: Tracker,
    #     domain: Dict[Text, Any],
    # ) -> List[Dict[Text, Any]]:
    #     dispatcher.utter_message(template="my_custom_fallback_template")

    #     # Revert user message which led to fallback.
    #     return [UserUtteranceReverted()]