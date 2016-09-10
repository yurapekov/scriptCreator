#!/usr/bin/env python

import sys
import os
import argparse
# project ScriptCreator
# main program file
# windows-version, unix-version
# Author: Pekov Yury

class Parameter:
    def __init__(self, name, letter, paramType):
        self.name = name # str
        self.letter = letter # str
        self.paramType = paramType # str
        self.default = None # bool/str

"""
This function construct parser string in output file, e.g.:
parser.add_argument('-o',
                  '--outFileName',
                  type=str,
                  default='out.txt',
                  help='name of output file [string], default value = out.txt')

In:
    1) param [Parameter] - input parameter data
    2) outFile [file] - flow to the output file
Out:
    (void)
"""
def addParser(param, outFile, shift):
    localShift = len('parser.add_option(')*' '
    outFile.write(shift + "parser.add_argument('-" + param.letter + "',\n")
    outFile.write(shift + localShift + "'--" + param.name + "',\n")
    outFile.write(shift + localShift + "type=" + param.paramType + ",\n")
    '''
    if param.paramType == 'bool':
        if param.defaul
        outFile.write(shift + localShift + "action='store',\n")
    '''
    if param.default != None:
        outFile.write(shift + localShift + "default = " + param.default + ",\n")
    outFile.write(shift + localShift + "help = ' [" + param.paramType + "], ")
    if param.default != None:
        outFile.write("default value = " + param.default + "')\n")
    else:
        outFile.write("no default value')\n")

"""
This function construct option module in output file, e.g.:
if options.outFileName == None:
    outFileName = "res.py"

In:
    1) param [Parameter] - input parameter data
    2) outFile [file] - flow to the output file
Out:
    (void)
"""
def addOption(param, outFile, shift):
    if param.default == None:
        outFile.write(shift + 'if args.' + param.name + ' == None:\n')
        outFile.write(shift + '    print("Please, define --' + param.name + ' parameter. To read help use -h. Program is broken.")\n')
        outFile.write(shift + '    sys.exit(1)\n')

def main():
    #[options]
    parser = argparse.ArgumentParser(description='Default description', add_help=True, version='1.0.0')
    parser.add_argument(
            '-n',
            '--name',
            type=str,
            default='newProject',
            help='Name of the new project. Output file will be named as name.py [string], default value = newProject'
            )
    parser.add_argument(
            '-p', 
            '--parameters',
            type=str,
            help='''
            List with parameters of output sctipt, format: 'name:letter:type:default#name:letter:type:default'. If
            there is not default value for some parameter, type 'None' instead of 'default'. [string], no default value'
            '''
            )
    args = parser.parse_args()
    # END_OF [options]

    shift = '    '

    outFileName = args.name + '.py'
    outFile = open(outFileName, 'w')

    outFile.write('#!/usr/bin/env python3.3\n\n')
    outFile.write('import sys\n')
    outFile.write('import argparse\n')
    outFile.write('import subprocess\n')
    outFile.write('# project ' + args.name + '\n')
    outFile.write('# main program file\n')
    outFile.write('\n')
    outFile.write('def main():\n')
    outFile.write(shift + '#[options]\n')
    outFile.write(shift + "parser = argparse.ArgumentParser()\n")

    paramList = [] 
    colonDelimList = args.parameters.split('#')
    for colonDelimListItem in colonDelimList:
        dotDelimList = colonDelimListItem.split(':')
        newParam = Parameter(dotDelimList[0], dotDelimList[1], dotDelimList[2])
        if len(dotDelimList) == 4:
            newParam.default = dotDelimList[3]
        paramList.append(newParam)

    for param in paramList:
        addParser(param, outFile, shift)
    outFile.write(shift + 'args = parser.parse_args()\n')

    for param in paramList:
        outFile.write("\n")
        addOption(param, outFile, shift)
    outFile.write(shift + '# END_OF [options]\n\n')
    outFile.write(shift + 'return 0\n')
    outFile.write('# def main\n')

    outFile.write('\n')
    outFile.write("if __name__ == '__main__':\n")
    outFile.write(shift + "sys.exit(main())\n")
    outFile.close()

    os.system('chmod +x ' + outFileName)

    return 0
# def main

if __name__ == '__main__':
    sys.exit(main())

