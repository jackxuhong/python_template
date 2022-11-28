import os, sys

def config():
    # Get venv root dir
    venv = getattr(sys, "prefix", None)
    cfg_file = os.path.join(venv, 'etc', 'app1.cfg')
    print(cfg_file)

def my_func1():
    return "my application works!"

if __name__ == "__main__":
    config()
    print(my_func1())
