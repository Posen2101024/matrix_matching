
import numpy as np
import queue

class MatrixMatching():

	def __new__(cls, target, matrix):

		trie, array = cls.buildTrie(matrix)

		fail = cls.getFailFunction(array)

		return cls.getMatching(target, matrix, trie, array, fail)

	def buildTrie(matrix):

		trie, array = {"fail": None}, []

		for label, row in enumerate(matrix, 1):

			node = trie

			for num in row:

				node[num] = node = node.get(num, {})

			if not "label" in node: 

				node["label"] = label

			array.append(node["label"])

		root_queue = queue.Queue()

		root_queue.put(trie)

		while not root_queue.empty():

			root = root_queue.get()

			for num in [k for k in root if not isinstance(k, str)]:

				root_queue.put(root[num])

				node = root["fail"]

				while node and not num in node:
					node = node["fail"]

				root[num]["fail"] = node[num] if node else trie

		return trie, array

	def getFailFunction(array):

		fail = [-1]

		k = -1

		for num in array[1:]:

			while k >= 0 and array[k + 1] != num:
				k = fail[k]

			if array[k + 1] == num:
				k += 1

			fail.append(k)

		return fail

	def getMatching(target, matrix, trie, array, fail):

		table = np.zeros(target.shape, dtype = int)

		for i, row in enumerate(target):

			node = trie

			for j, num in enumerate(row):

				while node and not num in node:
					node = node["fail"]

				node = node[num] if node else trie

				table[i, j] = node.get("label", 0)

		for i, row in enumerate(table.T):

			k = -1

			for j, num in enumerate(row):

				while k >= 0 and array[k + 1] != num:
					k = fail[k]

				if array[k + 1] == num:
					k += 1

				if k == len(array) - 1:
					dx, dy = j - k, j + 1
					ex, ey = i - matrix.shape[1] + 1, i + 1
					return [dx, dy, ex, ey]
