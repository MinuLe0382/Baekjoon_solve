def knapsack(capacity, item):
    if capacity == 0 or item >= _number:
        return 0

    if _memo[capacity][item] != -1:
        return _memo[capacity][item]

    if _weight[item] > capacity:
        _memo[capacity][item] = knapsack(capacity, item + 1)
    else:
        with_the_item = _value[item] + knapsack(capacity - _weight[item], item + 1)
        without_the_item = knapsack(capacity, item + 1)
        _memo[capacity][item] = max(with_the_item, without_the_item)

    return _memo[capacity][item]

_number, _capacity = map(int, input().split())
_weight = []
_value = []

for _ in range(_number):
    w, v = map(int, input().split())
    _weight.append(w)
    _value.append(v)

_memo = [[-1] * (_number + 1) for _ in range(_capacity + 1)]

print(knapsack(_capacity, 0))