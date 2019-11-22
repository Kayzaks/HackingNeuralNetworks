import numpy as np

# We generate simple commands:
# 
# Call home         --->  ping 192.168.0.4
# Show me the money --->  nc -v 192.168.0.2 4444
# Let's go!         --->  echo 1 > /proc/sys/net/ipv4/ip_forward
# Stop annoying me  --->  kill 2222
#
# --------------------------------------------------------------
# Train this with
#
# batch_size = 4  
# epochs = 10  
# latent_dim = 256  
#
# Training should only take one or two minutes on a 1060 GTX

total_size = 1000

output_string = ""
out_texts = []


for i in range(total_size):

    # We use "tab" as the "start sequence" character
    # for the targets, and "\n" as "end sequence" character.
    if i % 7 == 0:
        out_texts.append('Call home\tping 192.168.0.4\n')
    elif i % 7 == 1:
        out_texts.append('Show me the money\tnc -v 192.168.0.2 4444\n')
    elif i % 7 == 2:
        out_texts.append("Let's go!\techo 1 > /proc/sys/net/ipv4/ip_forward\n")
    elif i % 7 == 3:
        out_texts.append('Stop annoying me\tkill 2222\n')
    elif i % 7 == 4:
        out_texts.append('Stop\tkill\n')
    elif i % 7 == 5:
        out_texts.append('Show me\tnc -v\n')
    elif i % 7 == 6:
        out_texts.append('Call\tping\n')

with open('./solution_data.txt', 'w') as f:
    for item in out_texts:
        f.write(item)