import uvicorn  # pragma: no cover


def run():  # pragma: no cover
    uvicorn.run("app:app", host="0.0.0.0", log_level="info", reload=True)


if __name__ == "__main__":  # pragma: no cover
    run()
