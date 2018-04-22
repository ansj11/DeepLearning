

n = int(raw_input())
a = raw_input().split(' ')
a.sort()
ans = 0
num = 0
for x in a:
    num %= 3
    if num != 0 and x > last + 10:
        ans += 3 - num
        num = 0
    num += 1
    last = x
print num,ans
ans += 3 - num
print ans