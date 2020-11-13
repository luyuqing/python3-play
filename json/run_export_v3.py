import json
import datetime as dt

import requests

"""
Pavel's list:
Conversation ID – unique ID for the conversation. It’d be passed on onClose event to our container, and be used by Qualtrics to fetch chat metadata and update customer response
Start Date – start datetime of the conversation. I guess this would the timestamp of when the visitor has first clicked on the chat icon
End Date – end datetime of the conversation. This would probably be the timestamp of when the visitor clicked on the close button
Duration – duration of the conversation, in seconds
Wait Time – only relevant for escalated chats. How long did the visitor wait for agent?
Escalated? – a Boolean flag which shows whether the conversation has at any time been escalated to a human (true), or if it was performed entirely by chatbot (false)
Company – which of our brands is the visitor currently being served by? Tryg, Enter, TJM, Alka, etc
Queue – eGain queue name, or boost's internal queue/category which shows who the customer spoke with - sales, claims, etc. If there are subcategories (especially claims – travel, behandling, etc), then I'll need them as well
Customer Data – Name, Email, Customer Number, etc - whatever is available
Customer Type – Private or Commercial
Language – detected language name
customer_support_representative_id
customer_support_email
Agent First Name
Agent Last Name
source_url – which URL the chat was activated on
device
"""


raw_data = requests.post(
    url='<Tryg export v3 url>',
    headers={'Authorization': 'Bearer <token>'},
    json={"from": "2020-11-10T10:10:00", "to": "2020-11-10T16:00:00"}
).json()

results = [{'conversation_id': conversation['id'], 'metadata': {}} for conversation in raw_data if conversation['type'] == 'conversation']

for i, v in enumerate(results):
    data = raw_data[i+1]
    assert data['id'] == v['conversation_id']
    metadata_dict = {}

    # Start Date
    start = metadata_dict['start_datetime'] = data['messages'][0]['time']

    # End Date
    # PLEASE NOTE: end_datetime is the "last_message" by the time export api V3 is called, may not neccessarily the "end_datetime"
    # Not every user closes the chat panel, some might just close the webpage, in that way, boost does not receive any info on this user behavior
    end = metadata_dict['end_datetime'] = data['messages'][-1]['time']

    # Duration
    metadata_dict['duration'] = str(dt.datetime.fromisoformat(end) - dt.datetime.fromisoformat(start))

    # Company
    # PLEASE NOTE: this is actually "filter_values", if client sends filter values to disguish company, this can be helpful
    metadata_dict['filter_values'] = data['messages'][0]['sent_filter_values']

    # Queue, Escalated, Wait Time
    # PLEASE NOTE: boost only logs the "skill" when escalting to humanchat, but not aware of anything realted with queue/skill change on humanchat
    skill = None
    escalated = None
    hc_start = None
    for message in data['messages']:
        if message['is_human_chat'] is True and escalated is None:
            escalated = message['time']
        elif message['is_human_chat'] is True and skill is None and message.get("skill"):
            skill = message["skill"]
            continue
        if message.get('is_human_agent') is True and hc_start is None:
            hc_start = message['time']
            continue
    metadata_dict['skill'] = skill
    metadata_dict['escalated'] = bool(escalated)
    if escalated is None:
        metadata_dict['wait_time'] = None
    else:
        metadata_dict['wait_time'] = str(dt.datetime.fromisoformat(hc_start) - dt.datetime.fromisoformat(escalated)) if hc_start else 'User left before human chat begins'

    # Customer Data, Customer type
    # Please NOTE: This is not available in export V3 now, boost is going to add id_subclaim (unique id for each user) to export V3 probably on V11.04
    metadata_dict['user_id'] = 'Will be availabe probably on V11.04'

    # Agent First Name, Agent Last name
    # We only log human chat agent info if using boost human chat, but not for egain or other 3rd party hc operator
    # as each hc operator handles data differently and we don't get relative human chat agent info

    # Language, Source url, device
    metadata_dict['language'] = set()
    metadata_dict['source_url'] = None
    metadata_dict['device'] = None
    for message in data['messages']:
        if message.get('question') and 'predicted_language' in message['question']:
            metadata_dict['language'].add(message['question']['predicted_language'])
        if message.get('actions'):
            if message['actions'].get('displayed'):
                metadata_dict['language'].add(message['actions']['displayed'].get('language'))
            elif message['actions'].get('came_from'):
                metadata_dict['language'].add(message['actions']['came_from'].get('language'))
        if message.get('source_url') and metadata_dict['source_url'] is None:
            metadata_dict['source_url'] = message['source_url']
        if message.get('device') and metadata_dict['device'] is None:
            metadata_dict['device'] = message['device']
    metadata_dict['language'] = list(metadata_dict['language'])

    v['metadata'] = metadata_dict


with open('boost_metadata.json', 'w') as f:
    f.write(json.dumps(results, indent=2))