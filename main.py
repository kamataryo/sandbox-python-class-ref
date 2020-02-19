class MYCLASS:
  def __init__(self):
    self.data99 = []
  data1=""
  data2=""

def main():
  ary = []
  cls = MYCLASS()
  cls.data1="aaaa1"
  cls.data2="aaaa2"
  cls.data99.append("D01-1")
  cls.data99.append("D01-2")
  ary.append(cls)

  cls = MYCLASS()
  cls.data1="bbbb"
  cls.data99.append("D02-1")
  cls.data99.append("D02-1")
  ary.append(cls)

  cls = MYCLASS()
  cls.data1="ccccc"
  cls.data99.append("D03-1")
  cls.data99.append("D03-2")
  ary.append(cls)

  print(ary[0].data1)
  print(ary[1].data1)
  print(ary[2].data1)
  print(ary[0].data99)
  print(ary[1].data99)
  print(ary[2].data99)

main()
