numbers=input("Input first second number : ").split()
n1=int(numbers[0])
n2=int(numbers[1])
if n1 > n2:
    n1, n2 = n2, n1
#파이썬은 이렇게 바로 가능 (packing, unpacking의 관계임)
for number in range(n1, n2+1):
    is_prime = True

    if number < 2:
        #print(f'{number} is not prime number')
        pass #아무것도 하지 않는데 지나갈 때 사용하는 코드 continue는 위로 올라가는 것임
    else :
        i = 2
        while i*i < number:#계산량 줄이기 위한것
        #소수일때 if문이 다 돈다는 문제점 발생
            if number % i == 0:
                is_prime = False
                break
            i = i + 1
            #print(i, end=' ')#성능체크

        if is_prime:
            pass
            print(number, end=' ')
