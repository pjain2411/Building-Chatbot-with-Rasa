from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import re

class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'
		
	def run(self, dispatcher, tracker, domain):
		global emailBody
		count=0
		config={ "user_key":"f4924dc9ad672ee8c4f8c84743301af5"}
		zomato = zomatopy.initialize_app(config)
		loc = tracker.get_slot('location')
		cuisine = tracker.get_slot('cuisine')
		budget = tracker.get_slot('budget')
		location_detail=zomato.get_location(loc, 1)
		d1 = json.loads(location_detail)
		lat=d1["location_suggestions"][0]["latitude"]
		lon=d1["location_suggestions"][0]["longitude"]
		cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
		results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 1000)
		d = json.loads(results)
		response=""
		dispatcher.utter_message("---------------------------------------")
		dispatcher.utter_message("Searching for restaurants...")
		if d['results_found'] == 0:
			response= "No restaurant found for your criteria"
			dispatcher.utter_message(response)
		else:
			if budget== "Lesser than Rs. 300":
				for restaurant in sorted(d['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
				#for restaurant in d['restaurants']:
					if((restaurant['restaurant']['average_cost_for_two'] < 300) and (count<5)):
							response=response+str(count+1)+" Found "+ restaurant['restaurant']['name']+ " in "+restaurant['restaurant']['location']['address']+" has been rated "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n\n"
							count = count+1
							#dispatcher.utter_message("<300---------------------------------------")

			elif budget== "Rs. 300 to 700":
				#dispatcher.utter_message("odssf---------------------------------------")
				for restaurant in sorted(d['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
				#for restaurant in d['restaurants']:
					if((restaurant['restaurant']['average_cost_for_two'] >= 300) and (restaurant['restaurant']['average_cost_for_two'] <= 700) and (count<5)):
							response=response+str(count+1)+" Found "+ restaurant['restaurant']['name']+ " in "+restaurant['restaurant']['location']['address']+" has been rated "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n\n"
							count = count+1
							#dispatcher.utter_message("300=700---------------------------------------")

			elif budget== "More than 700":
				for restaurant in sorted(d['restaurants'], key=lambda x: x['restaurant']['user_rating']['aggregate_rating'], reverse=True):
				#for restaurant in d['restaurants']:
					if((restaurant['restaurant']['average_cost_for_two'] > 700) and (count<5)):
							response=response+str(count+1)+" Found "+ restaurant['restaurant']['name']+ " in "+restaurant['restaurant']['location']['address']+" has been rated "+ str(restaurant['restaurant']['user_rating']['aggregate_rating'])+"\n\n\n"
							count = count+1
							#dispatcher.utter_message(">700---------------------------------------")
 
			if(count==5):
				dispatcher.utter_message("Top 5 Restaurants based on ratings!"+ "\n" +response)
				emailBody = response
		if(count<5 and count>0):
			dispatcher.utter_message("Top 5 Restaurants based on ratings!"+ "\n" +response)
			emailBody = response
		if(count==0):
			response = "Sorry, No results found for your criteria. Would you like to search for some other restaurants?"
			dispatcher.utter_message(response)
		return [SlotSet('location',loc)]

class ActionCheckLocation(Action):

    def name(self):
        return 'action_chklocation'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        
        cities=['Ahmedabad', 'Bangalore', 'Chennai', 'Delhi', 'Hyderabad', 'Kolkata', 'Mumbai', 'Pune',
        'Agra', 'Ajmer', 'Aligarh', 'Amravati', 'Amritsar', 'Asansol', 'Aurangabad', 'Bareilly',
        'Belgaum', 'Bhavnagar', 'Bhiwandi', 'Bhopal', 'Bhubaneswar', 'Bikaner', 'Bilaspur','Bokaro Steel City',
        'Chandigarh', 'Coimbatore', 'Cuttack', 'Dehradun', 'Dhanbad', 'Bhilai', 'Durgapur',
        'Erode', 'Faridabad', 'Firozabad', 'Ghaziabad', 'Gorakhpur', 'Gulbarga', 'Guntur', 'Gurgaon',
        'Guwahati','Hamirpur','Gwalior', 'Hubli-Dharwad', 'Indore', 'Jabalpur', 'Jaipur', 'Jalandhar', 'Jammu', 'Jamnagar','Jamshedpur', 'Jhansi', 'Jodhpur', 'Kakinada','Kannur', 'Kanpur', 'Kochi', 'Kolhapur', 'Kollam',
        'Kozhikode', 'Kurnool', 'Lucknow', 'Ludhiana', 'Madurai', 'Malappuram', 'Mathura', 'Goa', 'Mangalore',
        'Meerut', 'Moradabad', 'Mysore', 'Nagpur', 'Nanded', 'Nashik', 'Nellore', 'Noida', 'Patna',
        'Pondicherry','Purulia', 'Prayagraj', 'Raipur', 'Rajkot', 'Rajahmundry', 'Ranchi', 'Rourkela', 'Salem', 'Sangli',
        'shimla','Siliguri', 'Solapur', 'Srinagar','Surat', 'Thiruvananthapuram', 'Thrissur', 'Tiruchirappalli',
        'Tiruppur', 'Ujjain', 'Bijapur', 'Vadodara', 'Varanasi', 'Vasai-Virar City', 'Vijayawada','Visakhapatnam','Vellore','Warangal']
        
        cities_lower=[x.lower() for x in cities]
        
        if loc.lower() not in cities_lower:
            dispatcher.utter_message("Sorry, we don’t operate in this city. Can you please specify some other location")
        return       

class ActionValidateEmail(Action):
    def name(self):
        return 'action_validate_email'
    def run(self, dispatcher, tracker, domain):
        regex = r'^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        email_check = tracker.get_slot('email')
        #dispatcher.utter_message(email_check)
        if email_check is not None:
            lst = re.findall('\S+@\S+', email_check)
            if len(lst)>0:
                if re.search(regex, lst[0]):
                    #dispatcher.utter_message(email_check)
                    return[SlotSet('email',email_check)]
                else:
                    dispatcher.utter_message("Sorry this is not a valid email. please check for typing errors")
                    return[SlotSet('email',None)]
            else:
                dispatcher.utter_message("Can you please provide the emailId")
                return[SlotSet('email',None)]
        else:
            dispatcher.utter_message("Sorry I could not understand the email address which you provided? Please provide again")
            return[SlotSet('email', None)]
        
class ActionSendEmail(Action):

	def name(self):
		return 'action_send_email'

	def run(self, dispatcher, tracker, domain):
		global emailBody
		from_user = 'group.sachin.prachi@gmail.com'
		to_user = tracker.get_slot('email')
		password = 'UpgradChatbot@123'
		server = smtplib.SMTP('smtp.gmail.com',587)
		server.starttls()
		server.login(from_user, password)
		subject = 'Top 5 Restaurants search results'
		msg = MIMEMultipart()
		msg['From'] = from_user
		msg['TO'] = to_user
		msg['Subject'] = subject
		msg.attach(MIMEText(emailBody,'plain'))
		text = msg.as_string()
		server.sendmail(from_user,to_user,text)
		server.close()
		dispatcher.utter_message("Email has been sent to your email id")