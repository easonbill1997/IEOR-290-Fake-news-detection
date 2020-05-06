#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  4 02:46:06 2020

@author: byc
"""


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dat = pd.read_csv("/Users/byc/Desktop/train.csv")


from tensorflow.keras import models, layers
from tensorflow.keras.optimizers import RMSprop,Adam
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape = (512,)))
model.add(layers.Dense(64,activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))
opt = RMSprop(lr=0.001, decay=1e-5)
model.compile(loss='binary_crossentropy', optimizer=opt, metrics=['acc'])

model.summary()




train_new = dat
y = train_new.label
embed = np.load("/Users/byc/Desktop/embed.npy", allow_pickle=True)
train_new.embed = embed
x = np.array(train_new.embed)
d = {'barely-true':1, 'false':0, 'mostly-true':1,'pants-fire':0,'true':1, 'half-true':1}
y_binary = [float(d[_]) for _ in y]
from sklearn import linear_model
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
x_train = [_.reshape(512) for _ in x_train]
x_test = [_.reshape(512) for _ in x_test]
x_train_bin, x_test_bin, y_train_bin, y_test_bin = train_test_split(x, y_binary, test_size=0.2, random_state=100)
x_train_bin = np.array([_.reshape(512) for _ in x_train_bin])
x_test_bin = [_.reshape(512) for _ in x_test_bin]
y_train_bin = np.array(y_train_bin).reshape(-1,1)

hist = model.fit(x_train_bin.reshape(8192,512,), y_train_bin, batch_size=128, epochs=100, validation_split=0.2)


plt.style.use('ggplot')
plt.plot(hist.history['acc'])
plt.plot(hist.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()