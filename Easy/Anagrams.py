def find_anagram(s, q):
    max_count = 0
    similar = None

    for string in s:
        curr_count = 0
        for i in range(len(string) - 1):
            for j in range(len(q) - 1):
                if string[i] == q[j] and string[i + 1] == q[j + 1]:
                    curr_count += 1

        if max_count < curr_count:
            max_count = curr_count
            similar = string

    return similar

s = ["hello", "hey!!", "yellow"]
q = "hey"

res = find_anagram(s, q)
print("The answer is:", res)
