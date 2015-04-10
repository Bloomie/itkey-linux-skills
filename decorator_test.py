def counted(fn):
  def wrapper(*args, **kwargs):
    wrapper.called += 1
    if wrapper.called > 3:
      print "that's enough!"
    else: 
      try:
        return fn(*args, **kwargs)
      except:
        pass

  wrapper.called = 0
  return wrapper

@counted
def foo():
  print "hey"
  raise Exception("nooo")


for i in xrange(5):
  foo()

