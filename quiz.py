import sys
import requests
import json

command = sys.argv[1]

def search_quizlet(q):
    client_id = "anpmmF7bXs"
    payload = {'client_id': client_id, 'whitespace': 1}
    r = requests.get("https://api.quizlet.com/2.0/search/sets?q=%s" % q, params=payload)

    data = json.loads(r.text)
    # list_thumbnails(recipient_id, list(map(set_to_element, data['sets'][:5])))
    print("Select a number to quiz:")
    for i, s in enumerate(data['sets'][:5]):
        print("%s %s by %s" % (i, s['title'], s['created_by']))

    n = int(input())
    sys.argv[2] = data['sets'][n]['id']


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


if command == "search":
    search_quizlet(sys.argv[2])
    command = "quiz"

if command == "quiz":
    qid = sys.argv[2]
    data = fetch_quizlet(qid)
    for c in data['cards']:
        print("Front: " + c['term'])
        ans = input(">")
        if c['definition'].lower() == ans.lower():
            print("Correct: " + c['definition'])
        else:
            print("Incorrect: " + c['definition'])
        print()

    print("Nice review session!")

elif command == "list":
    pass
elif command == "help":
    print("""Usage: remembrall [subcommand]

Subcommands:
    search         Searches for a set to be quizzed on.
    quiz           Starts a quiz on a specific set.
    """)

elif command == "stop":
    pass
else:
    pass
