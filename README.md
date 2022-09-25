# Reverse Image Search
<div style="text-align:center"><img src="static/Logo.png" /></div>

>Please note that this is my first project :sunglasses:

## Video Demo: https://youtu.be/YXrxTnmEFjo

## Requirements:
```Flask
Flask_Dropzone
imgbbpy
Werkzeug
```
Install it by cloning this `repo` then run:  
```
 pip install -r /path/to/requirements.txt 
 ```

## Using `imgbbpy`
In this project I have used `imgbbpy` for generating url of uploaded image which is stored in `uploads` folder.
To use this, go [Imgbb](https://api.imgbb.com/) then `Get API key` and paste it the given field in `helpers.py`.
```Python
def get_link(file_location):
        try:
                client = imgbbpy.SyncClient('[Paste your API Key here]')
                image = client.upload(file = f'{file_location}')
                return image.url
        except:
                return render_template('error.html', message="Invalid File")
```
## Using `Flask-Dropzone`
Take a look [here](https://github.com/greyli/flask-dropzone) to get the documentation of `Flask-Dropzone`. I have implemented it just like the `complete-redirect` example given there.


## Pseudocode
### Route 1: File uploaded by dropzone  
1) File is uploaded by user -> function `uploads()` stores it in uploads folder -> Redirected to `fetch()`
2) A url is generated using `imgbb`
3) Then page is redirected to `https://www.google.com/searchbyimage?image_url={url}` to search for image in the url.    
   
### Route 2: URL entered by user  
Since we now directly have the url, we can directly redirected to `https://www.google.com/searchbyimage?image_url={url}` to search for image in the url.

## `helpers.py`
It consist of `get_link` and `get_result` functions:

### `get_link`
```Python
def get_link(file_location):
        try:
                client = imgbbpy.SyncClient('[Paste your API Key here]')
                image = client.upload(file = f'{file_location}')
                return image.url
        except:
                return render_template('error.html', message="Invalid File")
```
It takes file location (path in which file is stored) as argument and returns its url using the `imgbbpy` library.


### `get_result`
```Python
def get_result(url):
    location = url
    url = get_link(location)
    return redirect(f"https://www.google.com/searchbyimage?image_url={url}")
```
It uses `get_link` function to generate url. The url is then used to get result by url.

## Bootstrap implementation
Read the documentation [here](https://getbootstrap.com/docs/5.1/getting-started/introduction/)
This framework is used for the form field in `index.html` as well as for the text field in `instructions.html`, `about.html` and `error.html`

## Flask-Dropzone configurations
```Python
app.config.update(    
    UPLOADED_PATH = os.path.join(basedir,'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE = 8,
    DROPZONE_MAX_FILES=1,
    DROPZONE_UPLOAD_MULTIPLE=False,
    DROPZONE_REDIRECT_VIEW='fetch'
)
```
`DROPZONE_ALLOWED_FILE_TYPE`: since we have to search for images only, Allowed filetype for upload is that of image only.  
`DROPZONE_MAX_FILE_SIZE`: Max file size is set to 8 MB.  
`DROPZONE_MAX_FILES`: At a time only one file is accepted in drop box.  
`DROPZONE_REDIRECT_VIEW`: after uploading file, /fetch route is redirected automatically.  

## `werkzeug.utils`'s `secure_filename`
On windows systems the function also makes sure that the file is not named after one of the special device files. Since we are using filename as na argument in functions of python, the user may tamper it by uploading a file named `../../../etc/passwd` for example, namely if the file is named as a directory of some important file stored in computer.  
This function changes the above mentioned filename to something like `etc_passwd`, which dosent represent any directory.


