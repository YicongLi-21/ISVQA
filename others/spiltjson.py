import numpy as np
import json
from sklearn.model_selection import train_test_split
# from sklearn.utils import shuffle


path = './imdb_nuscenes_trainval_score_id.json'
file = json.load(open(path))['data']
y = np.arange(len(file))
X_train, X_test, y_train, y_test = train_test_split(file, y, test_size=0.2, random_state=1, shuffle=True)

X_train_new = './input/imdb_nuscenes_spilt2_train_score_id.json'
X_test_new = './input/imdb_nuscenes_spilt2_test_score_id.json'
y_train_new = './train_id2.txt'
y_test_new = './test_id2.txt'

with open(X_train_new, 'w') as f:
    json.dump(X_train, f)

with open(X_test_new, 'w') as f:
    json.dump(X_test, f)

np.savetxt(y_train_new, y_train)

np.savetxt(y_test_new, y_test)