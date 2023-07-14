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
> Alla fine sono arrivato al capitolo 12, concludendo cosí la struttura principale del progetto all'interno del libro.
> I capitoli successivi si concentrano sopratutto su cose che ancora non sono in grado di utilizzare in maniera utile, come il deployment.
> Ora come ora sono soddisfatto del risultato, essendo che l'intero progetto é funzionante!

#### Conclusione

>Questa é la struttura finale del progetto:
```
microblog/
    venv/
    __pycache__/
    app/
        __pycache__/
        __init__.py
        routes.py
        form.py
        errors.py
        models.py 
        templates/
            404.html
            500.html
            _post.html
            edit_profile.html
            base.html
            index.html
            login.html
            user.html
            register.html 
    logs/
        // various log report files
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
>ho aggiunto anche il file requirements.txt, anche se in teoria non sarebbe necessario includere tutto quello che presenta al suo interno
