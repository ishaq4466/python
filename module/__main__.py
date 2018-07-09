from argparse import ArgumentParser as Parser

from program15 import setdata, get_template,render_template


parser = Parser(prog = "module")
parser.add_argument("--name","-n",type=str)
parser.add_argument("--item","-i", type =str)
parser.add_argument("--amount","-a",type=int)
parser.add_argument("--team","-t", type =str)
args = parser.parse_args()
data =[args.name,args.item,args.amount,args.team]

#print(get_template("module/template.txt"))
#print(setdata(*data))
#print(setdata(data))
#==>{'name': ['ishaq', 'thor', '123', 'titan'], 'item': None, 'amount': None, 'team': None}


print(render_template(get_template("module/template.txt"),setdata(*data)))


