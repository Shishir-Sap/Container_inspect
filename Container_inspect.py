import json
f = open('container_inspect.json',"r")
input_file=(f.read())
# print(input_file)
docker_dict2 = json.loads(input_file)
print(docker_dict2[0].keys())
print("-----------Antwoord--------------")
print(docker_dict2[0]["Config"]["Hostname"])
print(docker_dict2[0]["NetworkSettings"]["Networks"]["bridge"]["IPAddress"])
print(docker_dict2[0]["NetworkSettings"]["Ports"])
print(docker_dict2[0]["State"]["Status"])
