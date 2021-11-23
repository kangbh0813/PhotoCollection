data = "hello"
with open("test.txt", "w") as fp:
    fp.write(data)

with open("test.txt", "r") as fp:
  print(fp.read())


  