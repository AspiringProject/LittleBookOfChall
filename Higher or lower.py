import random
def number_gen():
  score = 0
  print("get 10 in a row to win\n")
  while score < 10:
    num = random.randint(1,13)
    print("the number is:",num)
    while True:
      guess = input("is the next number higher(h) or lower(l)?: ")
      if guess == "h" or guess == "l":
        break
      else:
        print("invalid answer\n")
    nxtnum = random.randint(1,13)
    if nxtnum > num and guess == "l":
      print("that is wrong, the number was: ",nxtnum)
      score = 0
      print("your score is: ",score,"\n")
    elif nxtnum > num and guess == "h":
      print("that is right, the number was: ",nxtnum)
      score = score + 1
      print("your score is: ",score,"\n")
    elif nxtnum < num and guess == "l":
      print("that is right, the number was: ",nxtnum)
      score = score + 1
      print("your score is: ",score,"\n")
    elif nxtnum < num and guess == "h":
      print("that is wrong, the number was: ",nxtnum)
      score = 0
      print("your score is: ",score,"\n")
  print("you win!")

number_gen()