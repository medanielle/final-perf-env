#!/usr/bin/python3

import os, sys, subprocess, random

avoid_these = ['.DS_Store', 'VS_SLN_Template']

googletest_url = 'https://github.com/google/googletest.git'
testbank_url = 'https://gitlab.com/90COS/public/evaluation-prep/performance.git'
proj_path = os.path.abspath('./')
C_path = '.testbank/Basic/Dev/C_Programming'
Python_path = '.testbank/Basic/Dev/Python'
Networking_path = '.testbank/Basic/Dev/Networking'

def cleanTest():
    subprocess.run('find CProgramming/* -type l -exec rm {} +', shell=True)
    subprocess.call(['rm', '-r', 'Python'])
    subprocess.call(['mkdir', 'Python'])
    subprocess.call(['rm', '-r', 'Networking'])
    subprocess.call(['mkdir', 'Networking'])

def getRandomQuestions():
    question_container = {
        'C': set(),
        'Python': set(),
        'Network': set()
    }

    while len(question_container['C']) < 2:
        C_question = random.choice(os.listdir(C_path))
        if C_question not in avoid_these and C_question not in question_container['C']:
            question_container['C'].add(C_question)

    while len(question_container['Python']) < 2:
        Python_question = random.choice(os.listdir(Python_path))
        if Python_question not in avoid_these and Python_question not in question_container['Python']:
            question_container['Python'].add(Python_question)

    question_container['Network'].add(random.choice(os.listdir(Networking_path)))
    return question_container

def copyQuestionToTest(questions):
    for question in questions['C']:
        subprocess.call(['ln', '-s', os.path.join(proj_path, C_path, question), 'CProgramming/'])
        subprocess.call(['cp', 'CProgramming/main.cpp', f'CProgramming/{question}'])
        subprocess.call(['cp', 'CProgramming/CMakeLists.txt', f'CProgramming/{question}'])
        subprocess.call(['ln', '-s', f'{proj_path}/googletest', f'CProgramming/{question}/'])
    for question in questions['Python']:
        subprocess.call(['ln', '-s', os.path.join(proj_path, Python_path, question), 'Python/'])
    for question in questions['Network']:
        subprocess.call(['ln', '-s', os.path.join(proj_path, Networking_path, question), 'Networking/'])


def main():
    cleanTest()
    
    if not os.path.exists("googletest"):      
        subprocess.call(['git', 'clone', googletest_url])
    
    if not os.path.exists(".testbank/Basic"):
        subprocess.call(['git', 'submodule', 'update', '--init', '--recursive'])
    else:
        subprocess.call(['git', 'submodule', 'update', '--remote'])
    
    copyQuestionToTest(getRandomQuestions())

    return 0

if __name__ == "__main__":
    main()