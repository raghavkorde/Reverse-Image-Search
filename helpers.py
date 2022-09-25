import imgbbpy
from flask import redirect
from flask import render_template


def get_link(file_location):
        try:
                client = imgbbpy.SyncClient('[Paste your API Key here]')
                image = client.upload(file = f'{file_location}')
                return image.url
        except:
                return render_template('error.html', message="Invalid File")

        
        



def get_result(path):
    location = path
    url = get_link(location)
    return redirect(f"https://www.google.com/searchbyimage?image_url={url}")