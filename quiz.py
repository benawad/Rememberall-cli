import sys
import requests
import json

command = sys.argv[1]

def fetch_quizlet(deck_id):
    client_id = "anpmmF7bXs"
    payload = {'client_id': client_id, 'whitespace': 1}
    r = requests.get("https://api.quizlet.com/2.0/sets/{}".format(deck_id),
            params=payload)

    if r.status_code != 200:
        return None

    data = json.loads(r.text)
    title = data['title']
    cards = data['terms']
    return {
        'id': deck_id,
        'title': title,
        'cards': cards,
    }


if command == "quiz":
    qid = sys.argv[2]
    data = fetch_quizlet(qid)
    for c in data['cards']:
        print("Front: " + c['term'])
        input(">")
        print("Answer: " + c['definition'])
        print()

    print("Nice review session!")
elif command == "list":
    pass
elif command == "help":
    pass
elif command == "stop":
    pass
else:
    pass
