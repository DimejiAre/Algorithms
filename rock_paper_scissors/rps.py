#!/usr/bin/python

import sys

# def rock_paper_scissors(n):
#   outcomes = []
#   plays = ['rock', 'paper', 'scissors']

#   def find_results(rounds_to_go, results=[]):
#     # if rounds = 0
#       # append results to outcomes
#       # then retun
#     # iterate over plays
#       # new result concatenate our results with our plays ** newres = results + [play]
#       # recursive call using roundstogo - 1, newresult

#   # call find_results pass in n, []
#       pass 
#   # return the outcomes
#   pass

def rock_paper_scissors(n):
  outcomes = []
  plays = ['rock', 'paper', 'scissors']

  def find_results(rounds_to_go, results=[]):
    if rounds_to_go == 0:
      return outcomes.append(results)
    for play in plays:
      new_result = results + [play]
      find_results(rounds_to_go - 1, new_result)

  find_results(n, [])
  return outcomes

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')