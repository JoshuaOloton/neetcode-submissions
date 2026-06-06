class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        adj = collections.defaultdict(list)

        def isValid(w1, w2):
            i, diff = 0, 0
            while i < len(w1):
                if w1[i] != w2[i]:
                    diff += 1
                    if diff > 1:
                        return False
                i += 1
            return diff == 1
        
        if beginWord not in wordList:
            for w in wordList:
                if isValid(beginWord, w):
                    adj[beginWord].append(w)

        for i in range(len(wordList) - 1):
            for j in range(i, len(wordList)):
                w1, w2 = wordList[i], wordList[j]
                if isValid(w1, w2):
                    adj[w1].append(w2)
                    adj[w2].append(w1)
        
        visit = set()
        res = 1
        q = collections.deque([beginWord])

        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                visit.add(w)
                for nei in adj[w]:
                    if nei in visit:
                        continue
                    q.append(nei)
            res += 1

        return 0

