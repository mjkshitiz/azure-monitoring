from flask import flash, render_template, redirect, request
from FlaskExercise import app


@app.route('/')
def home():
    log = request.values.get('log_button')
    if log:
        if log == 'info':
            app.logger.info('No Issue')
        elif log == 'warning':
            app.logger.warning('Warning occured.')
        elif log == 'error':
            app.logger.error('Error!!!!!')
        elif log == 'critical':
            app.logger.critical('Criticial error!!!!!!!')
    return render_template(
        'index.html',
        log=log
    )
