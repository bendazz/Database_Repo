# Database_Repo

This is a repo dedicated to building and learning about different aspects of databases.

## Using SQLModel with an existing SQLite DB

If you have an existing SQLite database (e.g., `baseball.db`) with tables created outside of SQLModel, you can still interact with it:

- Map a SQLModel class to the existing table using `table=True` and set `__tablename__` to match, e.g., `"people"`.
- Define only the columns you need. Extra columns in the table are fine for reads; for inserts/updates respect NOT NULL/defaults.
- Avoid calling `SQLModel.metadata.create_all(engine)` unless you intend to create missing tables.

See [app.py](app.py) for a minimal example that:
- Connects to `baseball.db`.
- Maps a `Person` model to the `people` table.
- Shows ORM querying and reflection-based querying with SQLAlchemy Core.

### Preventing circular imports

Avoid naming your Python files the same as libraries you import. For example, a file named `sqlmodel.py` will shadow the external `sqlmodel` package and cause a circular import error like:

```
ImportError: cannot import name 'Field' from partially initialized module 'sqlmodel' ... (most likely due to a circular import)
```

Use names like `sqlmodel_demo.py` or `app.py` instead.