#!/usr/bin/env python3
import yaml
from ecies import encrypt

publickey = str()

# Optain the publickey via https://ecies.sapcic.io
#Use this publickey to encrypt data
# Open the publickey and fetch the publickey
with open('publickey.txt') as public_key:
    pub_keys = public_key.readlines()
    for pub_key in pub_keys:
        p_key=(pub_key.split(':'))
        publickey=(p_key[1].strip())
        print (publickey)

# Open yaml file
with open('output/kube.yaml', 'rU') as kubecontent:
    data = yaml.safe_load(kubecontent)

    userdata = data['users']
    for user in userdata:
        cluster_token = user['user']['token']

        # Encrypt the token with ecies encryption (https://github.com/ecies/py)
        encrypted_data = encrypt(publickey, cluster_token.encode("utf8"))

        # Replace the kubeconfig token with encrypted token
        cluster_token= "ecies:"+ encrypted_data.hex()

        user['user']['token'] = cluster_token
        print (cluster_token)
        
#write the encrypted data 
with open('output/testrepo1/core/dev/kubeconfig.yaml', 'w') as kubeout:
    yaml.dump(data, kubeout)













        


                


                    

            