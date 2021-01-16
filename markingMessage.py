from simplegmail import Gmail

gmail = Gmail()

messages = gmail.get_unread_inbox()

message_to_read = messages[0]
message_to_read.mark_as_read()

# Oops, I want to mark as unread now
message_to_read.mark_as_unread()

message_to_star = messages[1]
message_to_star.star()

message_to_trash = messages[2]
message_to_trash.trash()
