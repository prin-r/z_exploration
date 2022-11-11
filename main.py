from itertools import chain, combinations


def powerset(iterable):
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def cal_directly(n,s):
  return len(set([v if sum(list(v)) % s == 0 else None for v in powerset(range(1,n+1))]) - {None})


def create_table(n, m):
  # print(1, sorted([i%m for i in range(1, n+1)]))
  tmp = [[i % m for i in range(1, n + 1)]]
  for i in range(2,m):
    # print(i, sorted([(j*i)%m for j in range(1, n+1)]))
    tmp.append([(j * i) % m for j in range(1, n + 1)])

  if m % 2 == 0:
    for t in tmp:
      if m >> 1 not in t:
        print(t)
  else:
    for t in tmp:
      print(t)

  print("-"*n*3)


create_table(19, 15)
print(cal_directly(19, 15))
