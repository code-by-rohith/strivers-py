def main(nums):
    temp = []
    samp = []
    cons = 0
    for i in nums:
        if i != -1:
            temp.append(i)
            cons = 0
        else:
            cons += 1
            if cons <= len(temp):
                a = temp[-cons]
                samp.append(a)
            else:
                samp.append(-1)
    return samp

nums = [1,-1,2,-1,-1]
print(main(nums))


