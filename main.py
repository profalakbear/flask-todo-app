from todo import create_app
import os

if __name__ == '__main__':
    app = create_app() 
    #app.run(debug=True)
    app.run(host='0.0.0.0')