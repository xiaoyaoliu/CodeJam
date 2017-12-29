from os import path
#!python % < ../A-small-practice.in
# in_file = '../A-small-practice.in'
in_file = '../A-large-practice.in'
out_file = '.'.join([path.splitext(path.basename(in_file))[0], 'out'])


def solution(fin, fout):
	N = int(fin.readline())
	for i in range(N):
		S = int(fin.readline())
		full_flag = 0L
		mdict = {}
		for si in range(S):
			sname = fin.readline()
			mid = 1 << si
			mdict[sname] = mid
			full_flag |= mid

		Q = int(fin.readline())
		mflag = 0L
		result = 0
		for j in range(Q):
			sname = fin.readline()
			mflag |= mdict[sname]
			if mflag == full_flag:
				result += 1
				mflag = mdict[sname]
		fout.write('Case #%s: %s\n' % (i + 1, result))


with open(in_file) as fin:
	with open(out_file, 'w') as fout:
		solution(fin, fout)
