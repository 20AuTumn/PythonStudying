# 평균 알고리즘(Average Algorithm) : 주어진 범위에 주어진 자료에 해당하는 자료들의 평균

#[?] n명의 점수 중에서 80점 이상 90점 이하인 점수의 평균

#[1] Input : n명의 성적
data = [ 90, 65, 78, 50, 95 ]
sum = 0 # 합계를 담는 그릇
count = 0 # 개수를 담는 그릇
N = len(data) #의사코드(슈도코드)

#[2] Process : AVG = SUM / COUNT (조합의 형태)
for i in range(0, N): # 주어진 범위
    if data[i] >= 80 and data[i] <= 95: # 주어진 조건
        sum += data[i] # SUM
        count += 1 # COUNT

avg = 0.0
if sum != 0 and count != 0:
     avg = sum / count # AVERAGE

#[3] Output
print(f'80점 이상 90점 이하인 자료의 평균 : {avg:.2f}')
