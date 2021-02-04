from flask import Flask, render_template , request, redirect
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix, vstack
from lightfm import LightFM
from lightfm.data import Dataset

app = Flask(__name__)

plays = pd.read_csv('lastfm/user_artists.dat', sep='\t')
artists = pd.read_csv('lastfm/artists.dat', sep='\t', usecols=['id','name'])


# Merge artist and user pref data
ap = pd.merge(artists, plays, how="inner", left_on="id", right_on="artistID")
ap = ap.rename(columns={"weight": "playCount"})

# Group artist by name
artist_rank = ap.groupby(['name']) \
    .agg({'userID' : 'count', 'playCount' : 'sum'}) \
    .rename(columns={"userID" : 'totalUsers', "playCount" : "totalPlays"}) \
    .sort_values(['totalPlays'], ascending=False)

artist_rank['avgPlays'] = artist_rank['totalPlays'] / artist_rank['totalUsers']
# Merge into ap matrix
ap = ap.join(artist_rank, on="name", how="inner") \
    .sort_values(['playCount'], ascending=False)

# Preprocessing
pc = ap.playCount
play_count_scaled = (pc - pc.min()) / (pc.max() - pc.min())
ap = ap.assign(playCountScaled=play_count_scaled)

# Build a user-artist rating matrix
ratings_df = ap.pivot(index='userID',
                      columns='artistID',
                      values='playCountScaled')
ratings = ratings_df.fillna(0).values

# Build a sparse matrix
X = csr_matrix(ratings)

n_users, n_items = ratings_df.shape
user_ids = ratings_df.index.values
artist_names = ap.sort_values("artistID")["name"].unique()

# BEST hyperparameters
loss = 'warp'
learning_rate = 0.06
n = 8
k = 8

# classifier instance with BEST hyperparameters
clf = LightFM(loss=loss, learning_rate=learning_rate, n=n, k=k)

##########
listed = tuple(artists['name'])[:50]
#############################################################################################

@app.route('/')
def index():
    print(artists)
    
    return render_template('index.html', artists = listed)

@app.route('/results/', methods = ["POST"])
def result():
    if request.method == 'POST':
        selected_artists = request.form.getlist('selection')
        new_user = np.zeros(X.shape[1])
        for artist in selected_artists:
            index = list(artists.name).index(artist)
            new_user[index] = X[:, index].mean()
        X_new = vstack([X, new_user])
        new_user_id = X_new.shape[0] - 1
        clf.fit(X_new, epochs=10, num_threads=2)
        pred = clf.predict(new_user_id, np.arange(n_items))
        recommendations = artist_names[np.argsort(-pred)][:10]
    return render_template('result.html',
                           selection=selected_artists,
                           recommendations=recommendations,)
   