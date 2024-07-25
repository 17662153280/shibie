from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
import numpy as np

# 下载并加载IMDB数据集
num_words = 10000
(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=num_words)

# 将评论填充或截断到maxlen长度
maxlen = 200
x_train = pad_sequences(x_train, maxlen=maxlen)
x_test = pad_sequences(x_test, maxlen=maxlen)

# 构建LSTM模型
model = Sequential()
model.add(Embedding(input_dim=num_words, output_dim=128, input_length=maxlen))
model.add(LSTM(units=128, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(units=1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# 训练模型
batch_size = 64
epochs = 5
history = model.fit(x_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

# 在测试数据上评估模型
score, accuracy = model.evaluate(x_test, y_test, batch_size=batch_size)
print(f'Test score: {score}')
print(f'Test accuracy: {accuracy}')

# 保存模型
model.save('sentiment_analysis_model.h5')

# 加载模型
loaded_model = load_model('sentiment_analysis_model.h5')

# 验证加载的模型
loaded_model.evaluate(x_test, y_test, batch_size=batch_size)

# 预测示例
index = np.random.randint(0, len(x_test))
predicted_sentiment = model.predict(np.array([x_test[index]]))
predicted_label = 'positive' if predicted_sentiment[0][0] > 0.5 else 'negative'
print(f'Review: {" ".join([str(word) for word in x_test[index]])}')
print(f'Predicted sentiment: {predicted_label}, Actual sentiment: {"positive" if y_test[index] == 1 else "negative"}')

