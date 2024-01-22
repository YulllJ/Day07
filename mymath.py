print(globals())#여기서 main파일이 아니라 mymath이다.
if __name__=="__main__": # import한 모듈안에서 main으로 하면 에러가 발생한다.
    def isprime(n) -> bool:
        """
        매개변수로 넘겨 받은 수가 소수인지 여부를 boolean으로 리턴
        :param n: 판정할 매개변수
        :return: 소수면 True, 소수가 아니면 False
        """
        if n < 2:
            return False
        else:
            i = 2
            while i * i <= n:
                if n % i == 0:
                    return False
                i += 1
            return True


    def fahrenheit_to_celsius(fahrenheit):
        return ((fahrenheit - 32.0) * 5.0 / 9.0)
else:
    print("mymath is not a main file") #이게 출력됨 이파일은 main이 아니라 subfile이라는 의미
