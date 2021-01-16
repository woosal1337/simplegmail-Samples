import base64
from email import errors


def get_attachments(service, msg_id):
    try:
        message = service.users().messages().get(userId='me', id=msg_id).execute()

        for part in message['payload']['parts']:
            if part['filename']:
                if 'data' in part['body']:
                    data = part['body']['data']
                else:
                    att_id = part['body']['attachmentId']
                    att = service.users().messages().attachments().get(userId='me', messageId=msg_id,
                                                                       id=att_id).execute()
                    data = att['data']
                file_data = base64.urlsafe_b64decode(data.encode('UTF-8'))
                path = part['filename']

                with open(path, 'wb') as f:
                    f.write(file_data)


    except errors.HttpError as error:
        print('An error occurred: %s') % error


def get_message(service, msg_id):
    try:
        message = service.users().messages().get(userId='me', id=msg_id).execute()
        if message['payload']['mimeType'] == 'multipart/mixed':
            for part in message['payload']['parts']:
                for sub_part in part['parts']:
                    if sub_part['mimeType'] == 'text/plain':
                        data = sub_part['body']['data']
                        break
                if data:
                    break
        else:
            for part in message['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                    break

        content = base64.b64decode(data).decode('utf-8')
        print(content)

        return content

    except errors.HttpError as error:
        print("An error occured : %s") % error

