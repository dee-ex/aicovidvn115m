# AICovidVN115m - Top 3 solution on the final round (AUC 0.92)

The competition "[AICV-115M Challenge](https://aihub.vn/competitions/22#learn_the_details)" is a Covid-19 couch detect contest attracting 168 competitors.
We, team `đi thi` finished at **Top 3** to the AUC score around **0.92** (precisely 0.921527). Subsequently, we intend to share our whole solution working on the competition. The reporting materials can be found at `reports/`.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/reports/score.jpg" width="1000"></p>
<p align="center"><i>Figure 1. Our best score (AUC 0.921527)</i></p>
<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/reports/ranking.jpg" width="1000"></p>
<p align="center"><i>Figure 2. The final standings (our result was just 0.01 less the winner and runner-up team)</i></p>

## Table of contents
* [1. Development environment and libraries](#1-development-environment-and-libraries)
* [2. The structures of the repository](#2-the-structures-of-the-repository)
* [3. Training and prediction](#3-training-and-prediction)
    * [3.1 Training](#31-training)
    * [3.2 Prediction](#32-prediction)
* [4. For tesing with your own audio](#4-for-tesing-with-your-own-audio)
* [5. API](#5-api)
* [6. Frontend](#6-frontend)
* [7. Acknowledge](#7-acknowledge)
* [8. Dataset license](#8-dataset-license)
* [9. License](#9-license)

## 1. Development environment and libraries

Environment needed is Python 3.X (https://www.python.org/) or just using Google colab (https://colab.research.google.com/).

List of necessary stored in `requirements.txt`. For installing, open commandline (Command Prompt, Terminal, ...) and type the following codes (if using Google colab, skip this step):
```
pip install -r requirements.txt
```

For personal local environment, we suggest creating a virtual environment to avoid unwanted conflicts (https://docs.python.org/3/tutorial/venv.html).

After installing the libraries listed in `requirements.txt`, the API is ready for use.  
For using frontend, the Node.js (https://nodejs.org/en/download/) need setting up. Then, install vue-cli to compiling the host:
```
npm i
```

## 2. The structures of the repository

```
aicovidvn115m
│   LICENSE
|   main.py
│   README.md
│   requirements.txt
|   submission.ipynb
│
└───data/ - dataset and its information
│   │   extra/ - 20 audio files collected from aicv115m_extra_public_1235samples provided by the organizers
│   |   private/ - 1627 testing audio files
|   |   private_features/ - features extracted from private/
|   |   train/ - 4505 raw training audio files
|   |   train_features/ - features extracted fromtrain/
|   |   ...
└───modules/ - source codes for developing the model
|   |   __init__.py
│   │   ...
│
└───report/ - solution report, slides and related images
|   |   report.pdf
|   |   ranking.jpg
│   │   ...
│
└───src/ - source codes of api backend and frontend
│   └───backend/
|   |   |   manage.py - executive file to build backend
│   |   frontend/
└───weights/ - trained models
│   │   modles/ - 100 trained models
│   │   scalers/ - 4 scaler using for scale the features
│
```

## 3. Training and prediction

### 3.1 Training

In order to train the model, go inside directory `modules` and type:
```
python train.py
```

P/s: when training, the new trained models are also stored in `weigths/models/`. The directory for storing new trained models should be modified if needed.

### 3.2 Prediction

Inside directory `modules`:
```
python predict.py
```

Prediction result saved in `modules/results.csv`.

## 4. For tesing with your own audio

By default, our model is used for predicting `main.py`.
```
python main.py -f audio_file_name
```

`audio_file_name` file name or a directory to an audio file. File required format is `.wav`.

## 5. API

We developed a simple API with Django. In order to build the host server run the following codes inside `src/backend/`:
```
python manage.py runserver
```

Default host built at IP loopback `127.0.0.1`, port `8000` (http://127.0.0.1.8000/). As usual, the loopback should be `localhost`, so the IP address can be replaced by `localhost`.  
Endpoint to use API is set up at  `api/predict/` with method POST. Simply, we did not take care of security as CSRF, CORS. The audio file is sent by form with the name `"audio"`. The result saved in JSON file:
```json
{
    "prob": 0.123456789
}
```

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/reports/api.jpg" width="1000"></p>
<p align="center"><i>Figure 3. API tesing using Postman</i></p>

## 6. Frontend

For getting started, make sure to have API host server (previous step).  
Then, start frontend by run the below codes in directory `src/frontend/`:
```
npm run serve
```

The default host address at http://localhost:8080/.  
The API address where frontend set up is the same as API. If changing the API address, it has to be synced with frontend address in `src/frontend/src/App.vue`, line 74.  

The executing time is around 15s for mid-level hardware.

<p align="center"><img src="https://raw.githubusercontent.com/dee-ex/aicovidvn115m/main/reports/frontend.jpg" width="1000"></p>
<p align="center"><i>Figure 4. Frontend experience</i></p>

The result is highlighted by color scale from red to green (red: at high risk, green: safe).

## 7. Acknowledge

We'd like to give many thank you to the organizers of AICovidVN 115 Challenge. This competition help students like us contribute our little things to public community and gain lots of valuable experience.
The pure goal of competition is to develop a solution supporting community to fight against Covid-19, we sincerely have a chance to contribute our solution to the community.

## 8. Dataset license

The dataset in  `data/` owned by "[AICV-115M Challenge](https://aihub.vn/competitions/22#learn_the_details)", for more details, [Terms and Conditions](https://aihub.vn/competitions/22#learn_the_details-terms_and_conditions).

## 9. License

[MIT](https://github.com/dee-ex/aicovidvn115m/blob/main/LICENSE).
