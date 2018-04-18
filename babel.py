from sys import stdin
from heapq import *
words, language, dictionary = None, None, None
INF = float('inf')
ans = None
def solve(lista, miniword, minilen):
	global words, language, dictionary
	visited = [False for i in range(words*2000)]
	source = dictionary[language[0]]
	print('source = ', source)
	dist = [ INF for i in range(words*2000)]; dist[source] = 0
	heap = [ (0,'',source)]
	while len(heap) != 0:
		d,l, u = heappop(heap)
		if not (visited[u]):
			visited[u] = True
			for v, letra, w in lista[u]:
				print('firstU = {},v = {}, letra = {}, w = {}'.format(u,v, letra, w))
				if dist[v] >= d+w and l != letra:
					dist[v] = d+w
					if v == 9:
						print('lang = ', dist[9])
					heappush(heap,(dist[v],letra,v))
					print('u = {}, v = {}, prevletra = {}, letra = {}, dist[v] = {}'.format(u,v,l, letra, dist[v]))
	print('l 1 = ',dictionary[language[1]])
	print(dist[dictionary[language[1]]])
	print(dist)
	return dist[dictionary[language[1]]]


def main():
	global words,language, dictionary
	words = int(stdin.readline().strip())
	while words != 0:
		language = [ str(x) for x in stdin.readline().split()]
		save = [list() for i in range(words)]
		lista = [list() for i in range(words*2000)]
		dictionary = dict()
		i, miniword, minilen = 0,'',INF
		for w in range(words):
			save[w]=  [ str(x) for x in stdin.readline().split()]
			if save[w][0] not in dictionary:
				dictionary[save[w][0]] = i
				i +=1
			if save[w][1] not in dictionary:
				dictionary[save[w][1]] = i
				i +=1
			palabra1 = dictionary[save[w][0]],dictionary[save[w][1]]
			index1, index2 = dictionary[save[w][0]],dictionary[save[w][1]]
			word = save[w][2]
			longitud = len(word)
			print(dictionary)
			if language[0] == save[w][0] or  language[0] == save[w][1] and longitud < minilen:
				minilen,miniword = longitud, word[0]
			lista[index1].append((dictionary[save[w][1]], word[0], longitud))
			lista[index2].append((dictionary[save[w][0]], word[0], longitud))
		#xprint(lista)
		#ans = (solve(lista, miniword, minilen))
		if language[1] not in dictionary or language[0] not in dictionary:
			print('impossivel')
		else:
			ans = (solve(lista, miniword, minilen))
			if ans == INF:
				print('impossivel')
			else:
				print(ans)
		words = int(stdin.readline().strip())


main()