from simplegmail import Gmail

gmail = Gmail() # will open a browser window to ask you to log in and authenticate

params = {
  "to": "ysfbnl2000@gmail.com",
  "sender": "ysfbnl2000@gmail.com",
  "subject": "My first email",
  "msg_html": "<h1>Woah, my first email!</h1><br />This is an HTML email.",
  "msg_plain": "Hi\nThis is a plain text email.",
  "signature": True  # use my account signature
}
message = gmail.send_message(**params)  # equivalent to send_message(to="you@youremail.com", sender=...)
