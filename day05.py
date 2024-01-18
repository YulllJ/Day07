# set은 딕셔너리에서 키만 있는 것과 같다. 따라서 키는 유니크해야돼
# set은 값 꺼낼때(dict) 말고 존재여부 판정할때 사용하면 좋다, set= key container value까지 있는거 다루렴녀 dict로
# set은 기호로만 만들수 없어 empty set만드려면 set()으로만 가능
# set은 중복 제거, key만 존재함 set은 순서가 존재하지 않는다 섞여서 나와도 상관없어
# item은 키벨류 튜플 형태로 반환
# for name, contencts in drinks.items(): 에서 unpacking해서 값을 각각 받음
# 교집합에 & 쓴다. a.intersection(b)나 a & b로 쓴다.
# 합집합 | union
# 부분집합 subset은 <=  a.issubset(b); return type:boolean
# tuple은 없지만 set도 comprehension존재함(조건이 너무 많아서 길어져서 가독성 떨어지면 그냥 나눠서 쓰는게 낫다)
# 안변하는 set을 frozenset add로 추가불가(그냥 set은 가능했음):immutable
# is&*&$라고 이름 떠진 것은 boolean type이라는게 명확히 잘보인다.
# 객체지향설계 원칙 SOLID
# 그중 S..책임 = 기능 <단일 책임 원칙> 하나의 클래스, 하나의 함수는 맡은 바 하나만 잘하면 된다. 각각의 기능에 충실하게




