class Solution:
    def countSeniors(self, details: List[str]) -> int:
        phone_no = []
        gender = []
        age = []
        seat = []
        a = ""
        phone = ""
        s = ""
        output = 0

        for detail in details:
            # print(len(detail))
            for i in range(0,10):
                phone = phone + detail[i]
            phone_no.append(phone)
            phone = ""
            gender.append(detail[i+1])
            for j in range(11,13):
                a = a + detail[j]
            age.append(int(a))
            a = ""
            for k in range(13,len(detail)):
                s = s + detail[k]
            seat.append(detail[k])
            s = ""

        # print(phone_no)
        # print(gender)
        # print(age)
        # print(seat)

        for a in age:
            if a > 60:
                output += 1
        return output
        