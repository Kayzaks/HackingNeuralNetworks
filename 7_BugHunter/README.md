# Exercise 7-0 

You are tired of doing bug hunting by hand and static code analysis doesn't seem to be working as you intended. Instead, you decide to use a neural network to search for vulnerabilities!

You have already done the first step and created a training set of (code, vulnerable?) pairs in the 'train.txt' file. Now its time to train a model to get the AI working! You decide to use convolution and find that the code in 'train.py' seems to be a good starting point.

- Train a model on the data provided in 'train.txt', such as the one found in 'train.py', to find vulnerable code. (You can use any other model if you so please)
- 'exercise.py' contains some further code you found that seems helpful.
- Test your model on the following source code you found to see if it finds the vulnerable 'printf' statement.
- *The emphasize of this exercise lies in pre-processing the data! Don't worry about the training process that much, such as overfitting.*


```
printf("Hey %s, how are you?", name);
printf("Doing fine...");
printf(status);
printf("What about you?");
printf("");
```


A solution can be found in 'solution_7_0.py'