def fibr(n):
    if n==0 or n==1:
        return 1
    else:
        return fibr(n - 1) + fibr(n - 2)
for i in range(100):
            print(fibr(i))