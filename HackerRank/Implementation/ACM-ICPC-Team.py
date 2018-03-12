def pairs(n):
    for i in range(n):
        for j in range(i + 1, n):
            yield (i, j)

def common_topics(person0, person1):
    counter = 0
    for p0, p1 in zip(person0, person1):
        if p0 == '1' or p1 == '1':
            counter += 1
    return counter

n, m = map(int, input().strip().split(' '))
topic = []
topic_i = 0
for topic_i in range(n):
    topic_t = str(input().strip())
    topic.append(topic_t)

d = {}

for (p0, p1) in pairs(n):
    ct = common_topics(topic[p0], topic[p1])
    if ct not in d:
        d[ct] = [(p0, p1)]
    else:
        d[ct].append((p0, p1))

max_num_topics = max(d.keys())
team_count = len(d[max_num_topics])

print(max_num_topics)
print(team_count)