print('helow word!')


def mysort(a, low, high):
     if low < high:
         i = low
         j = high
         tmp = a[low]
         while i<j and a[j] >= tmp:
             j -= 1
         if i<j:
             a[i] = a[j]
             i += 1
         while i<j and a[i] < tmp:
             i += 1
         if i<j:
             a[j] = a[i]
             j -= 1
         a[i] = tmp
         mysort(a, low, i -1)
         mysort(a, i + 1, high)


if __name__ == '__main__':
    a =[1, 2, -1, 8 , 99, 90]
    mysort(a, 0, 5)
    for i in range(len(a)):
        print(a[i])