import tensorflow as tf
import sklearn.model_selection
import numpy  as np 
import pandas as pd

from tensorflow.keras.preprocessing.text import  Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences



class toxicCommentClassifier():
    def __init__(self):
        self.vocab_size =  21000
        self.max_len = 100
        self.embedding_dim = 300
        self.comments = []
        self.toxic = []
    
    def read_data(self, datapath):
        self.data = pd.read_csv(datapath)
        return self.data

    def pick_category(self, category = 'asian'):
        # TODO: pick different categories from input() and analyze different minorities
        self.data_per_category =  [['id', 'comment_text', 'target', 'asian']]
        self.data_per_category = data[data.asian>0.0] #10975
        # self.data_per_category = data.asian[data.category>0.0] #10975
        self.data_per_category.loc[(self.data_per_category.target > 0.1), 'target'] = 1
        self.data_per_category.loc[(self.data_per_category.target <= 0.1), 'target'] = 0
        # print(self.data_per_category.target.value_counts())


    def pre_process(self):
        self.comments = list(self.data_per_category.comment_text)
        self.toxic = list(self.data_per_category.target)
# build  tokenizer 
        tokenizer = Tokenizer(num_words  = self.vocab_size, oov_token =  "<OOV>")
        tokenizer.fit_on_texts(self.comments)

        word_index  =  tokenizer.word_index
        # create squence of tokens
        sequences = tokenizer.texts_to_sequences( self.comments)
        # padd the smaller comments
        self.padded = pad_sequences(sequences, padding = 'post' , maxlen = self.max_len)
        self.toxic = np.array(self.toxic)

    def train_test(self):
        self.train_x, self.test_x, self.train_y, self.test_y = sklearn.model_selection.train_test_split(
            self.padded, self.toxic, test_size =0.2, random_state=42
        )


    def model(self):
        self.model = tf.keras.Sequential([
            tf.keras.layers.Embedding(self.vocab_size, self.embedding_dim, input_length = self.max_len),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(units= 32, activation='relu' ),
            tf.keras.layers.Dense(units= 1, activation='sigmoid' )
        ])
        self.model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
        print(self.model.summary())
    
    def train(self):

        self.model.fit(self.train_x, self.train_y, epochs=10, batch_size=32, validation_data=(self.test_x, self.test_y))
        
if __name__ == "__main__":


    # file_path = 'train.csv'
    file_path = 'train_toxic.csv'

    model =  toxicCommentClassifier()

    data = model.read_data(file_path)
    model.pick_category()
    # data =  data[:100]

    model.pre_process()
    model.model()
    model.train_test()
    model.train()

    # print(len(data)) #1804874
    # print(type(data))
    # print(data.columns) #['id', 'target', 'comment_text', 'severe_toxicity', 'obscene',
        #    'identity_attack', 'insult', 'threat', 'asian', 'atheist', 'bisexual',
        #    'black', 'buddhist', 'christian', 'female', 'heterosexual', 'hindu',
        #    'homosexual_gay_or_lesbian', 'intellectual_or_learning_disability',
        #    'jewish', 'latino', 'male', 'muslim', 'other_disability',
        #    'other_gender', 'other_race_or_ethnicity', 'other_religion',
        #    'other_sexual_orientation', 'physical_disability',
        #    'psychiatric_or_mental_illness', 'transgender', 'white', 'created_date',
        #    'publication_id', 'parent_id', 'article_id', 'rating', 'funny', 'wow',
        #    'sad', 'likes', 'disagree', 'sexual_explicit',
        #    'identity_annotator_count', 'toxicity_annotator_count']

    # print(data.asian.value_counts())
    asian = data.asian[data.asian>0.0] #10975
    # y = data.asian[data.asian<=0.1]
    print(len(asian))
    # print(len(y))

    # print(f" toxic label dist : {data.target.value_counts()}")
    # 0    144277
    # 1     15294

    # print(f"max length of the comments {max(list(data.comment_text))}")

    # print(f" severe toxic dist on labels: {data.severe_toxic.value_counts()}")
    # 0    157976
    # 1      1595

    # print(model.pre_process())

    # print(data.identity_hate.value_counts())
