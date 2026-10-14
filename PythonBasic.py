#这个文件可以放python基础.md里的示例代码
def get_min_max(lst):
    return min(lst), max(lst)

low, high = get_min_max([3, 1, 4, 1, 5])
print(low, high)   # 1 5