import os
import random
from datetime import datetime, timezone
from pathlib import Path

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title='DevOps Playground')
templates = Jinja2Templates(directory=str(BASE_DIR / 'templates'))


def render_template(template_name: str, request: Request, **context) -> HTMLResponse:
    """Flask-like helper for rendering Jinja templates."""
    return templates.TemplateResponse(template_name, {'request': request, **context})


ENDPOINTS = [
    {
        'title': 'Health',
        'path': '/health',
        'pill': 'Health',
        'description': 'Simple readiness probe. Returns status JSON to feed liveness checks.',
        'cta': 'Open endpoint →',
    },
    {
        'title': 'Time',
        'path': '/time',
        'pill': 'Clock',
        'description': 'UTC timestamp both ISO8601 and epoch seconds.',
        'cta': 'Open endpoint →',
    },
    {
        'title': 'Random',
        'path': '/random?min=1&max=6',
        'pill': 'Random',
        'description': 'Returns a random integer within bounds. Handy for response variance.',
        'cta': 'Roll a die →',
    },
    {
        'title': 'Echo',
        'path': '/echo?message=ping',
        'pill': 'Echo',
        'description': 'Loop a message back for quick connectivity checks. Validates empty payloads.',
        'cta': 'Ping →',
    },
    {
        'title': 'Info',
        'path': '/info',
        'pill': 'Info',
        'description': 'Returns hostname, working directory, and selected environment flags.',
        'cta': 'Inspect →',
    },
]


@app.get('/', response_class=HTMLResponse)
def landing_page(request: Request):
    return render_template('index.html', request=request, endpoints=ENDPOINTS)


@app.get('/health')
def health():
    return {'status': 'ok'}


@app.get('/time')
def current_time():
    now = datetime.now(timezone.utc)
    return {'utc_iso': now.isoformat(), 'epoch_seconds': int(now.timestamp())}


@app.get('/random')
def random_number(minimum: int = Query(0, alias='min'), maximum: int = Query(100, alias='max')):
    if minimum >= maximum:
        raise HTTPException(status_code=400, detail='min must be less than max')
    return {'value': random.randint(minimum, maximum)}


@app.get('/echo')
def echo(message: str = Query(..., min_length=1, max_length=200)):
    return {'echo': message}


@app.get('/info')
def info():
    env_keys = ['ENV', 'STAGE', 'NODE_NAME']
    return {
        'hostname': os.getenv('HOSTNAME', 'unknown'),
        'working_dir': os.getcwd(),
        'env_example': {key: os.getenv(key) for key in env_keys if os.getenv(key)},
    }
