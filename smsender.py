import os
import tkinter as tk
from twilio.rest import Client

# Function to send an SMS when the "Send SMS" button is clicked
def send_sms():
    # Get the recipient's number and message from the input fields
    to_number = to_number_entry.get()
    message_body = message_entry.get()

    # Replace with your Twilio number
    from_number = 'insert here'

    try:
        # Send the SMS using the client object
        message = client.messages.create(
            body=message_body,
            from_=from_number,
            to=to_number
        )
        # Print the message SID
        print("SMS SID:", message.sid)
        status_label.config(text="SMS sent successfully!")
    except Exception as e:
        print("Error:", str(e))
        status_label.config(text="Error sending SMS!")

# Function to make a call when the "Make Call" button is clicked
def make_call():
    # Get the recipient's number from the input field
    to_number = to_number_entry.get()

    # Replace with your Twilio number
    from_number = '+12568183407'

    try:
        # Make the call using the client object
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',  # Replace with your TwiML URL
            from_=from_number,
            to=to_number
        )
        # Print the call SID
        print("Call SID:", call.sid)
        status_label.config(text="Call initiated successfully!")
    except Exception as e:
        print("Error:", str(e))
        status_label.config(text="Error initiating call!")

# Create the GUI window
root = tk.Tk()
root.title("Twilio Message and Call Sender")

# Create and place the GUI components
tk.Label(root, text="Recipient's Number:").pack()
to_number_entry = tk.Entry(root)
to_number_entry.pack()

tk.Label(root, text="Message/Call URL:").pack()
message_entry = tk.Entry(root)
message_entry.pack()

send_sms_button = tk.Button(root, text="Send SMS", command=send_sms)
send_sms_button.pack()

make_call_button = tk.Button(root, text="Make Call", command=make_call)
make_call_button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

# Get your Twilio account credentials from environment variables
account_sid = 'insert here'
auth_token = 'insert here'

if account_sid and auth_token:
    # Create a client object with your credentials
    client = Client(account_sid, auth_token)
else:
    status_label.config(text="Twilio credentials not found. Set them as environment variables.")

# Start the GUI event loop
root.mainloop()
