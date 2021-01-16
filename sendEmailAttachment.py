from simplegmail import Gmail

gmail = Gmail()

params = {
  "to": "ysfbnl2000@gmail.com",
  "sender": "ysfbnl2000@gmail.com",
  "cc": ["yusufbenli2002@gmail.com"],
  "bcc": ["woosal1337@gmail.com"],
  "subject": "My first email",
  "msg_html": "<h1>Attachment Mail!</h1><br />This is an HTML email.",
  "msg_plain": "Hi\nThis is a plain text email.",
  "attachments": ["attachments/chegg.jpg", "attachments/dvrk.jpg"],
  "signature": True  # use my account signature
}
message = gmail.send_message(**params)
