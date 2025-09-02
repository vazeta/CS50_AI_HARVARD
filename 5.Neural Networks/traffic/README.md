# Experiments with Traffic Sign Classification Model - CS50

For this project, I experimented with different neural network architectures to classify traffic sign images into NUM_CATEGORIES categories.

My first attempt was a very simple network with a single convolutional layer (32 filters) , flattening, and a dense output layer. While this network was fast to train, it quickly overfit to the training data and achieved poor generalization on the test set.

I then added a second convolutional + pooling layer, which allowed the network to learn more complex features. I also introduced a hidden dense layer with 128 neurons and used ReLU activation to improve non-linearity. Finally, I applied a dropout layer with a rate of 0.5 to reduce overfitting.

This final model achieved a significantly better accuracy on the validation set while still training relatively quickly. achieved 98.11% accuracy

## what i Learned

- Adding more convolutional layers improves feature extraction, but too many layers can overfit given a small dataset.
- Dropout wass essential to reduce overfitting.
