#reverse는 자체적으로 값을 바꿈 인덱싱으로 하면 재할당을 해줘야한다.
subjects=["C++","Java","Python", "Java"]
print(subjects[::-1])
print(subjects)#index쓰면 원본이 변하지는 않아.
subjects.reverse()
print(subjects)
#insert는 집어넣는 것, *는 반복시에도 사용이 가능하다
#append는 통째로 리스트 안에 리스트 형식으로 들어가져버려 더하기 하면 그냥 이어붙인것처럼
#list는 어떤 타입이든 담을수있따. list를 list에 담는 것도 가능하다.

#index slicing
#list slicing에서 집어넣을때, tuple string다 원소별로 리스트에 들어가게 돼
#지우는건 del, remove, pop으로 가능하다
#subjects.remove("Java")
#print(subjects)
#del subjects[-2]
#print(subjects)
#subjects.pop()#안에 아무것도 없으면 뒤를 지움 pop(0)은 앞을 지움 지우고 싶은 인덱스 pop안에 넣음
#pop성능은 뒤를 지우는 .pop()일때가 성능이 좋아 성능에 맞게 지우면됨
#print(subjects)#python에는 배열이 존재하지 않아 그에 따른 오버헤드가 존재함
#.clear해서 리스트 통으로 지울수있어
#배열 인덱스 반환하는 함수는 find, index find는 -1을 던지고 index는 invalid value?를 내뱉음 기억하고 있어야..
#list를 문자열로 바꿀떄 사용하는게 join ','.join(list)
#sort는 원본을 바꿔, sorted는 원본은 그대로 두고 사본을 만들게 되는 것
sorted_subjects= sorted(subjects)
print(subjects)
subjects.sort(reverse=True) #기본값은 false인데 true로 해서 정렬가능해짐
print(subjects) #정렬시 타입 같아야한다. 숫자랑 string이랑 같이 못해 숫자 str으로 바꾸게 되면 가능 한글 숫자 영어 정렬 우선순위 존재함
#숫자 알파벳 한글순으로 우선순위가 있음
