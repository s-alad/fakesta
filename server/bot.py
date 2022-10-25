from instagrapi import Client

cl = Client()
cl.login("", "")
print(cl)

user_id = cl.user_id_from_username("")
followers = cl.user_followers(user_id=user_id, amount=0)
following = cl.user_following(user_id=user_id, amount=0)
flwrs = []
flwng = []
for follower in followers.values():
    flwrs.append(follower.username)
for following in following.values():
    flwng.append(following.username)

print("Followers: ", flwrs)
print("Following: ", flwng)
#print people who you follow but they don't follow you back
print("People you follow but they don't follow you back: ", set(flwng)-set(flwrs))