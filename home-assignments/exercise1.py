import json
import yaml
import operator

# nested loops for building output dictionary.
# first loop -> iterates ages in buckets and creates key values in output dictionary
# second loop -> iterates people names and ages and checks if matches age in bucket
def print_output():
    for Iteration in range(len(buckets) - 1):
        keyStr = str(buckets[Iteration]) + ' - ' + str(buckets[Iteration + 1])   # Key of specific range
        dict2yaml[keyStr] = []                                                                       # Dictionary init
        for key in pplDic:
            if pplDic[key] >= buckets[Iteration] and pplDic[key] < buckets[Iteration + 1]: # compares age to values in bucket
                dict2yaml[keyStr].append(key)                                                                   # adds value name to output dictionary


if __name__ == "__main__":
    with open('c:\input.json') as json_file:
        data = json.load(json_file)  # read json file into var

    pplDic = data["ppl_ages"]                                   # this is the nested hash (dictionary) of names:ages
    buckets = data["buckets"]                                  # ages dictionary
    buckets.sort()

    # Find max value in dictionary and add it to buckets dictionaty of ages
    keyWithMaxValue = max(pplDic.items(), key=operator.itemgetter(1))[0]
    maxValue = pplDic[keyWithMaxValue]
    buckets.append(maxValue)
    buckets = [0] + buckets         # setting '0' as lowest age

    dict2yaml = {}

    print_output()

    with open('c:\Ex1output.yaml', 'w') as yaml_output:
        yaml.dump(dict2yaml, yaml_output, default_flow_style=False, allow_unicode=True)