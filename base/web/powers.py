from flask import Flask

app=Flask(__name__)

@app.route('/')
def powers(n=10):
    return ','.join(str(2 ** i) for i in range(n))

if __name__ == '__main__':
    app.run()
