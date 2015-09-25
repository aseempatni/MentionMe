import sys

def getCoeffs() :
	inFile = open(sys.argv[1], 'r')
        data = inFile.read()
        dict = eval(data)
        dicts = {}
        user_ids = []
        for key in dict :
                dicts[int(key)] = dict[key]['coeff']
                user_ids.append(int(key))
        print len(dicts)

def main() :
	getCoeffs()

if __name__ == "__main__" :
	main()
