# firstfork.py
import os
# Our child process.
def child():
  print("Hello from", os.getpid())
  os._exit(0)
# The parent process.
while (True):
  newpid = os.fork()
  if newpid == 0:
    child()
  else:
    print("Hello from parent", os.getpid(), newpid)
  if input() == "q": break
