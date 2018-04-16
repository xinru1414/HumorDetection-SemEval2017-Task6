import sys, os
from itertools import islice

root_path_1 = sys.argv[1]
root_path_2 = sys.argv[2]
#hl = sys.argv[3]

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f


def read_file_from_dir(path):
	lists = []
	for filename in listdir_nohidden(path):
		fullpath = os.path.join(path, filename)
		with open(fullpath) as myfile:
			numberoflines = count = len(open(fullpath).readlines())
			lists += [[i.replace('\n','') for i in islice(myfile, numberoflines)]]
	return lists


def main():
	a_lists = read_file_from_dir(root_path_1)
	b_lists = read_file_from_dir(root_path_2)
	# get top 10 from gold
	a_top10s, b_top10s = [],[]
	for a,b in zip(a_lists, b_lists):
		a_top10s += [a[:10]]
		b_top10s += [b[:10]]
	for a_top10, b_top10, b_list in zip (a_top10s, b_top10s, b_lists):
		print('\nfile '+ str(len(b_list)))
		for a in a_top10:
			print(b_list.index(a)+1)
		a_set, b_set = set(a_top10), set(b_top10)
		l = len(a_set & b_set)
		print("# of GOLD top 10 are actually in PREDICT top 10: " + str(l))
	# for a_top10, b_top10 in zip(a_top10s, b_top10s):
	# 	a_set, b_set = set(a_top10), set(b_top10)
	# 	l = len(a_set & b_set)
	# 	print("# of GOLD top 10 are actually in PREDICT top 10: " + str(l))
		#print(l)

if __name__ == '__main__':
    main()