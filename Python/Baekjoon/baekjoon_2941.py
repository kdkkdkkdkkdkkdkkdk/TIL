# baekjoon_2941.py
# 크로아티아 알파벳

s = input()
check = ['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in check:
  if i in s:
    s = s.replace(i,'*')

print(len(s))

