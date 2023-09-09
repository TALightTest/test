# Example: sfilde: somma, sovle
cnt = int(await input())
for i in range(cnt):
    line = await input()
    #print("line:", line)
    nums = line.split(" ")
    a = int(nums[0])
    b = int(nums[1])
    print(a+b)