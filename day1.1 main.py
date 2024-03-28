def main():
    file = "inputs/day1.txt"
    
    with open(file) as text:
        lines = text.read().splitlines()
        value_sum = 0
        for line in lines:
            nums = [char for char in line if char.isnumeric()]
            value_sum += int(str(nums[0]) + str(nums[-1]))    
        print(value_sum)
      
main()
            