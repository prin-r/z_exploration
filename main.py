from itertools import chain, combinations


def powerset(iterable):
  s = list(iterable)
  return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def cal_directly(n,s):
  return len(set([v if sum(list(v)) % s == 0 else None for v in powerset(range(1,n+1))]) - {None})


def create_table(n, m):
  print(1, sorted([i%m for i in range(1, n+1)]))
  for i in range(2,m):
    print(i, sorted([(j*i)%m for j in range(1, n+1)]))
