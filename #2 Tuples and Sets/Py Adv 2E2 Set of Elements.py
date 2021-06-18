# Py Adv 2E2 Set of Elements

# input 4 3
# 1
# 3
# 5
# 7
# 3
# 4
# 5
# output 3
# 5

m, n = input().split()
m_set = set()
n_set = set()
for num in range(int(m)):
    m_num = int(input())
    m_set.add(m_num)
# {1, 3, 5, 7}
for num in range(int(n)):
    n_num = int(input())
    n_set.add(n_num)
# {3, 4, 5}
result = m_set.intersection(n_set)
for el in result:
    print(el)
