#merging same powers
#removing power zeros
#mult.
#adding/removing comments

class Univariate:
    def __init__(self):
        self.terms = 0
        self.coeff = []
        self.deg = []
        
    def start(self):
        self.terms = int(input('Enter no. of terms: '))
        print('Enter the coefficients: ')
        for i in range (self.terms):
            self.coeff.append(int(input()))
        print('Enter the degrees: ')
        for i in range (self.terms):
            self.deg.append(int(input('x^')))
        self.disp()

    def disp(self):
        polynomial = ''
        for i in range(self.terms-1):
            polynomial += str(self.coeff[i]) + 'x^' + str(self.deg[i]) + ' + '
        polynomial += str(self.coeff[-1]) + 'x^' + str(self.deg[-1])
        print('Polynomial: ',polynomial)
        #print(self.terms, self.coeff, self.deg)
        print()
        
    def add(self, U):
        for i in range(self.terms):
            if self.deg[i] in U.deg:
                self.coeff[i] += U.coeff[U.deg.index(self.deg[i])]
        for i in range(U.terms):
            if U.deg[i] not in self.deg:
                self.terms +=1
                self.deg.append(U.deg[i])
                self.coeff.append(U.coeff[i])
        self.disp()

    def multiply(self, U):
        multdeg=[]
	    multcoeff=[]
	    multterms=self.terms*U.terms
        for i in range(self.terms):
            for j in range(U.terms):
                multcoeff.append(self.coeff[i]*U.coeff[j])
                multdeg.append(self.deg[i]+U.deg[j])
        self.terms=multterms
        self.deg=multdeg
        self.coeff=multcoeff
        self.disp()
        
class Polyvariate:
    def __init__(self):
        self.terms = 0
        self.variables = 0
        self.coeff = []
        self.deg = []
        
    def start(self):
        self.terms = int(input('Enter no. of terms: '))
        self.variables = int(input('Enter no. of variables: '))
        print('Enter the coefficients: ')
        for i in range (self.terms):
            self.coeff.append(int(input()))
        print('Enter the degrees: ',self.terms)
        for i in range (self.terms):
            powers=[]
            for j in range (self.variables):
                powers.append(int(input(chr(112+j)+'^')))
            self.deg.append(powers)
            print('--')
        self.disp()

    def disp(self):
        polynomial = ''
        for i in range(self.terms):
            poly = ''
            for j in range(self.variables):
                poly += '(' + str(chr(112+j)) + '^' + str(self.deg[i][j]) + ')'
            if(i == self.terms-1):
                polynomial += str(self.coeff[i]) + f'{poly}'
            else:
                polynomial += str(self.coeff[i]) + f'{poly}' + ' + '
        print('Polynomial: ',polynomial)
        #print(self.terms, self.coeff, self.deg)
        print()

    def add(self, U):
        for i in range(self.terms):
            if self.deg[i] in U.deg:
                self.coeff[i] += U.coeff[U.deg.index(self.deg[i])]
        for i in range(U.terms):
            if U.deg[i] not in self.deg:
                self.terms +=1
                self.deg.append(U.deg[i])
                self.coeff.append(U.coeff[i])
        self.disp()

    def multiply(self, U):
        pass


print('\n\t1.Univariate\n\t2.Multivariate')
choice = int(input('Enter the type of polynomial you want to work with(1/2): '))
if choice == 1:
    print('\n\t\tFIRST POLYNOMIAL')
    P1 = Univariate()
    P1.start()
    print('\t\tSECOND POLYNOMIAL')
    P2 = Univariate()
    P2.start()
    P2.disp() 
elif choice == 2:
    print('\n\t\tFIRST POLYNOMIAL')
    P1 = Polyvariate()
    P1.start()
    print('\t\tSECOND POLYNOMIAL')
    P2 = Polyvariate()
    P2.start()
    P2.disp()    
else:
    print('Invalid Input!!')
    exit()

print('\n\t1.Addition\n\t2.Multiplication')
choice = int(input('Enter your choice of operation to perform(1/2): '))
if choice == 1:
    P1.add(P2)
elif choice == 2:
    P1.multiply(P2)
else:
    print('Invalid Input!!')
