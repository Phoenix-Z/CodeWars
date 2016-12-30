#  -*- coding: utf-8 -*- 
# (220ms)
# 使用的是编辑距离算法(Levenshtein距离)
class Dictionary:
    def __init__(self,words):
        self.words=words
    def find_most_similar(self,term):
		distance = []
		max_similarity = 0.0
		ans = None
		for word in words:
			for i in range(len(term) + 1):
				distance.append(range(i,len(word) + i + 1))
			for i in range(1, len(term) + 1):
				for j in range(1, len(word) + 1):
					min_val = min(distance[i - 1][j - 1], distance[i - 1][j], distance[i][j - 1])
					if term[i - 1] == word[j - 1]:
						distance[i][j] = min_val
					else:
						distance[i][j] = min_val + 1
			maxLen = max(len(term), len(word))
			similarity = (maxLen - distance[i][j]) * 1.0 / maxLen
			if max_similarity < similarity:
				max_similarity = similarity
				ans = word
			distance = []
		return ans
		
words=['cherry', 'peach', 'pineapple', 'melon', 'strawberry', 'raspberry', 'apple', 'coconut', 'banana']
test_dict=Dictionary(words)
print test_dict.find_most_similar('berry')
