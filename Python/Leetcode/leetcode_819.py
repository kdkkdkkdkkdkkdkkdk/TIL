# leetcode_819.py
# 금지된 단어를 제외한 가장 흔하게 당장하는 단어를 출력하는 문제.

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(
            r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.defaultdict(int)
        for word in words:
            counts[word] += 1

        return max(counts, key=counts.get)

        # or

        counts = collections.Counter(words)
        # 가장 흔하게 등장하는 단어의 첫 번째 인덱스 리턴
        return counts.most_common(1)[0][0]


# 리스트 컴프리헨션
# re.sub(pattern, nex_text, text)
# text 에서 pattern 에 맞는 부분을 new_text로 대체하라

# collections - 컨테이너 데이터형
# Counter - 해시 가능한 객체를 세는데 사용하는 딕셔너리 서브 클래스
#           요소가 딕셔너리 키로 저장되고 개수가 딕셔너리값으로 저장되는 컬랙션
# most_coomon([n]) - n개의 가장 흔한 요소와 그 개수를 가장 흔한 것부터 가장 적은 것 순으로 나열한 리스트를 반환
#                    n이 생략되거나 None이면, most_common()은 계수기의 모든 요소를 반환
#                    개수가 같은 요소는 처음 발견된 순서를 유지
