from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
import numpy as np

# ���ز�����IMDB���ݼ�
num_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# ����������ضϵ�maxlen����
maxlen = 200
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# ����LSTMģ��
model = Sequential()
model.add(Embedding(input_dim=num_words, output_dim=128, input_length=maxlen))
model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# ѵ��ģ��
batch_size = 64
epochs = 5
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

# �ڲ�������������ģ��
score, accuracy = model.evaluate(x_test, y_test, batch_size=batch_size)
print(f'Test score: {score}')
print(f'Test accuracy: {accuracy}')

# ����ģ��
model.save('sentiment_analysis_model.h5')

# ����ģ��
loaded_model = load_model('sentiment_analysis_model.h5')

# ��֤���ص�ģ��
loaded_model.evaluate(x_test, y_test, batch_size=batch_size)

# Ԥ��ʾ��
index = np.random.randint(0, len(x_test))
predicted_sentiment = model.predict(np.array([x_test[index]]))
predicted_label = 'positive' if predicted_sentiment[0][0] > 0.5 else 'negative'
print(f'Review: {" ".join([str(word) for word in x_test[index]])}')
print(f'Predicted sentiment: {predicted_label}, Actual sentiment: {"positive" if y_test[index] == 1 else "negative"}')

