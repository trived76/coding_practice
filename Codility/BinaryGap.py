# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    bin_num = str(bin(N)[2:])
    if '0' not in bin_num or len(set(bin_num)) <= 1:
        return 0
    else:
        ones_occurance = bin_num.count('1')
        index_found_current = 0
        index_found_next = 0
        diff = 0
        for i in range(ones_occurance):
            index_found_next = bin_num.index('1', index_found_current)
            if abs(index_found_next - index_found_current) > diff:
                diff = abs(index_found_next - index_found_current)
            index_found_current = index_found_next + 1
        return diff
