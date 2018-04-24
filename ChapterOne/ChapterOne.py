from collections import Counter

users = [
	{"id": 0, "Name": "Hero"},
	{"id": 1, "Name": "Dunn"},
	{"id": 2, "Name": "Sue"},
	{"id": 3, "Name": "Chi"},
	{"id": 4, "Name": "Thor"},
	{"id": 5, "Name": "Clive"},
	{"id": 6, "Name": "Hicks"},
	{"id": 7, "Name": "Devin"},
	{"id": 8, "Name": "Kate"},
	{"id": 9, "Name": "Klein"}]

print(users)

friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), 
			  (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

for user in users:
	user["friends"] = []

for i, j in friendships:
	users[i]["friends"].append(users[j])
	users[j]["friends"].append(users[i])

def number_of_friends(user):
	return len(user["friends"])

total_connections = sum(number_of_friends(user) for user in users)
print("total connections: " + str(total_connections))

num_users = len(users);
avg_connections = total_connections / num_users
print("avg connections: " + str(avg_connections))

num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
print(sorted(num_friends_by_id, key=lambda user : user[1], reverse = True))

def friends_of_friend_ids_bad(user):
	return [foaf["id"] for friend in user["friends"]
		 for foaf in friend["friends"]]

def not_the_same(user, other_user):
	return user["id"] != other_user["id"]

def not_friends(user, other_user):
	return all(not_the_same(friend, other_user) for friend in user["friends"])

def friends_of_friend_ids(user):
	return Counter(foaf["id"] 
				for friend in user["friends"]
				for foaf in friend["friends"]
				if not_the_same(user, foaf)
				and not_friends(user, foaf))

print("Friends of friend Chi:" + str(friends_of_friend_ids(users[3])))