from datetime import date
todays_date = date.today()

print(f'''작성하고 싶은 파일명을 입력하세요.
(예: examples.sql -> examples 입력)
아무것도 입력하지 않으시면 {todays_date}.sql 파일이 생성됩니다.
공백문자는 언더스코어로 대체됩니다.''')
file_name = input('> ').strip()

s = set('\\/*:?"<>|')

def is_valid(file_name: str) -> bool:
    for i in file_name:
        if i in s:
            return False
    
    return True

while not is_valid(file_name=file_name):
    file_name = input('사용할 수 없는 문자를 입력하셨습니다. 다시 입력하세요: ').strip()    
    while len(file_name) > 255:
        file_name = input('255자 이내로 입력해주세요: ').strip()

while len(file_name) > 255:
    file_name = input('255자 이내로 입력해주세요: ').strip()
    while not is_valid(file_name=file_name):
        file_name = input('사용할 수 없는 문자를 입력하셨습니다. 다시 입력하세요: ').strip()

if file_name == '':
    file_name = str(todays_date)
else:
    file_name = file_name.replace(' ', '_')

while True:
    try:
        num_problem_set = int(input('이번 과제는 몇 문제인가요? 정수형으로 입력하세요: '))
        if num_problem_set <= 0:
            raise ValueError
        break
    except ValueError:
        print('바른 값을 입력하세요')

with open(f'{file_name}.sql', 'w+', encoding='utf-8') as f:
    for i in range(1, num_problem_set+1):
        f.write(f'-- 문제 {i}\n\n\n')

print(f'현재 디렉토리에 {file_name}.sql 파일이 생성되었습니다.')