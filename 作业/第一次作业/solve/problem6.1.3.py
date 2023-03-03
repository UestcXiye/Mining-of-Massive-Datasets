# 购物篮T
T = []
# 初始化购物篮T
for i in range(1, 301):
    t = []
    for value in range(i, 301):
        if value % i == 0:
            t.append(value)
    T.append(t)
# 打印购物篮T
print("\n购物篮T: " + str(T))

# 候选1项集C1，key为项集，value为该项集对应的支持度
C1 = {}
# 求C1
for i in range(1, 101):
    count = 0
    for t in T:
        if i in t:
            count += 1
    C1[str(i)] = count
# 打印候选1项集C1
print("\n候选1项集C1: " + str(C1))

# 支持度阈值s
s = 15
# 频繁1项集L1，key为项集，value为该项集对应的支持度
L1 = {}
# 求L1
for key, value in C1.items():
    if value >= s:
        L1[key] = value
# 打印频繁1项集L1
print("\n频繁1项集L1: " + str(L1))

# 候选2项集C2，key为项集，value为该项集对应的支持度
C2 = {}
for i in range(1, 301):
    for j in range(i, 301):
        if i == j:
            continue
        count = 0
        pair = f"[{i}, {j}]"
        for t in T:
            if i in t and j in t:
                count += 1
        C2[pair] = count
# 打印候选2项集C2
print("\n候选2项集C2: " + str(C2))

# 支持度阈值s
s = 15
# 频繁2项集L2，key为项集，value为该项集对应的支持度
L2 = {}
# 求L2
for key, value in C2.items():
    if value >= s:
        L2[key] = value
# 打印频繁2项集L2
print("\n频繁2项集L2: " + str(L2))

# 求所有购物篮中项的数目之和
sum = 0
for t in T:
    for t_value in t:
        sum += 1
print(f"\n所有购物篮中项的数目之和为：{sum}。")

# 求所有购物篮中最大的购物篮，即元素个数最多的购物篮
# t_len存储T中每个购物篮t的元素个数
t_len = []
for t in T:
    t_len.append(len(t))
# print(t_len)
max_t_len = max(t_len)
print(f"\n在最大的购物篮中，元素个数为：{max_t_len}。\n它是：")
for i in range(100):
    if t_len[i] == max_t_len:
        print(f"购物篮t{i}：{T[i]}")
