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


ElementaryType = ('int', 'float', 'bool', 'str', 'bytes', 'None', 'NoneType', 'NoReturn')
ParametricType = ('list', 'tuple', 'dict', 'set', 'callable', 'generator', 'sequence', 'iterable', 'iterator',
                  'collection', 'mapping', 'type')


def classify_a_type(t):
    # print(dir(__builtins__))
    def preprocess(t):
        std_t = t.replace('"', '').replace("'", "")
        std_t = std_t.replace('builtin.', '').replace('typing.', '')
        return std_t
    t = t.replace('"', '').replace("'", "")
    if t in ('Any', 'typing.Any', 't.Any', 'any', 'object', 'builtins.object'):
        return TypeCategory.Dynamic
    if t.startswith('_T') or '@@' in t:
        return TypeCategory.Variable
    if t.startswith(('Union', 'Optional', 'typing.Union', 'typing.Optional', 't.Union', 't.Optional')):
        return TypeCategory.Union
    if t in ElementaryType or t.replace('builtins.', '').replace('typing.', '') in ElementaryType:
        return TypeCategory.Elementary
    if t.replace('builtins.', '').replace('typing.', '').lower() in ParametricType:
        return TypeCategory.Parametric
    if (t.startswith('[') and t.endswith(']')) or (t.startswith('(') and t.endswith(')')) or (t.startswith('{') and t.endswith('}')):
        return TypeCategory.Parametric
    if '[' in t and t.endswith(']'):
        return TypeCategory.Parametric
    return TypeCategory.UserDefined

# type4py_dict = {}
# pytype_dict = {}


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
            if s.count('@@') == 2:
                s_groups = s.split('@@')
                return s_groups[1]
            if s.count('@@') > 2:
                only_type_str = s.split('@@', 1)[1]
                new_ann = 'Union[' + only_type_str.replace('@@', ',').rstrip(',') + ']'
                return new_ann
            if s.count('@@') == 1:
                if len(s) > 5 and '.' not in s and '[' not in s:
                    return s.lstrip('_T').rstrip('@@')
            if s.startswith('_T') and len(s) > 5 and '.' not in s and '[' not in s:
                return s.lstrip('_T').rstrip('@@')
            else:
                return type_str

        def parse_raw_type(type_str):
            type_str = type_str.replace('\'', '').replace('\"', '').replace(' ', '')
            type_str = type_str.replace('typing.', '').replace('builtins.', '')
            type_str = type_str.replace('[,]', '').replace('[]', '')
            if type_str.lower() in ParametricType:
                type_str = type_str.lower()
                type_str = type_str.capitalize()
            for param_type in ParametricType:
                if type_str.startswith(param_type + '['):
                    type_str = type_str.replace(param_type, param_type.capitalize(), 1)
                    break
            return type_str

        def algorithm():
            def parse_point(pytype_list, type4py_list, hityper_list):
                pytype_list = [x for x in pytype_list if len(x) > 0]
                type4py_list = [x for x in type4py_list if len(x) > 0]
                hityper_list = [x for x in hityper_list if len(x) > 0]

                if len(pytype_list) + len(type4py_list) + len(hityper_list) == 0:
                    return []
                if len(pytype_list) > 0 and classify_a_type(pytype_list[0]) in (TypeCategory.Elementary, TypeCategory.Parametric, TypeCategory.Union, TypeCategory.UserDefined):
                    return pytype_list
                if len(pytype_list) > 0 and classify_a_type(pytype_list[0]) == TypeCategory.Variable:
                    new_type_str = parse_type_variable(pytype_list[0])
                    if '@@' not in new_type_str:
                        tl = []
                        tl.append(new_type_str)
                        return tl
                if len(type4py_list) > 0 and len(hityper_list) == 0:
                    return type4py_list
                if len(type4py_list) == 0 and len(hityper_list) > 0:
                    return hityper_list
                if len(type4py_list) > 0 and len(hityper_list) > 0:
                    ranks = {}
                    for t in type4py_list:
                        idx = type4py_list.index(t)
                        t = parse_raw_type(t)
                        if t not in ranks:
                            ranks[t] = 0
                        ranks[t] += (1 / (idx + 1) / len(type4py_list))
                    for t in hityper_list:
                        idx = hityper_list.index(t)
                        t = parse_raw_type(t)
                        if t not in ranks:
                            ranks[t] = 0
                        ranks[t] += (1 / (idx + 1) / len(hityper_list))
                    ann_dict = sorted(ranks.items(), key=lambda x:x[1], reverse=True)
                    ann_list = []
                    for k in ann_dict:
                        ann_list.append(k[0])
                    return ann_list
                return pytype_list

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