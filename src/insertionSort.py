'''
Created on 2016��8��2��

@author: Administrator
'''

def insert_sort(lists):
    count = len(lists)
    for i in range(1,count):
        key=lists[i]
        j=i-1
        while j>=0:
            if lists[j]>key:
                lists[j+1]=lists[j]
                lists[j] =key
                j -=1
    return lists






if __name__ == '__main__':
    pass