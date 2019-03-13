"""
phone_book	                    return
[119, 97674223, 1195524421]	    false
[123,456,789]	                true
[12,123,1235,567,88]	        false
"""
phone_book = ["118", "97674223", "1195524421"]

def solution(phone_book):

    for i in phone_book:
        for j in phone_book:
            if i != j:
                temp_str_a = i.replace(' ','')
                temp_str_b = j.replace(' ','')

                temp_str_b = temp_str_b[0:len(temp_str_a)]

                if temp_str_a == temp_str_b: return False
                else: continue



    return True


print(solution(phone_book))