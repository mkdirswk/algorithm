"""
입출력 예제
입력: [img12.png, img10.png, img02.png, img1.png, IMG01.GIF, img2.JPG]
출력: [img1.png, IMG01.GIF, img02.png, img2.JPG, img10.png, img12.png]

입력: [F-5 Freedom Fighter, B-50 Superfortress, A-10 Thunderbolt II, F-14 Tomcat]
출력: [A-10 Thunderbolt II, B-50 Superfortress, F-5 Freedom Fighter, F-14 Tomcat]
"""

files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']


def solution(files):

    refined_list = []
    for i in files:
        refined_list.append(string_parse(i))

    refined_files = sorted(refined_list, key=lambda element: element[0])

    count = -1
    temp_list = []

    while count != 0:
        count = 0
        for m in range(len(refined_files)):
            if m != (len(refined_files) - 1):
                if refined_files[m][0] == refined_files[m + 1][0]:
                    if int(refined_files[m][1]) > int(refined_files[m + 1][1]):
                        temp_list = refined_files[m]
                        refined_files[m] = refined_files[m + 1]
                        refined_files[m + 1] = temp_list
                        count += 1

    return list_to_str_handler(refined_files,files)


def string_parse(string):
    lower_str = string.lower()

    head = ''
    num = ''
    tail = ''
    for s in lower_str:
        if 97 <= ord(s) <= 122 and num == '':
            head += s
        elif '0' <= s <= '9' and tail == '':
            num += s
        else:
            tail += s

    return [head, num, tail]


def list_to_str_handler(mylist, files):
    final_list = []
    for m in mylist:
        final_list.append("".join(m))

    refined_list = []
    for i in files:
        refined_list.append(i.lower())

    for j in final_list:
        for k in refined_list:
            if j == k:
                final_list[final_list.index(j)] = files[refined_list.index(k)]

    return final_list



print(solution(files))

