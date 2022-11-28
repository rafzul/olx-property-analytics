import json
import ast

# open file
f = open("test-2022-11-23.json", "r")
input = f.read()
input2 = json.dump(ast.literal_eval(input))
f.write(input2)
f.close()
