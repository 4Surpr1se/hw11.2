import json


def load_candidates_from_json(path):
    with open(path, 'r', encoding="utf-8") as file:
        content = file.read()
        global worker_list
        worker_list = json.loads(content)
    return worker_list


def get_candidate(candidate_id):
    for i in worker_list:
        if i['id'] == candidate_id:
            return i


def get_candidates_by_name(candidate_name):
    output = []
    for i in worker_list:
        if candidate_name.lower() in i['name'].lower():
            output.append(i)
    return output


def get_candidates_by_skill(skill_name):
    candidates_list = []
    for i in worker_list:
        if skill_name.lower() in i["skills"].lower().split(", "):
            candidates_list.append(i)
    return candidates_list


print(load_candidates_from_json('candidates.json'))
