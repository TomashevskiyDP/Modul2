# Дополнительное практическое задание по модулю 2

def password(n):
    result = ''
    for i in range(1, 20):
        if n <= 2 or n >= 21:
            print('Вы проиграли')
            break
        for j in range(i + 1, n + 1):
            if n % (i + j) == 0:
                result += str(i) + str(j)
    return result

print(password(int(input('Введите число от 3 до 20: '))))



