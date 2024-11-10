import re
import requests
from typing import Text,Any, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet



# Global stack list
stack_list = []
POCKETBASE_URL = "http://23.21.225.129:8090"  # Replace with your PocketBase URL
COLLECTION_NAME = "order_items"
API_TOKEN = "your_api_token"

def add_item(item):
    stack_list.insert(0, item)
    print(f"Added {item} to the stack")

def peek():
    if stack_list:
        return stack_list[0]
    else:
        return "Stack is empty"    

def view_items(dispatcher, position=None):
    if not stack_list:
        dispatcher.utter_message(text="The stack is empty.")
        return

    if position is None:
        # Show all items from top to bottom
        messages = [f"{index + 1}. {item}" for index, item in enumerate(stack_list)]
        dispatcher.utter_message(text="Stack from top to bottom:\n" + "\n".join(messages))
    else:
        try:
            index = len(stack_list) - position
            if index < 0 or index >= len(stack_list):
                dispatcher.utter_message(text=f"Invalid position. Stack has {len(stack_list)} items.")
            else:
                dispatcher.utter_message(text=f"Item at position {position} from bottom: {stack_list[index]}")
        except ValueError:
            dispatcher.utter_message(text="Invalid position. Please provide a number.")

class Action_view_list(Action):
    def name(self) -> Text:
        return "action_view_list"
    
    async def run(self, dispatcher, tracker, domain) -> List[Dict[Text, Any]]:
        # Get position from tracker slots if provided, otherwise None
        position = tracker.get_slot("position")
        if position:
            try:
                # Convert position to an integer if it exists
                position = int(position)
            except ValueError:
                dispatcher.utter_message(text="Invalid position. Please provide a number.")
                
                return [SlotSet("position", None)]

        # Call the global view_items function with dispatcher and position
        view_items(dispatcher, position)

        return [SlotSet("position", None)]


               
class ActionSearchProduct(Action):
    def name(self) -> Text:
        return "action_search_product"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        product = tracker.get_slot("product")
        
        if not product:
            dispatcher.utter_message(text="I'm sorry, I didn't catch the product you're looking for.")
            return []

        dispatcher.utter_message(text=f"Searching for {product}...")

        url = "https://api.ebay.com/buy/browse/v1/item_summary/search"
        headers = {
            "Authorization": "Bearer v^1.1#i^1#f^0#I^3#r^0#p^3#t^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",  # Use your OAuth token
            "Content-Type": "application/json",
            "X-EBAY-C-ENDUSERCTX": "contextualLocation=country=IN"
        }
        params = {
            "q": product,
            "limit": 5
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            if 'itemSummaries' in data:
                for item in data['itemSummaries']:
                    title = item.get('title')
                    price = item.get('price', {}).get('value')
                    currency = item.get('price', {}).get('currency')
                    item_url = item.get('itemHref')
                    image_url = item.get('image', {}).get('imageUrl')

                    message = f"**Product:** {title}\n**Price:** {price} {currency}\n[View Item]({item_url})\n![Image]({image_url})"
                    add_item(message)
                    dispatcher.utter_message(text=message)
            else:
                dispatcher.utter_message(text="No products found.")
        else:
            dispatcher.utter_message(text="Failed to retrieve products from eBay.")
        return []



class ActionLoginUser(Action):
    def name(self) -> Text:
        return "action_login_user"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy login action
        dispatcher.utter_message(text="You have successfully logged into your account!")
        return []


class ActionAddPayment(Action):
    def name(self) -> Text:
        return "action_add_payment"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy add payment method action
        dispatcher.utter_message(text="Payment method has been added.")
        return []


class ActionPlaceOrder(Action):
    def name(self) -> Text:
        return "action_place_order"

    async def run(self, dispatcher: CollectingDispatcher,
                  tracker: Tracker,
                  domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Ensure stack_list has items and product_index is valid
        product_index = int(tracker.get_slot("product_cart")) # Use an appropriate index if it's dynamically set
        if not stack_list or product_index >= len(stack_list):
            dispatcher.utter_message(text="Product not found in stack.")
            return []

        # Extract the product information from stack_list
        selected_product_message = stack_list[product_index]
        title_match = re.search(r"\*\*Product:\*\* (.+)", selected_product_message)
        price_match = re.search(r"\*\*Price:\*\* ([\d.]+)", selected_product_message)

        # Ensure matches were found
        if title_match and price_match:
            product_name = title_match.group(1)
            price = float(price_match.group(1))

            # Prepare data to send to PocketBase
            data = {
                "pdt_id": product_name,
                "price": price,
                "quantity": 1,
                "order_id": "3nvy8qeoeu9f42t"  # Use a unique order ID
            }

            # Send data to PocketBase collection
            response = requests.post(
                f"{POCKETBASE_URL}/api/collections/{COLLECTION_NAME}/records",
                json=data,
                headers={"Authorization": f"Bearer {API_TOKEN}"}
            )

            # Check if the request was successful
            if response.status_code == 200:
                dispatcher.utter_message(text=f"Added {product_name} with price {price} to Orders")
            else:
                dispatcher.utter_message(text=f"Failed to add {product_name}: {response.status_code} - {response.text}")
        else:
            dispatcher.utter_message(text="Failed to find product name or price.")

        return []



        # POCKETBASE_URL = "http://23.21.225.129:8090/api/collections/_pb_users_auth_/records"
        # ADMIN_TOKEN = "1209600"

        # user_id = "test@example.com"
        # product_cart = tracker.get_slot("product_cart")

        # # Check if product_cart is empty
        # if not product_cart:
        #     dispatcher.utter_message(text="Please specify a product number.")
        #     return []

        # try:
        #     product_index = int(product_cart)
        # except ValueError:
        #     dispatcher.utter_message(text="Product number must be a valid integer.")
        #     return []

        # # Validate product index
        # if product_index >= len(stack_list):
        #     dispatcher.utter_message(text="Item is out of the cart range.")
        #     return []

        # # Extract details from the selected product message
        # selected_product_message = stack_list[product_index]
        # title = re.search(r"\*\*Product:\*\* (.+)", selected_product_message)
        # price = re.search(r"\*\*Price:\*\* ([\d.]+)", selected_product_message)
        # currency = re.search(r"\*\*Price:\*\* [\d.]+ (\w+)", selected_product_message)
        # item_url = re.search(r"\[View Item\]\((.*?)\)", selected_product_message)
        # image_url = re.search(r"!\[Image\]\((.*?)\)", selected_product_message)

        # # If any of the components are missing, return an error
        # if not all([title, price, currency, item_url, image_url]):
        #     dispatcher.utter_message(text="Could not parse the selected product details.")
        #     return []

        # # Extracted product details
        # order_com = {
        #     "title": title.group(1),
        #     "price": float(price.group(1)),
        #     "currency": currency.group(1),
        #     "item_url": item_url.group(1),
        #     "image_url": image_url.group(1)
        # }

        # # Prepare payload for the order
        # order_payload = {
        #     "user_id": user_id,
        #     "quantity": 1,
        #     "price": order_com["price"]
        # }

        # # Send POST request to Pocketbase
        # headers = {"Authorization": f"Bearer {ADMIN_TOKEN}"}
        # response = requests.post(POCKETBASE_URL, json=order_payload, headers=headers)

        # if response.status_code == 200:
        #     dispatcher.utter_message(text="Order has been placed successfully.")
        #     return [SlotSet("order_com", order_com)]
        # else:
        #     dispatcher.utter_message(text="Failed to place the order.")
        #     return []


class ActionAddToCart(Action):
    def name(self) -> Text:
        return "action_add_to_cart"
    
    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
        # Dummy order tracking action
        dispatcher.utter_message(text="Product added to the cart.")
        return []

    # def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[Dict[Text, Any]]:
    #     # Get the position from the slot
    #     position = tracker.get_slot("position")
        
    #     # Determine the cart item based on position
    #     if position == 'this':
    #         cart_item = peek()  # Get the topmost item
    #         add_item(cart_item)
    #     else:
    #         try:
    #             # Try converting position to an integer
    #             position = int(position)
    #             # Retrieve the specific item from stack_list based on position
    #             cart_item = stack_list[len(stack_list) - position] if 0 <= position <= len(stack_list) else None
    #             add_item(cart_item)
    #         except (ValueError, IndexError):
    #             cart_item = None

    #     # Check if a valid item was found
    #     if cart_item:
    #         dispatcher.utter_message(text=f"Adding the Product: {cart_item} to cart")
    #         print(cart_item)
    #         # Here you could add logic to process the order, update the database, etc.
            
    #     else:
    #         dispatcher.utter_message(text="The specified item position is invalid or the stack is empty.")

    #     return [SlotSet("position", None)]


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

