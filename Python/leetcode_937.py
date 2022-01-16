# leetcode_937.py
# 로그 파일 재정렬
# 요구 조건을 얼마나 깔끔하게 처리할 수 있는지를 묻는 문제.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
               
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x:(x.split()[1:], x.split()[0]))
        return letters + digits
        
# 람다 표현식
# 식별자 없이 실행 가능한 함수, 함수 선언 없이도 하나의 식으로 함수를 단순하게 표현할 수 있음.

# letters.sort(key = lambda x:(x.split()[1:], x.split()[0])) 의미
# 문자순 정렬 후 문자가 동일한 경우 번호순으로 정렬

# s = ['2 A','1 B','4 C','1 A']
# sorted(s) = ['1 A','1 B','2 A','4 C']

# s.sort(key = lambda x:(x.split()[1:], x.split()[0]))
# s = ['1 A','2 A','1 B','4 C']
