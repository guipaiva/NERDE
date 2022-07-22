import json

def write_jsonl(filename, objects):
  f = open(filename, 'w')
  for object in objects:
    f.write(json.dumps(object, ensure_ascii=False) + '\n')
  f.close()

def read_jsonl(filename):
  with open(filename, 'r') as f:
    result = [json.loads(line) for line in f.readlines()]
  return result
