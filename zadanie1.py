#Funkcja tworzy palindrom z zadanej liczby
def revNumber(num):
    return int(str(num)[::-1])

#Funkcja sprawdza czy liczba to palindom. Jeżeli jest zwraca True
def isPalindrome(num):
    return num==revNumber(num)

#Funkcja oblicza palindrom dla zadanej liczby startowej oraz maksymalnej liczbie iteracji  
def findPalindrome(number,max_iter):
    for num in range(0,number+1):
        #Inicjalizacja licznika iteracji
        count=0
        #Inicjalizacja palindromu
        rev_num=0
        #Inicjalizacja sumy
        sum=num
        rev_num = revNumber(num)
        #Szukaj sumy, sprawdź czy jest palidromem dopóki count<max_iter. Jeżeli isPalindrome(sum)-->true
        # wypisz: liczbe startowa, liczbe iteracji, palindrom
        #jezeli przekroczysz liczbe iteracji
        #wypisz: liczbe startowa, ostatnią policzoną sumę
        while (count<max_iter) :
            count+=1
            rev_num = revNumber(sum)
            sum=sum+rev_num
            if(isPalindrome(sum)):
                print("Starting point: %i, Iteration number: %i, Palindrome: %i" % (num,count, sum))
                break
            elif(count>=max_iter):
                print("FAILED. Starting point %i, Last iterated sum: %i"% (num,sum))
    return