#!/usr/bin/python3

#https://practice.geeksforgeeks.org/problems/first-non-repeating-character-in-a-stream/0

import queue

def sol(arr, n):
    """
    Let there be a hash counting the occurence of characters. Push the 
    character in the Queue as it appears for the first time. 
    Now, pop the element from the queue only if it differs from the result
    else keep using the same result.

    We are keeping a track of 'res' because we are using q.get() which
    pops the element. We can also check the first element and we need not
    keep track of last result
    """
    ht = {}
    q = queue.Queue(maxsize=n)
    cnt = {}
    
    res = arr[0]
    for char in arr:
        if res == char or res == -1:
            res = False
        
        if char in cnt:
            cnt[char]+=1
        else:
            cnt[char] = 1
            q.put(char)
        
        if not res:
            found = False
            while not q.empty():
                res = q.get()
                if cnt[res] == 1:
                    found = True
                    break
            if not found:
                res = -1
        print(res, end=" ")
    print()

arr="w l r b b m q b h c d a r z o w k k y h i d d q s c d x r\
j m o w f r x s j y b l d b e f s a r c b y n e c d y g g x x p\
k l o r e l l n m p a p q f w k h o p k m c o q h n w n k u e w h\
s q m g b b u q c l j j i v s w m d k q t b x i x m v t r r b l\
j p t n s n f w z q f j m a f a d r r w s o f s b c n u v q h f\
f b s a q x w p q c a c e h c h z v f r k m l n o z j k p q p x\
r j x k i t z y x a c b h h k i c q c o e n d t o m f g d w d w\
f c g p x i q v k u y t d l c g d e w h t a c i o h o r d t q k v w c s g s p q o q m s b o a g u w n n y q x n z l g d g w"

sol(arr, len(arr))