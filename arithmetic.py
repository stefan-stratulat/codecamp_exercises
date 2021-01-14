numbers= ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]
def arithmetic_arranger(problems):
  arranged_problems = " "
  #create a for loop to separate the elements in the list
  for problem in problems:
      separated_number = problem.split()
      #print(separated_number)
      if separated_number[1]=="+":
        result = int(separated_number[0])+int(separated_number[2])
      if separated_number[1]=="-":
        result = int(separated_number[0])-int(separated_number[2])
      arranged_problems = "  "+separated_number[0]+'\n'+separated_number[1]+' '+separated_number[2]+'\n.......\n'+str(result)
      print(arranged_problems)

  #return arranged_problems

arithmetic_arranger(numbers)