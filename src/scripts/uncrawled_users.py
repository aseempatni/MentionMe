import json
f = open('user_ids.json','r')
all_users = json.load(f)
all_users = set(all_users)
f = open('done_users.txt','r')
done_users = json.load(f)
done_users = set(done_users)
remaining_users = all_users - done_users
remaining_users = list(remaining_users)
print remaining_users
