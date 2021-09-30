#KMP algorithm
#Find the matching sequence's first index id
#index starts from 0
#The KMP algorithm here is used to catch the POS tag sequence which matches the predefined pattern and returns the indexs for the pattern
#The indexs are then used to extract the word sequence, which should be the predicted terms.

def KMPSearch(pattern, sequence):
    res=[]
    M = len(pattern)
    N = len(sequence)
    lps = [0]*M
    j = 0 # index for pat[],initialized as 0
    computeLPSArray(pattern, M, lps)

    i = 0 # index for txt[],initialized as 0
    while i < N:
        if pattern[j] == sequence[i]:
            i += 1
            j += 1
        if j == M:
            #print("Found pattern at index " + str(i-j))
            res.append([i-j,M])
            j = lps[j-1]
        elif i < N and pattern[j] != sequence[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return res

def computeLPSArray(pat, M, lps):
    len = 0 # length of the previous longest prefix suffix
    lps[0] # lps[0] is always 0
    i = 1
    while i < M:
        if pat[i]== pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len-1]
            else:
                lps[i] = 0
                i += 1

#a = ['CD', 'NN', 'CD', ':', 'NN', 'NN', 'VBD', 'NNP', 'NN', 'NN', 'VBZ','VBD', 'NNP','NN']
#b = [ 'VBD', 'NNP', 'NN']
#print(KMPSearch(b, a))