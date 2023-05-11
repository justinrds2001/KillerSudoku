# save the final model to file
import tensorflow as tf
from tensorflow import keras
 
# load train and test dataset
def load_dataset():
 # load dataset
 (trainX, trainY), (testX, testY) =  keras.datasets.mnist.load_data()
 # reshape dataset to have a single channel
 trainX = trainX.reshape((trainX.shape[0], 28, 28, 1))
 testX = testX.reshape((testX.shape[0], 28, 28, 1))
 # one hot encode target values
 trainY = keras.utils.to_categorical(trainY)
 testY = keras.utils.to_categorical(testY)
 return trainX, trainY, testX, testY
 
# scale pixels
def prep_pixels(train, test):
 # convert from integers to floats
 train_norm = train.astype('float32')
 test_norm = test.astype('float32')
 # normalize to range 0-1
 train_norm = train_norm / 255.0
 test_norm = test_norm / 255.0
 # return normalized images
 return train_norm, test_norm
 
# define cnn model
def define_model():
 model = keras.models.Sequential()
 model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', kernel_initializer='he_uniform', input_shape=(28, 28, 1)))
 model.add(keras.layers.MaxPooling2D((2, 2)))
 model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
 model.add(keras.layers.Conv2D(64, (3, 3), activation='relu', kernel_initializer='he_uniform'))
 model.add(keras.layers.MaxPooling2D((2, 2)))
 model.add(keras.layers.Flatten())
 model.add(keras.layers.Dense(100, activation='relu', kernel_initializer='he_uniform'))
 model.add(keras.layers.Dense(10, activation='softmax'))
 # compile model
 opt = keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)
 model.compile(optimizer=opt, loss='categorical_crossentropy', metrics=['accuracy'])
 return model
 
# run the test harness for evaluating a model
def run_test_harness():
 # load dataset
 trainX, trainY, testX, testY = load_dataset()
 # prepare pixel data
 trainX, testX = prep_pixels(trainX, testX)
 # define model
 model = define_model()
 # fit model
 model.fit(trainX, trainY, epochs=3, batch_size=32, verbose=0)
 # save model
 model.save('final_model3epochs.h5')
 
# entry point, run the test harness
run_test_harness()