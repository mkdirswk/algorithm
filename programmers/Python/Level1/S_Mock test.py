"""
문제 설명


수포자는 수학을 포기한 사람의 준말입니다. 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요

입출력 예


answers

return


[1,2,3,4,5] [1]
[1,3,2,4,2] [1,2,3]


"""
answers = [1,3,2,4,2]
def solution(answers):
    #1 : 1234512345...5
    #2 : 21232425...8
    #3 : 3311224455...10

    first_giveuper = [1,2,3,4,5] * (int(len(answers) / 5) + 1)
    second_giveuper = [2,1,2,3,2,4,2,5] * (int(len(answers) / 8) + 1)
    third_giveuper = [3,3,1,1,2,2,4,4,5,5] * (int(len(answers) / 10) + 1)

    first_answerCount = 0
    second_answerCount = 0
    third_answerCount = 0

    for i in range(len(answers)):
        if answers[i] == first_giveuper[i]: first_answerCount += 1
        if answers[i] == second_giveuper[i]: second_answerCount += 1
        if answers[i] == third_giveuper[i]: third_answerCount += 1

    result = []
    if first_answerCount == max(first_answerCount, second_answerCount, third_answerCount): result.append(1)
    if second_answerCount == max(first_answerCount, second_answerCount, third_answerCount): result.append(2)
    if third_answerCount == max(first_answerCount, second_answerCount, third_answerCount): result.append(3)

    return sorted(result)


print(solution(answers))