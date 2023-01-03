import boto3
import json

# Let's use Amazon S3
# s3 = boto3.resource('s3')
# # Print out bucket names
# for bucket in s3.buckets.all():
#     print(bucket.name)
def ec2():
  client = boto3.client('ec2')
  res = client.describe_instances()
  # print(res)
  # print(res["Reservations"][0]["Instances"][0])
  ret = []
  for j in res["Reservations"]:
    for i in j["Instances"]:
      o = {}
      state = i["State"]["Name"]
      id = i["InstanceId"]
      name = i["Tags"][0]["Value"]
      o["name"] = name
      o["id"] = id
      o["state"] = state
      ret.append(o)
      # print("AWS EC2 Name:{0}, ID: {1}, State: {2} ".format(name, id, state))
  return ret

  
def print_ec2(ret):
  # print("ret:",ret)
  stopped=list(filter(lambda x: x["state"] == "stopped",ret))
  running=list(filter(lambda x: x["state"] == "running",ret))

  print("App Running:")
  print("")
  print("#################")
  print("Running instances:")
  for i in running:
    print(i)

  print("#################")
  print("Stopped instances:")
  for i in stopped:
    print(i)

# ec2()