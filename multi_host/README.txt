1. Introduction
1) app-server register their ip and port on dir-server by sending message. 
2) dir-server sends these servers ip and port to app-client. 
3) app-client then connects to the given available app-server. 
4) app-client sends 10KB data to each app-server and measures the time (performance)
5) app-client sends set-record message to db-server
6) db-server sends get-records message to app-client

2. Execution
Open 4 different terminals, run each file on each of them, in order:
1) %python dir-server.py <ds_port>
2) %python app-server.py <ds_port>
3) %./db-server.py <db_port>
4) %python app-client.py <ds_port> <db_port>

3. File hierarchy
multi-socket/
    README.txt    
    app-server/
        app-server.py
    app-client/
        app-client.py
    dir-server/
	dir-server.py


