import praw
from pprint import pprint

reddit = praw.Reddit(
    client_id="Eu4m12VDmL138g",
    client_secret="iNInsUYMLSdMXdqafuoNP4OHbxXEYg",
    password="algarrobo18",
    user_agent="bot by u/algarrobo18",
    username="algarrobo18",
)

subreddit = reddit.subreddit("nba")

pprint("The subreddit being scrapped is: " + subreddit.display_name)
# print(subreddit.title)
# print(subreddit.description)
print("\n")
print("""Mostrando los últimos 10 resultados en "new":""")
print("\n")

for submission in subreddit.new(limit=10):
    print(submission.title)
    print(submission.url)

print("\n")
print("-------------------------------------------------------------------------------------------")
print("\n")
print("""Mostrando los últimos 10 resultados en "hot":""")
print("\n")

for submission in subreddit.hot(limit=10):
    print(submission.title)
    print(submission.url)

print("\n")
print("-------------------------------------------------------------------------------------------")
print("\n")
print("""Mostrando los últimos 10 resultados en "rising":""")
print("\n")

for submission in subreddit.rising(limit=10):
    print(submission.title)
    print(submission.url)


