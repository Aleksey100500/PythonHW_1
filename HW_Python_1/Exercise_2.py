# 2. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

xyz = ['x', 'y', 'z']
nums = []

for i in range(3):
    nums.append(input(f"Введите значение {xyz[i]}: "))

left = not (nums[0] or nums[1] or nums[2])
right = not nums[0] and not nums[1] and not nums[2]

if left == right:
    print("Утверждение истинно")
else:
    print("Утверждение ложно")