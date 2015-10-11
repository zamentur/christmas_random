# coding: utf8
# The exclude parameter allow to avoid a person have to offer to certain persons (like couples, or last year results )
CONFIG={
    'Sam':{'mail':'sam@exemple.com','exclude':['Max','Luc']},
    'Max':{'mail':'max@exemple.com','exclude':['Sam','Tom']},
    'Rod':{'mail':'rod@exemple.com','exclude':['Luc','Ted']},
    'Luc':{'mail':'luc@exemple.com','exclude':['Rod','Sam']},
    'Tom':{'mail':'tom@exemple.com','exclude':['Ted','Max']},
    'Ted':{'mail':'ted@exemple.com','exclude':['Tom','Luc']},
}
SUBJECT='Present'
BODY='This is an automatic email. {summary} has received a global summary. This year you will offer a present to...\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n{present}'

SUMMARY_MAIL='bill@exemple.com'
SUBJECT_SUM='Present : global summary'
BODY_SUM='This is an automatic email. Global summary : \n {summary}'
OFFER_TO='{person1} offers to {person2}'

EMAIL_CMD='thunderbird -compose "to=\'{to}\',subject=\'{subject}\',body=\'{body}\'"'
