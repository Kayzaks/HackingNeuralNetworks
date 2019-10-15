# Exercise 0-0

Just by looking at the 'model.h5' file and some googling, try to deduce what the model is doing. 

**What does the Architecture look like?** 
 - [ ] Conv -- Conv -- MaxPool -- Conv -- MaxPool -- Dense -- Dense
 - [ ] Conv -- Conv -- Conv -- Conv -- Dense -- Dense
 - [ ] Conv -- Conv -- MaxPool -- Conv -- Conv -- Dense -- Dense
 - [ ] Conv -- Conv -- MaxPool -- Dense -- Dense
 - [ ] Conv -- Dense -- Conv -- MaxPool -- Dense -- Dense -- Dense

**What was the model trained with?** 
 - [ ] Adam
 - [ ] SGD
 - [ ] RMSProp
 - [ ] Adadelta

**What is happening?**
 - [ ] Text Classification
 - [ ] Regression Analysis
 - [ ] Image Classification
 - [ ] Time Series Prediction
 - [ ] Language Translation


The solution can be found in 'solution_0_0.py'

(Wouldn't it be great to have a script that just tells us all this...)

# Exercise 0-1

The exercise takes as input handwritten digits ('0' to '9'). However, only one of these digits grants access, namely '4'. Our best attempts to fake this digit have failed. We have a fake digit, but its a '2'. Not all is lost though, as we have access to the 'model.h5'!

- Do not modify the 'exercise.py' or 'fake_id.png' (but you may look).
- You are only allowed to modify the 'model.h5' file.
- Modify 'model.h5' in such a way, that running 'exercise.py' accepts 'fake_id.png' for access.
- Your goal should be to modify as little as possible.

A solution can be found in 'solution_0_1.py'