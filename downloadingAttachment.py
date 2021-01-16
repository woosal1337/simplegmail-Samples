from simplegmail import Gmail

gmail = Gmail()

messages = gmail.get_unread_inbox()

message = messages[0]
if message.attachments:
    for attm in message.attachments:
        print('File: ' + attm.filename)
        attm.save()
