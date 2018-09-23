import yaml


def analyze_with_file_name(file_name, script_name):
    with open("./data/" + file_name + "_data.yml", "r") as f:
        all_data = yaml.load(f)

        script_data = all_data[script_name]

        data_list = list()
        for i in script_data.values():
            data_list.append(i)
    return data_list



