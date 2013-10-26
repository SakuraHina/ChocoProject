import web

urls = tuple()
app = web.application(urls, globals())


if __name__ == '__main__':
    app.run()