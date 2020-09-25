## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbain"}
    - slot{"location": "Mumbain"}
    - action_chklocation
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "mumbai"}
    - utter_ask_email
* validate_email{"email": "sachin.worldlife@gmail.com"}
    - slot{"email": "sachin.worldlife@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - action_chklocation
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_chklocation
* restaurant_search{"location": "meerut"}
    - slot{"location": "meerut"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "meerut"}
    - utter_ask_email
* restaurant_search
    - utter_ask_email_again
* validate_email{"email": "pjain2411@gmail.com"}
    - slot{"email": "pjain2411@gmail.com"}
    - action_validate_email
    - slot{"email": "pjain2411@gmail.com"}
    - action_send_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - utter_ask_email
* affirm
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_budget
* restaurant_search{"budget": "More than 700"}
    - slot{"budget": "More than 700"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
    - utter_ask_email
* validate_email{"email": "sa#@f1n.com"}
    - slot{"email": "sa#@f1n.com"}
    - action_validate_email
    - slot{"email": null}
* validate_email{"email": "pjain2411@gmail.com"}
    - slot{"email": "pjain2411@gmail.com"}
    - action_validate_email
    - slot{"email": "pjain2411@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* validate_email
    - action_validate_email
    - slot{"email": null}
* validate_email{"email": "pjain2411@gmail.com"}
    - slot{"email": "pjain2411@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* validate_email{"email": "sachin.worldlife@gmail.com"}
    - slot{"email": "sachin.worldlife@gmail.com"}
    - action_validate_email
    - slot{"email": "sachin.worldlife@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_chklocation
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_budget
* restaurant_search{"budget": "Rs. 300 to 700"}
    - slot{"budget": "Rs. 300 to 700"}
    - action_search_restaurants
    - slot{"location": "delhi"}
    - utter_ask_email
* validate_email{"email": "sachin.worldlife@gmail.com"}
    - slot{"email": "sachin.worldlife@gmail.com"}
    - action_validate_email
    - slot{"email": "sachin.worldlife@gmail.com"}
    - action_send_email
* goodbye
    - utter_goodbye
