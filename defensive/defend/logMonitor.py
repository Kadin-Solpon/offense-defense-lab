import re

successfullRegex = re.compile(r"Accepted password for (.+) from (.+) port (\d+) ssh2")
failedRegex = re.compile(r"Failed password for (.+) from (.+) port (\d+) ssh2")

logFilePath = '/var/log/auth.log'


def matchFunction(line):
    success = re.search(successfullRegex, line)
    unsuccessfull = re.search(failedRegex, line)

    if success != None:
        return (1,success)
    
    if unsuccessfull != None:
        return (2,unsuccessfull)
    
    return (0, 0)
     
def monitor_log():

    with open(logFilePath, 'r') as file:

        file.seek(0,2)
        failCounter = 0
        num = 0

        while num != 1:
            line = file.readline()
            if line:
                num,matchObj = matchFunction(line = line)
                if num == 2:
                    failCounter += 1
        return f"{matchObj.group(2)} successfully logged in as {matchObj.group(1)} on port {matchObj.group(3)}. This took {failCounter} attempts"