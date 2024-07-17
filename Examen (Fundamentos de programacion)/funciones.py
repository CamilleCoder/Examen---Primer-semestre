


def mayor(a:list, b:list):
            for i in a:
                for j in i:
                    b.append(i[j])
            return b

def menor(a:list, b:list):
            for i in a:
                for j in i:
                    b.append(i[j])
            return b

def promedio(a:list, b:list):
            for i in a:
                for j in i:
                    b.append(i[j])
            ave = sum(b) / len(a)
            return ave

def reports(a:list):
       for i in a:
              for j in i:
                    print(f"{i.keys()} - {i[j]} - {int(i[j] * 0.07)} - {int(i[j] * 0.12)} - {int((i[j]) - (i[j] * 0.07 + i[j] * 0.12))}")

