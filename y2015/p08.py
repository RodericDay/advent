import json


lines = df.read_text().splitlines()
ans1 = sum(len(ln) - len(eval(ln)) for ln in lines)
ans2 = sum(len(json.dumps(ln)) - len(ln) for ln in lines)
