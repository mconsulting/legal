import os
from cleanup import cleanup

x=cleanup()

x.execute("this is a test")
print(os.listdir())


# i just went and manually deleted them through explorer, but the scaffolding is here now as a #todo item