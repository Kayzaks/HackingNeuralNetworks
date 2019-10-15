# Exercise 6-0  

You want to create persistency on a target machine by having a service run in the background. However, you know the network is monitored. Your goal is to train a recurrent neural network (Seq2Seq) to understand plain text commands and convert them into shell commands:

- Create training data and save them in the file 'solution_data.txt'
- Train the model by running 'train.py'
- Check that your model works by running 'exercise.py'
- Your model must be able to at least translate the following commands:

```
    Call home         --->  ping 192.168.0.4
    Show me the money --->  nc -v 192.168.0.2 4444
    Let's go!         --->  echo 1 > /proc/sys/net/ipv4/ip_forward
    Stop annoying me  --->  kill 2222
```

- You may modify all files to suit your training requirements, except the lower part of 'exercise.py' (it is marked)

*Some Tipps:*

- Play around with the batch_size and the epochs. 

    &rightarrow; Smaller batch_sizes usually lead to higher accuracy, but  slower training. Normally this can also lead to overfitting, but in our case that is fine/wanted.

    &rightarrow; More epochs lead to higher accuracy on the training set, but slower training and can lead to overfitting.
- If you change anything apart from batch_size and epochs in the training routine, remember to change 'test.py' in the same way.
- You can check out datasets that are actually used by Seq2Seq for inspiration (http://www.manythings.org/anki/)

A solution can be found in 'solution_6_0.py'