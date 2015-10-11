#!/usr/bin/python
# coding: utf8
import os
import settings

CONFIG=settings.CONFIG

#Random choice
import random
result = {}
while len(result) != len(CONFIG):
    result = {}
    for firstname in CONFIG:
        possibility = list(CONFIG.keys())
        for person in CONFIG[firstname]['exclude']:
            possibility.remove(person)
        possibility.remove(firstname)
        for person in list(result.values()):
            if person in possibility:
                possibility.remove(person)
        if len(possibility) == 0:
            break;
        result[firstname]=random.choice(possibility)


#Sending mail to each person
summary = ''
for firstname in CONFIG:
    summary = summary + '\n' + settings.OFFER_TO.format(
        person1=firstname,
        person2=result[firstname])
    msg=settings.BODY.format(
            summary=settings.SUMMARY_MAIL,
            present=result[firstname]
        )
    os.system(settings.EMAIL_CMD.format(to=CONFIG[firstname]['mail'],
        subject=settings.SUBJECT, 
        body=msg))

#Send summary mail
os.system(settings.EMAIL_CMD.format(
    to=settings.SUMMARY_MAIL,
    subject=settings.SUBJECT_SUM, 
    body=settings.BODY_SUM.format(summary=summary)))
