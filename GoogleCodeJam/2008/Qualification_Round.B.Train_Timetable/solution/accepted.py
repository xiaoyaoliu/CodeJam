from os import path
from heapq import heappush, heappop
#!python % < ../A-small-practice.in
# in_file = '../B-small-practice.in'
in_file = '../B-large-practice.in'
# in_file = '../sample.in'
out_file = '.'.join([path.splitext(path.basename(in_file))[0], 'out'])


def solution(fin, fout):
	def tstr2int(tstr):
		thour, tmin = map(int, tstr.split(':'))
		return thour * 60 + tmin

	def cmppair(x, y):
		return cmp(x[0], y[0]) or cmp(x[1], y[1])

	def onestep(tin, cur_wait, other_wait):
		heappush(other_wait, tin[1] + T)
		if cur_wait and cur_wait[0] <= tin[0]:
			heappop(cur_wait)
			return 0
		return 1

	N = int(fin.readline())
	for i in range(N):
		T = int(fin.readline())
		NA, NB = map(int, fin.readline().split())
		Ares, Bres = 0, 0
		Await, Bwait = [], []
		A, B = [], []
		for j in range(NA):
			tpair = map(tstr2int, fin.readline().split())
			A.append(tpair)
		for j in range(NB):
			tpair = map(tstr2int, fin.readline().split())
			B.append(tpair)
		A.sort(cmppair)
		B.sort(cmppair)
		ai = bi = 0
		while ai < len(A) and bi < len(B):
			if A[ai][0] < B[bi][0]:
				Ares += onestep(A[ai], Await, Bwait)
				ai += 1
			else:
				Bres += onestep(B[bi], Bwait, Await)
				bi += 1
		while ai < len(A):
			Ares += onestep(A[ai], Await, Bwait)
			ai += 1
		while bi < len(B):
			Bres += onestep(B[bi], Bwait, Await)
			bi += 1
		fout.write('Case #%s: %s %s\n' % (i + 1, Ares, Bres))


with open(in_file) as fin:
	with open(out_file, 'w') as fout:
		solution(fin, fout)
