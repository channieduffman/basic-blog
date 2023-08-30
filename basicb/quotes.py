from flask import (
    Blueprint, render_template, request
)

import time

# For use in accessing https:// API route
import urllib.request, json
import ssl

from basicb.auth import login_required

bp = Blueprint('quotes', __name__)


def get_quotes():
    # Fetch the ZenQuotes API
    url = "https://zenquotes.io/api/quotes"
    context = ssl._create_unverified_context() # quick fix

    response = urllib.request.urlopen(url, context=context)
    data = response.read()
    quotes = json.loads(data)

    curr_t = time.ctime()

    return quotes, curr_t


@bp.route('/quotes', methods=('GET',))
def quotes():

    quotes, curr_t = get_quotes()

    return render_template('quotes/index.html', quotes=quotes, curr_t=curr_t)