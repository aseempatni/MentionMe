import collections
lines_seen = set() # holds lines already seen
outfile = open("unique_user_id_new.txt", "w")
for line in open("user_id_new.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
y=collections.Counter(lines_seen)
y
