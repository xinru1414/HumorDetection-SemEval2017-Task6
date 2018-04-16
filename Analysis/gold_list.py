import csv
import os, sys

root_path = sys.argv[1]

def listdir_nohidden(path):
	for f in os.listdir(path):
		if not f.startswith('.'):
			yield f
def main():
	for filename in listdir_nohidden(root_path):
		fullpath = os.path.join(root_path, filename)
		outfile = fullpath + '.txt'
		with open(fullpath,'r') as tsvin:
			tsvin = csv.reader(tsvin, delimiter='\t')
			sortedlist = sorted(tsvin, key=lambda row: int(row[2]), reverse=True)
			print(sortedlist)
			with open(outfile, 'w') as o:
				for i in range(len(sortedlist)):
					o.write(sortedlist[i][0] + "\n")

if __name__ == '__main__':
    main()