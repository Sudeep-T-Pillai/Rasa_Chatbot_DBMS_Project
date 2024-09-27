# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from typing import Text,Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet


class ActionRegisterUser(Action):
    def name(self) -> Text:
        return "action_register_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy registration action
        dispatcher.utter_message(text="Your account has been successfully registered!")
        return []


class ActionLoginUser(Action):
    def name(self) -> Text:
        return "action_login_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy login action
        dispatcher.utter_message(text="You have successfully logged into your account!")
        return []


class ActionSearchProduct(Action):
    def name(self) -> Text:
        return "action_search_product"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy product search action
        product = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Searching for {product}...")
        return []


class ActionAddPayment(Action):
    def name(self) -> Text:
        return "action_add_payment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy add payment method action
        dispatcher.utter_message(text="Payment method has been added.")
        return []


class ActionDeletePayment(Action):
    def name(self) -> Text:
        return "action_delete_payment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy delete payment action
        dispatcher.utter_message(text="Payment method deleted.")
        return []
        

class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy place order action
        dispatcher.utter_message(text="Your order has been successfully placed!")
        return []


class ActionAddToCart(Action):
    def name(self) -> Text:
        return "action_add_to_cart"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy add to cart action
        dispatcher.utter_message(text="Product added to cart.")
        return []


class ActionTrackOrder(Action):
    def name(self) -> Text:
        return "action_track_order"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy order tracking action
        dispatcher.utter_message(text="Your order is on the way.")
        return []


class ActionCheckDelivery(Action):
    def name(self) -> Text:
        return "action_check_delivery"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy check delivery action
        location = tracker.latest_message['text']
        dispatcher.utter_message(text=f"Delivery is available to {location}.")
        return []


class ActionCheckCOD(Action):
    def name(self) -> Text:
        return "action_check_cod"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy COD availability check
        dispatcher.utter_message(text="Cash on Delivery is available for this product.")
        return []

