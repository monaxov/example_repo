def find_odd_counter(array: list[int]) -> int:
    fd = {}
    for n in array:
        if n in fd:
            fd[n] += 1
        else:
            fd[n] = 1
    for k, v in fd.items():
        if v % 2 == 1:
            return k

find_odd_counter([1,2,2,3,3,3,4,3,3,3,2,2,1])
