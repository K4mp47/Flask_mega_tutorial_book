# Tutorial del libro flask mega tutorial by Miguel Grinberg

### Microblog
> dentro la cartella microblog troviamo il progetto microblog, per il momento fino al capitolo 2.
> Si possono vedere l'implementazione dei template all'interno della cartella template.
> Introduzione ai cicli e alle condizioni all'interno dei file flask.
> Struttura base di un progetto flask.
```
microblog/
    venv/
    app/
        __init__.py
        routes.py
        templates/
            base.html
            index.html
    microblog.py
```
> aggiunta del database, nuovi moduli installati per il login, la registrazione e l'intero
> reindirizzamento delle pagine web, aggiunte nuove pagine dinamiche in templates.
> Con queste ultime modifiche si conclude la prima parte, capitoli dall'uno al sei.
```
microblog/
    venv/
    __pycache__/
    app/
        __pycache__/
        __init__.py
        routes.py
        form.py
        models.py 
        templates/
            base.html
            index.html
            login.html
            register.html 
    migrations/
        __pycache/
        versions/
        alembic.ini 
        env.py 
        README
        script.py.mako 
    app.db
    config.py
    microblog.py
```
> Utilizzo principalmente di Wtform e SQLAlchemy per quanto riguarda autenticazione e database.
