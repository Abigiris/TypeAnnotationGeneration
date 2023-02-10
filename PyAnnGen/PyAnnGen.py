import os
import json
import copy
import sys


class TypeCategory:
    Elementary = 'Elementary'
    Parametric = 'Parametric'
    Union = 'Union'
    Dynamic = 'Dynamic'
    Variable = 'Variable'
    UserDefined = 'UserDefined'


ElementaryType = ('int', 'float', 'bool', 'str', 'bytes', 'None')
ParametricType = ('list', 'tuple', 'dict', 'set', 'callable', 'generator')


def classify_a_type(t):
    # print(dir(__builtins__))
    def preprocess(t):
        std_t = t.replace('"', '').replace("'", "")
        std_t = std_t.replace('builtin.', '').replace('typing.', '')
        return std_t
    if t in ('Any', 'typing.Any', 't.Any'):
        return TypeCategory.Dynamic
    if t.startswith('_T'):
        return TypeCategory.Variable
    if t.startswith(('Union', 'Optional', 'typing.Union', 'typing.Optional', 't.Union', 't.Optional')):
        return TypeCategory.Union
    if t.startswith('builtins.'):
        t = t.split('.', maxsplit=1)[1]
    if t in dir(__builtins__) and t not in ParametricType:
        return TypeCategory.Elementary
    if '[' in t or t.lower() in ParametricType:
        return TypeCategory.Parametric
    return TypeCategory.UserDefined

type4py_dict = {}
pytype_dict = {}


def PyAnnGen(pytype_dir, type4py_dir, hityper_dir, output_dir):
    proj_list = os.listdir(pytype_dir)
    for proj in proj_list:
        with open(pytype_dir + proj) as f:
            pytype_dict = json.load(f)
        with open(type4py_dir+ proj) as f:
            type4py_dict = json.load(f)
        with open(hityper_dir + proj) as f:
            hityper_dict = json.load(f)

        d = copy.deepcopy(pytype_dict)

        def parse_type_variable(type_str):
            s = type_str.strip("'").strip('"')
            if s.startswith('_T') and len(s) > 3 and '.' not in s and '[' not in s:
                return s.lstrip('_T')
            else:
                return type_str

        def algorithm():
            def parse_point(pytype_list, type4py_list, hityper_list):
                if len(pytype_list) > 0 and classify_a_type(pytype_list[0]) in (TypeCategory.Elementary, TypeCategory.Parametric, TypeCategory.Union, TypeCategory.UserDefined):
                    return pytype_list
                if len(pytype_list) > 0 and classify_a_type(pytype_list[0]) == TypeCategory.Variable:
                    tl = []
                    tl.append(parse_type_variable(pytype_list[0]))
                    return tl
                if len(type4py_list) > 0 and len(hityper_list) == 0:
                    return type4py_list
                if len(type4py_list) == 0 and len(hityper_list) > 0:
                    return hityper_list
                if len(type4py_list) > 0 and len(hityper_list) > 0:
                    ranks = {}
                    for t in type4py_list:
                        if t not in ranks:
                            ranks[t] = 0
                        ranks[t] += (1 / (type4py_list.index(t) + 1) / len(type4py_list))
                    for t in hityper_list:
                        if t not in ranks:
                            ranks[t] = 0
                        ranks[t] += (1 / (hityper_list.index(t) + 1) / len(hityper_list))
                    ann_dict = sorted(ranks.items(), key=lambda x:x[1], reverse=True)
                    ann_list = []
                    for k in ann_dict:
                        ann_list.append(k[0])
                    return ann_list
                return []

            for filename in d:
                for func_id in d[filename]:
                    ann = parse_point(pytype_dict[filename][func_id]['return'], type4py_dict[filename][func_id]['return'], hityper_dict[filename][func_id]['return'])
                    d[filename][func_id]['return'] = ann
                    for arg in d[filename][func_id]['arguments']:
                        if arg == 'self':
                            continue
                        ann = parse_point(pytype_dict[filename][func_id]['arguments'][arg], type4py_dict[filename][func_id]['arguments'][arg], hityper_dict[filename][func_id]['arguments'][arg])
                        d[filename][func_id]['arguments'][arg] = ann

        algorithm()
        with open(output_dir + proj, 'w') as f:
            json.dump(d, f, indent=4)


if __name__ == '__main__':
    pytype_dir = sys.argv[1]
    type4py_dir = sys.argv[2]
    hityper_dir = sys.argv[3]
    output_dir = sys.argv[4]
    PyAnnGen(pytype_dir, type4py_dir, hityper_dir, output_dir)