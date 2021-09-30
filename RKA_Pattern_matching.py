# Rabin Karp Algorithm
# We suppose that the POS tags pattern's size will not be so long for a term, e.g., 100?


pos_size = 100
def search(pattern, sequence, q):
    res=[]
    M = len(pattern)
    N = len(sequence)
    i = 0
    j = 0
    p = 0 # hash value for pattern
    t = 0 # hash value for txt
    h = 1
    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h * pos_size) % q
    for i in range(M):
        p = (pos_size * p + ord(pattern[i])) % q
        t = (pos_size * t + ord(sequence[i])) % q
    for i in range(N-M+1):
        if p==t:
            # Check for characters one by one
            for j in range(M):
                if sequence[i + j] != pattern[j]:
                    break
                else: j+=1
            # if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
            if j==M:
                res.append([i,M])
                print ("Pattern found at index " + str(i))
                #indexs=[]
                #for t in range(M):
                #    indexs.append(i+t)
                #res.append(indexs)
                #continue
        if i < N-M:
            t = (pos_size * (t - ord(sequence[i]) * h) + ord(sequence[i + M])) % q
            if t < 0:
                t = t+q
    return res
#txt = "aa bb aa cc abcda ba bc ba"
#pat = "ba"
#prime_size = 10
#print(search(pat, txt, prime_size))

