import csv
from datetime import datetime
from twilio.rest import Client
import schedule
import time
import openai

openai.api_key = "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"

# Twilio account details
account_sid = 'ACd9aca1f3e4ce0746eee727ca7c0f3cbd'
auth_token = '8fe5e7aea332820de3ebd89a435026bc'
client = Client(account_sid, auth_token)

# Open the CSV file and read its contents
with open('survey_responses.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Extract the time, message, and interests from the CSV file
        msg_time = datetime.strptime(row['Time'], '%Y-%m-%dT%H:%M')
        interests = row['interests']
        
        # Check if interests is "outside" and if so, skip scheduling the message
        if interests == 'outside':
            print(f"Message not scheduled because user is not available at the moment.")
        else:
            # Generate message using OpenAI API
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=f"Generate a one-line reminder message for filling a survey {row['FName']} about the {row['Interest']} event, with emojis and engaging quotes. ",
                max_tokens=50,
                temperature=0.5,
                n=1,
                stop=None,
                timeout=10,
            )
            msg = response.choices[0].text.strip()
            
            # Schedule the SMS message to be sent at the specified time
            schedule.every().day.at(msg_time.strftime('%H:%M')).do(lambda: send_sms(row['FName'], msg, row['returnTime']))
            print(f"Message '{msg}' scheduled for {msg_time.strftime('%Y-%m-%d %H:%M:%S')}")

survey_link = 'https://forms.gle/qeQahBB46jMWz42CA'

# Function to send the SMS message using the Twilio API
def send_sms(name, msg, event_time):
    message = client.messages.create(
        body=f"Hi {name}, {msg} The event is scheduled for {event_time}. 🎉🎉🎉\n" +survey_link,
        from_='+16315199905',
        to='+918072485114'
    )
    
    print(f"Message '{msg}' sent at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Continuously check the scheduled jobs and execute them when the time arrives
while True:
    schedule.run_pending()
    time.sleep(1)
