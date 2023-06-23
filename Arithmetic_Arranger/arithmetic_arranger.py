def arithmetic_arranger(problems, answers=False):
  nums1 = list()
  ops = list()
  nums2 = list()
  results = list()
  problem_counter = 0
  
  for sum in problems:
    problem_counter = problem_counter + 1
    if(problem_counter > 5):
      return "Error: Too many problems."
      
    lists = sum.split()
    
    if(lists[1] != '+' and lists[1] != '-'):
      return "Error: Operator must be '+' or '-'."

    if len(lists[0]) > 4 or len(lists[2]) > 4:
      return "Error: Numbers cannot be more than four digits."
    
    try:
      nums1.append(int(lists[0]))
      ops.append(lists[1])
      nums2.append(int(lists[2]))
    except:
      return "Error: Numbers must only contain digits."
    
    if lists[1] == '+':
      results.append(int(lists[0]) + int(lists[2]))
    else:
      results.append(int(lists[0]) - int(lists[2]))

  line0 = str()
  line1 = str()
  line2 = str()
  line3 = str()

  for i in range(len(nums1)):
    cwidth = max(len(str(nums1[i])), len(str(nums2[i])))+2
    line0 = line0 + f"{str(nums1[i]):>{cwidth}}    "
    line1 = line1 + f"{ops[i]:<{2}}{str(nums2[i]):>{cwidth - 2}}    "
    line2 = line2 + "-" * cwidth + "    "
    line3 = line3 + f"{str(results[i]):>{cwidth}}    "

  if answers:
    return (line0 + '\n' + line1 + '\n' + line2 + '\n' + line3)
  else:
    return (line0 + '\n' + line1 + '\n' + line2) 
    
