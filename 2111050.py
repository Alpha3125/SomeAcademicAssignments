#Algebraic Expression calculator

#class containing attributes for univariable expressions
class Univariate:
    def __init__(self):
        self.terms = 0
        self.coeff = []
        self.deg = []
        
    def start(self):
        self.terms = int(input('Enter no. of terms: '))
        print('Enter the coefficient and degree of each term: ')
        for i in range (self.terms):
            self.coeff.append(int(input()))
            self.deg.append(int(input('x^')))
            print('--')
        self.arrange()
        self.disp()

    def disp(self):
        print('Polynomial: ', end = '')
        for i in range(self.terms):
            if self.coeff[i] == 0:
                continue
            elif self.coeff[i] < 0:
                print(' - ', end = '')
            elif self.coeff[i] > 0:
                if i != 0:
                    print(' + ', end = '')
            if self.coeff[i]  > 0 and self.coeff[i] != 1:
                print(self.coeff[i], end = '')
            elif self.coeff[i]  < 0 and self.coeff[i] != -1:
                print(-1*self.coeff[i], end = '')
            if self.deg[i] == 0:
                print('', end= '')
                if self.coeff[i] == 1:
                    print(self.coeff[i], end = '')
                if self.coeff[i] == -1:
                    print(-1*self.coeff[i], end = '')
            elif self.deg[i] == 1:
                print('x', end = '')
            else:
                print('x^', self.deg[i], end = '', sep='')
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

    def multiply(self, U):
        multdeg = []
        multcoeff = []
        multterms = self.terms * U.terms
        for i in range(self.terms):
            for j in range(U.terms):
                multcoeff.append(self.coeff[i]*U.coeff[j])
                multdeg.append(self.deg[i]+U.deg[j])
        self.terms=multterms
        self.deg=multdeg
        self.coeff=multcoeff

    def arrange(self):
        i = 0
        while(i < self.terms-1):
            j = i+1
            while(j < self.terms):
                if self.deg[i] ==  self.deg[j]:
                    self.coeff[i] += self.coeff[j]
                    del self.deg[j]
                    del self.coeff[j]
                    self.terms -= 1
                    j -=1
                j += 1
            i += 1
        i = 0
        while(i < self.terms-1):
            j = i+1
            while(j < self.terms):
                if self.deg[i] < self.deg[j]:
                    temp=self.deg[i]
                    self.deg[i] = self.deg[j]
                    self.deg[j] = temp
                    temp = self.coeff[i]
                    self.coeff[i] = self.coeff[j]
                    self.coeff[j] = temp
                j += 1
            i += 1


#class containing attributes for multivariable expressions
class Multivariate:
    def __init__(self):
        self.terms = 0
        self.variables = 0
        self.coeff = []
        self.deg = []
        
    def start(self):
        self.terms = int(input('Enter no. of terms: '))
        self.variables = int(input('Enter no. of variables: '))
        print('Enter the coefficients and powers: ')
        for i in range (self.terms):
            self.coeff.append(int(input()))
            powers=[]
            for j in range (self.variables):
                powers.append(int(input(chr(112+j)+'^')))
            self.deg.append(powers)
            print('--')
        self.arrange()
        self.disp()

    def disp(self):
        polynomial = ' '
        for i in range(self.terms):
            if self.coeff[i] == 0:
                continue
            poly = ''
            for j in range(self.variables):
                if not self.deg[i][j] == 0:
                    poly += '(' + str(chr(112+j)) + '^' + str(self.deg[i][j]) + ')'
            if(i == 0):
                polynomial += str(self.coeff[i]) + f'{poly}'
            else:
                polynomial += ' + ' + str(self.coeff[i]) + f'{poly}'
        polynomial = polynomial.replace('+ -', '- ')
        polynomial = polynomial.replace('^1)', ')')
        polynomial = polynomial.replace(' 1(',' (')
        if polynomial.strip() == '':
            polynomial = '0'
        print('Polynomial:',polynomial)
        print('')

    def add(self, U):
        for i in range(self.terms):
            if self.deg[i] in U.deg:
                self.coeff[i] += U.coeff[U.deg.index(self.deg[i])]
        for i in range(U.terms):
            if U.deg[i] not in self.deg:
                self.terms +=1
                self.deg.append(U.deg[i])
                self.coeff.append(U.coeff[i])

    def multiply(self, U):
        diff = U.variables - self.variables 
        if diff > 0:
            self.variables += diff
            for i in range(self.terms):
                for j in range(diff):
                    self.deg[i].append(0)
        elif diff < 0:
            diff *= -1
            U.variables += diff
            for i in range(self.terms):
                for j in range(diff):
                    U.deg[i].append(0)
        multdeg = []
        multcoeff = []
        multterms = self.terms * U.terms
        for i in range(self.terms):
            for j in range(U.terms):
                multcoeff.append(self.coeff[i]*U.coeff[j])
                D = []
                for k in range(self.variables):
                    D.append(self.deg[i][k] + U.deg[j][k])
                multdeg.append(D)
        self.terms=multterms
        self.deg=multdeg
        self.coeff=multcoeff

    def arrange(self):
        i = 0
        while(i < self.terms-1):
            j = i+1
            while(j < self.terms):
                if self.deg[i] == self.deg[j]:
                    self.coeff[i] += self.coeff[j]
                    del self.deg[j]
                    del self.coeff[j]
                    self.terms -= 1
                    j -= 1
                j += 1
            i += 1
        i = 0
        while(i < self.terms-1):
            j = i+1
            while(j < self.terms):
                if sum(self.deg[i]) < sum(self.deg[j]):
                    temp = self.deg[i]
                    self.deg[i] = self.deg[j]
                    self.deg[j] = temp
                    temp=self.coeff[i]
                    self.coeff[i] = self.coeff[j]
                    self.coeff[j] = temp
                j += 1
            i +=1


#main body
print('\n---- ---- ---- ---- ---- ---- ---- ----\n')
print('\t\tPOLYNOMIAL TYPE\n\t1.Univariate\n\t2.Multivariate')
choice = int(input('Enter the type of polynomial you want to work with(1/2): '))
if choice == 1:
    print('\n\t\tFIRST POLYNOMIAL')
    P1 = Univariate()
    P1.start()
    print('\t\tSECOND POLYNOMIAL')
    P2 = Univariate()
    P2.start()
elif choice == 2:
    print('\n\t\tFIRST POLYNOMIAL')
    P1 = Multivariate()
    P1.start()
    print('\t\tSECOND POLYNOMIAL')
    P2 = Multivariate()
    P2.start() 
else:
    print('Invalid Input!!')
    exit()
print('\n\t1.Addition\n\t2.Multiplication')
choice = int(input('Enter your choice of operation to perform(1/2): '))
if choice == 1:
    P1.add(P2)
    P1.arrange()
    print('\t\tOUTPUT')
    P1.disp()
elif choice == 2:
    P1.multiply(P2)
    P1.arrange()
    print('\n\t\tOUTPUT')
    P1.disp()
else:
    print('Invalid Input!!')
print('\n---- ---- ---- ---- ---- ---- ---- ----\n')
