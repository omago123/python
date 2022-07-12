import re
# abcd ,book, desk
# ca?e
# care, cafe ,case, cave

p = re.compile("ca.e")
# . (ca.e) : 하나의문자를 의미   > care, cafe , case (O)  | caffe (X)
# ^ (^de) : 문자열의 시작  > desk, destination (O) | fade(X)
# $ (se$) : 문자열의 끝 > case, base (O) | face(X)

def print_match(m):
    if m:
        print(m.group())
    else:
        print("매칭되지 않음")

m = p.match("case")
print_match(m)