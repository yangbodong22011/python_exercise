from collections import OrderedDict

program = OrderedDict()

program["ddd"] = "ddd"
program["aaa"] = "aaa"
program["bbb"] = "bbb"
program["ccc"] = "ccc"

for k,v in program.items():
	print(k + ":" + v)