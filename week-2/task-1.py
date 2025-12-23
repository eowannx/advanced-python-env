s = input()
count = 0

for i in range(len(s) - 4):
    if (
       (s[i] == '>' and s[i+1] == '>' and s[i+2] == '-' and s[i+3] == '-' and s[i+4] == '>') or
       (s[i] == '<' and s[i+1] == '-' and s[i+2] == '-' and s[i+3] == '<' and s[i+4] == '<')
    ):
        count += 1

print(count)