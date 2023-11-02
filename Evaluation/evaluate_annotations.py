import ast
import astunparse
import json
import os
import re
import sys


class Metric:
    Match = 'Match'
    Similar = 'Similar'
    Parametric = 'Parametric'
    Partial = 'Partial'
    Dynamic = 'Dynamic'
    Variable = 'Variable'
    Different = 'Different'
    Fail = 'Fail'


class TypeCategory:
    Elementary = 'Elementary'
    Parametric = 'Parametric'
    Union = 'Union'
    Dynamic = 'Dynamic'
    Variable = 'Variable'
    UserDefined = 'UserDefined'


TOP_N = 1
TYPE_LIMIT = (TypeCategory.Elementary, TypeCategory.Parametric, TypeCategory.Union,
              TypeCategory.Dynamic, TypeCategory.Variable, TypeCategory.UserDefined)

category_results = {
    'ret': {
        'points': 0,
        'Cover': 0,
        'Match': 0,
        'Similar': 0,
        'Parametric': 0,
        'Partial': 0,
        'Dynamic': 0,
        'Variable': 0,
        'Different': 0
    },
    'arg': {
        'points': 0,
        'Cover': 0,
        'Match': 0,
        'Similar': 0,
        'Parametric': 0,
        'Partial': 0,
        'Dynamic': 0,
        'Variable': 0,
        'Different': 0
    }
}


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



def parse_annotation_basic(type_str):
    type_str = type_str.replace('\'', '').replace('\"', '').replace(' ', '')
    type_str = type_str.replace('[,]', '')
    if type_str.endswith('[]') and type_str.count(']') == 1:
        type_str = type_str.replace('[]', '')
    # type_str = type_str.replace('[]', '')
    return type_str


def normalize_one_type_basic(type_str):
    try:
        type_str = astunparse.unparse(ast.parse(type_str)).replace('\n', '')
        s = type_str.lower()
        s = s.replace(' ', '').replace('\t', '').replace('\n', '')
        s = s.replace('\'', '').replace('\"', '')
        if s in ('noreturn', 'nonetype'):
            s = 'none'
        if s in ('function', 'builtins.function'):
            s = 'callable'
        if s in ('builtins.object', 'object'):
            s = 'any'
        return s
    except:
        return type_str


def normalize_one_type_advanced(type_str, has_basic_normalized=False):
    s = type_str
    if not has_basic_normalized:
        s = normalize_one_type_basic(s)
    basic_str = s

    while True:
        pattern = re.findall(r'([a-z0-9_]+\.[a-z0-9_]+)', s)
        if not pattern:
            break
        for g in pattern:
            s = s.replace(g, g.split('.')[-1])
    # if s != basic_str:
    if '...' not in s and '.' in s:
        # print(type_str + ' === ' + basic_str + ' === ' + s)
        pass
    return s


def split_type(type_str):
    try:
        type_str = type_str.replace("optional[", "union[none,")
        types_stack = [type_str]
        base_types = []
        while types_stack:
            type_code = types_stack.pop()
            code_groups = str.split(type_code, "union[", maxsplit=1)
            if len(code_groups) < 2:
                base_types.append(type_code)
                continue
            group1 = code_groups[0]
            group2 = code_groups[1]
            brackets_stack = []
            split_index = -1
            for i in range(len(group2)):
                if group2[i] == '[':
                    brackets_stack.append('[')
                elif group2[i] == ']':
                    if not brackets_stack:
                        split_index = i
                        break
                    else:
                        brackets_stack.pop()
            group3 = group2[split_index + 1:]
            group2 = group2[:split_index]
            elem_tree = ast.parse(group2).body[0]
            if hasattr(elem_tree.value, "elts"):
                for elem_node in elem_tree.value.elts:
                    elem_str = astunparse.unparse(elem_node).strip('\n')
                    new_t = group1 + elem_str + group3
                    types_stack.append(new_t)
            else:
                new_t = group1 + group2 + group3
                types_stack.append(new_t)
        types_set = set()
        for bt in base_types:
            types_set.add(bt)
        return types_set
    except:
        # print('Error: split type str')
        types_set = set()
        types_set.add(type_str)
        return types_set


def is_similar_match(gt_type, res_list):
    gt = normalize_one_type_basic(gt_type)
    l = [normalize_one_type_basic(x) for x in res_list]
    if gt in l:
        return Metric.Similar
    gt = normalize_one_type_advanced(gt_type)
    l = [normalize_one_type_advanced(x) for x in res_list]
    if gt in l:
        return Metric.Similar
    return Metric.Different


def is_parametric(type_str):
    type_str = type_str.lower()
    for generic in ParametricType:
        if type_str == generic or type_str.startswith(generic + '['):
            return True
    if '[' in type_str:
        may_other_type = type_str.split('[', maxsplit=1)[0]
        if may_other_type.isalpha() and not may_other_type.startswith('union') and not may_other_type.startswith('optional'):
            return True
    return False


def is_parametric_match(gt_type, res_list):
    gt_type = normalize_one_type_advanced(gt_type)
    if is_parametric(gt_type):
        res_list = [normalize_one_type_advanced(x) for x in res_list]
        param_type_match = r'(.+?)\[(.+)\]'
        if not re.match(param_type_match, gt_type):
            gt_type = gt_type + '[Any]'
        for p in res_list:
            if re.match(param_type_match, p):
                if re.match(param_type_match, gt_type).group(1) == re.match(param_type_match, p).group(1):
                    return Metric.Parametric
            else:
                if re.match(param_type_match, gt_type).group(1).lower() == p.lower():
                    return Metric.Parametric
    return Metric.Different


def is_partial_match(gt_type, res_list):
    gt_type = normalize_one_type_advanced(gt_type)
    res_list = [normalize_one_type_advanced(x) for x in res_list]
    gt_set = split_type(gt_type)
    is_partial = False
    for res_type in res_list:
        res_set = split_type(res_type)
        if res_set == gt_set:
            return Metric.Similar
        elif len(res_set) == len(res_set.union(gt_set)):
            return Metric.Partial
        elif len(res_set.intersection(gt_set)):
            is_partial = True
    if is_partial:
        return Metric.Partial
    else:
        return Metric.Different


def is_dynamic_match(gt_type, res_list):
    gt_type = normalize_one_type_advanced(gt_type)
    res_list = [normalize_one_type_advanced(x) for x in res_list]
    if gt_type == "any" or "any" in res_list:
        return Metric.Dynamic
    return Metric.Different


def is_variable_match(gt_type, res_list):
    if gt_type.count('@@') == 1:
        for res in res_list:
            if res.count('@@') == 1:
                return Metric.Match
        return Metric.Variable

    if gt_type.count('@@') > 1:
        gt_list = gt_type.split('@@')
        may_match = [x for x in gt_list if x in res_list]
        if len(may_match) > 0:
            return Metric.Variable
        return Metric.Different

    for res in res_list:
        if res.count('@@') == 0:
            continue
        elif res.count('@@') == 1:
            return Metric.Variable
        else:
            gt = normalize_one_type_advanced(gt_type)
            tv_list = res.split('@@')
            if gt in [normalize_one_type_advanced(x) for x in tv_list]:
                return Metric.Variable

    return Metric.Different


def evaluate_point(res_list, gt_list):
    if len(gt_list) != 1:
        print('ERROR: no exact ground truth type')
        exit()

    res_list = res_list[:TOP_N]
    gt_type = gt_list[0]
    res_list = [parse_annotation_basic(x) for x in res_list]
    gt_type = parse_annotation_basic(gt_type)

    if gt_type in res_list:
        return Metric.Match

    if is_similar_match(gt_type, list(res_list)) == Metric.Similar:
        return Metric.Similar

    ''' Top-N '''
    if is_partial_match(gt_type, list(res_list)) == Metric.Similar:
        return Metric.Similar

    for single_res in res_list:
        new_res_list = []
        new_res_list.append(single_res)
        if is_parametric_match(gt_type, list(new_res_list)) == Metric.Parametric:
            return Metric.Parametric
        if is_partial_match(gt_type, list(new_res_list)) == Metric.Partial:
            return Metric.Partial
        if is_dynamic_match(gt_type, list(new_res_list)) == Metric.Dynamic:
            return Metric.Dynamic
        var_match_res = is_variable_match(gt_type, list(new_res_list))
        if var_match_res != Metric.Different:
            return var_match_res

    return Metric.Different


def evaluate_function(res_dict, gt_dict, filename=None, func_lo=None):
    metric = {Metric.Match: 0,
              Metric.Similar: 0,
              Metric.Parametric: 0,
              Metric.Partial: 0,
              Metric.Dynamic: 0,
              Metric.Variable: 0,
              Metric.Different: 0}
    if len(gt_dict['return']) > 0:
        if classify_a_type(gt_dict['return'][0]) in TYPE_LIMIT:
            category_results['ret']['points'] += 1
    if len(res_dict['return']) > 0 and len(gt_dict['return']) > 0:
        if classify_a_type(gt_dict['return'][0]) in TYPE_LIMIT:
            res = evaluate_point(res_dict['return'], gt_dict['return'])
            category_results['ret']['Cover'] += 1
            category_results['ret'][res] += 1
            metric[res] += 1
    for arg in res_dict['arguments']:
        if arg == 'self':
            continue
        if len(gt_dict['arguments'][arg]) > 0:
            if classify_a_type(gt_dict['arguments'][arg][0]) in TYPE_LIMIT:
                category_results['arg']['points'] += 1
        if len(res_dict['arguments'][arg]) > 0 and len(gt_dict['arguments'][arg]) > 0:
            if classify_a_type(gt_dict['arguments'][arg][0]) in TYPE_LIMIT:
                res = evaluate_point(res_dict['arguments'][arg], gt_dict['arguments'][arg])
                category_results['arg']['Cover'] += 1
                category_results['arg'][res] += 1
                metric[res] += 1
    return metric


def evaluate_project(res_dict, gt_dict):
    metric = {Metric.Match: 0,
              Metric.Similar: 0,
              Metric.Parametric: 0,
              Metric.Partial: 0,
              Metric.Dynamic: 0,
              Metric.Variable: 0,
              Metric.Different: 0}
    for filename in gt_dict:
        if '/venv/' in filename:
            continue
        for func_id in res_dict[filename]:
            func_metric = evaluate_function(res_dict[filename][func_id], gt_dict[filename][func_id])
            for m in metric:
                metric[m] += func_metric[m]
    return metric


def standardize_results(category_results):
    res = {'ret': {}, 'arg': {}, 'total': {}}
    for c in ('ret', 'arg'):
        res[c] = {
            'points': category_results[c]['points'],
            'Coverage': category_results[c]['Cover'],
            'Match': category_results[c]['Match'] + category_results[c]['Similar'],
            'Parametric': category_results[c]['Parametric'],
            'Union': category_results[c]['Partial'],
            'Dynamic': category_results[c]['Dynamic'],
            'Variable': category_results[c]['Variable'],
            'Mismatch': category_results[c]['Different']
        }
    for m in res['ret']:
        res['total'][m] = res['ret'][m] + res['arg'][m]
    return res


if __name__ == '__main__':
    results_dir = sys.argv[1]
    gt_dir = sys.argv[2]
    output_path = sys.argv[3]
    proj_list = os.listdir(results_dir)
    for proj in proj_list:
        res_path = results_dir + proj
        gt_path = gt_dir + proj
        if not os.path.exists(gt_path):
            print("WARNING: no ground truth for " + proj)
            continue
        with open(res_path) as f:
            res_dict = json.load(f)
        with open(gt_path) as f:
            gt_dict = json.load(f)
        metric = evaluate_project(res_dict, gt_dict)  # metric is the 'total' category, no use

    with open(output_path, 'w') as f:
        json.dump(standardize_results(category_results), f, indent=4)


