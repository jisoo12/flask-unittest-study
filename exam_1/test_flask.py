from my_flask import hello, world

def test_hello():
  rst = hello()
  assert "Hello!" == rst

def test_world():
  rst = world()
  assert "World" == rst