import sys

def read_file(file_name):
    return [line.rstrip('\n') for line in open(file_name)]

def split(apx_list):
    arg = [strip_arg(x) for x in apx_list if 'arg' in x]
    att = [strip_att(x) for x in apx_list if 'att' in x]
    return arg, att

def strip_arg(arg):
    return arg.replace('arg(', '').replace(').','').upper()

def strip_att(att):
    return att.replace('att(', '').replace(').','').replace(',','|->').upper()

def write_file(arguments, attacks, file_name='temp.txt'):
    f = open(file_name, 'wb')
    f.write('ARGUMENTS={')
    for i, arg in enumerate(arguments):
        f.write(arg)
        if i != len(arguments) - 1:
            f.write(',')
    f.write('};\n')
    f.write('attacks={')
    for i, att in enumerate(attacks):
        f.write(att)
        if i != len(attacks) - 1:
            f.write(', ')
    f.write('}\n')
    f.close()

if __name__ == '__main__':
    save_name = 'temp.txt'
    if len(sys.argv) > 1:
        apx_file = sys.argv[1]
    if len(sys.argv) > 2:
        save_name = sys.argv[2]

    apx = read_file(apx_file)
    arg, att = split(apx)
    write_file(arg, att, save_name)
