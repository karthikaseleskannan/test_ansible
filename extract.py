#!/usr/bin/env python3
import yaml

# Open yaml file
with open('output/shoot_complete.yaml') as shoot:
# Read the yaml file and assign it to an list    
    clusters = yaml.load_all(shoot, Loader=yaml.FullLoader)
# Fetch the necessary value from the list using for loop
    for cluster in clusters:
        
        for key, value in cluster.items():
            if key == 'spec':
                print("region: "+value["region"])
            elif key == 'metadata':
                print("project: "+value["namespace"].replace("garden-", ""))
                print("name: "+value["name"])
            elif key == 'status':
                print("technicalID: "+value["technicalID"])




