from collections import Counter
from collections import defaultdict

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

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]

users_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    users_ids_by_interest[interest].append(user_id)

interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

def most_common_interests_with(user):
    return Counter(interested_user_id
                   for interest in interests_by_user_id[user["id"]]
                   for interested_user_id in users_ids_by_interest[interest]
                   if interested_user_id != user["id"])

print("Most common interests with Chi: " + str(most_common_interests_with(users[3])))

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

salary_by_tenure = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries)
    for tenure, salaries in salary_by_tenure.items()
    }

def tenure_bucket(tenure):
    if tenure < 2:
        return "менее двух"
    elif tenure < 5:
        return "между двумя и пятью"
    else:
        return "более пяти"

salary_by_tenure_bucket = defaultdict(list)

for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

average_salary_by_bucket = {
     tenure_bucket: sum(salaries) / len(salaries)
     for tenure_bucket, salaries in salary_by_tenure_bucket.items()
     }

print("Avarage salary by bucket: " + str(average_salary_by_bucket))