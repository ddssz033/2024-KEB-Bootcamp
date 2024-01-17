sugang = dict(python="kim", cpp="sung", db="kang")
# print(sugang)
# sugang['datastructure'] = 'kim' #추가
# print(sugang)
# sugang['datastructure'] = 'park' #update
# print(sugang)
# print(sugang['db'])
# print(sugang.get('db'))
# print(sugang.get('opensource'))
# print(sugang.get('opensource', 'not exist')) #none 대신 not exist 뜨게 만들기
for subject, professor in sugang.items(): #subject = key, professor = values
    print(f'{subject} 과목 담당교수는 {professor}입니다')

for k in sugang.keys():
    print(k)

for v in sugang.values():
    print(v)

for s in sugang.items(): #tuple 형태로 출력
    print(s)