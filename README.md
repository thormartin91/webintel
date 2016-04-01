# WebIntel

## Setup
###Requirements:

- Python (>= 2.6 or >= 3.3)

###Procedure:
- Clone repo
- Create virtual environment: `virtualenv env`, `source env/bin/activate`
- Install requirements: `pip install -r requirements.txt`

## Data sources
_Available in **/data**_

### u.data
```
user_id | item_id | rating | timestamp
```

### u.item
```
movie id | movie title | release date | video release date | IMDb URL | 19 x genre |
```

_Smaller datasets are available in **/sample**_