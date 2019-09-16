# *For converting any directory into a python module we need two file 
# in that module viz __init__.py __main__.py 
# *If we print("Hwllo") in __main__.py then on executing the 
# following command "python modulename" o/p will b Hwllo
# *For Argument passing we will make use of "ArgumentParser" class from "argparse" module
# and make use of the following given object funtions for passing the argument at exe-
#cuting the python command

# **I have converted "module" dir to a "python module" and u can see the __main__.py
#file

#Function which for used in __main__.py for argument passing
from argparse import ArgumentParser as Parser
parser = Parser(program = "python")
parser.add_argument("--name","-n",type=str)
parser.add_argument("--item","-i", type =str)
parser.add_argument("--amount","-a",type=str)
parser.add_argument("--team","-t", type =str)
args = parser.parse_args()
#args =[parser.name,parser.item,parser.amount,parser.team]
print(args.name) 
