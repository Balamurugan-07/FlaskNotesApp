from website import create_app

app = create_app()

# execute the command only if main.py is running. 
# This avoids when main.py is imported instead of running it
if __name__ == "__main__": 
  app.run(debug=True) # auto run when change is saved. False in production
