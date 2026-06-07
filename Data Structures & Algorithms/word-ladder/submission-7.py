class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)
        if endWord not in words or beginWord == endWord:
            return 0

        res = 1
        visit = set()
        q = deque([beginWord])
        while q:
            for _ in range(len(q)):
                w = q.popleft()
                if w == endWord:
                    return res
                visit.add(w)
                for i in range(len(w)):
                    for c in range(97, 123):
                        if chr(c) == w[i]:
                            continue
                        search = w[ : i] + chr(c) + w[i + 1 : ]
                        if search in words and search not in visit:
                            q.append(search)
            res += 1
    
        return 0
