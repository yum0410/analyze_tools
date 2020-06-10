from collections import Counter


def counter_fill_key(list):
    cnt = Counter(list)
    max_iter = max(cnt.keys())
    for i in range(0, max_iter+1):
        if cnt.get(i) is None:
            cnt[i] = 0
    return {k: v for k, v in sorted(cnt.items(), key=lambda x:x[0])}

def set_sort(x: list):
    return set(sorted(x))

if __name__ == "__main__":
    hoge = [1,1,3,4,5,6,9,9,9,10]
    print(counter_fill_key(hoge))
    print(set_sort(hoge))
