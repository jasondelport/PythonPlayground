# PythonPlayground    

Python learning playground    

check version (you can have both python 2 and python 3 installed on same machine)    
* python --version
* python3 --version

install     
* brew install python3    

update    
* brew update     
* brew upgrade python3 
* brew cleanup python3          
  
run script    
* python3 src/main.py hello world     

pip3    
* pip3 --version    
* pip3 list
* pip3 freeze > requirements.txt (saves installed libs to requirements.txt file)      
* pip3 install -r requirements.txt          
* pip3 install package_name      
* pip3 install package_name --upgrade    
* pip3 show package_name 
* pip3 search <search_term>
* python3 -m pip install --upgrade pip    

run a server in a local mac directory     
* python3 -m http.server     

flask    
* mkdir webserver    
* cd webserver      
* python3 -m venv venv // lightweight “virtual environments”     
* . venv/bin/activate    
* export FLASK_ENV=development     
* export FLASK_APP=hello // if file named hello.py    
* // As a shortcut, if the file is named app.py or wsgi.py, you don’t have to set the FLASK_APP environment variable.    
* flask run    

https://docs.python-guide.org/intro/learning/         
https://book.pythontips.com/en/latest/args_and_kwargs.html       
https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/    

https://stackabuse.com/introduction-to-pythons-collections-module/    