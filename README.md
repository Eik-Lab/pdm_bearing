# PDM bearing

A manual for getting started with Predicative maintanance with machine learning and streamlit

## Structure
The project contains several parts, and can be divided into the following parts:

The machine learning scripts. These are:  
- `keras_example.py`
- `knn_example.py`

Then there are the scripts for reading,and processing data, those are:
- `read_data.py`
- `transform_data.py`

And at last, there is the streamlit scripts, which can be found in the `bearing_app` folder.


[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/eik-lab/pdm_bearing/streamlit_cloud/bearing_app/main.py)
## Run Locally
### Requirements

Python 3.6 or newer
### Setting up the project locally
Clone the project

```bash
  git clone https://github.com/Eik-Lab/pdm_bearing.git
```

Go to the project directory

```bash
  cd pdm_bearing
```

Install dependencies

```
pip install -r requirements.txt
```

To run the script you want, the command is:
```bash 
python $script_name$.py
```

To run the streamlit app, the command is:
```bash
streamlit run bearing_app/main.py
```


## Tech Stack

Python, and streamlit
