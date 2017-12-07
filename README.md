THE APPLICATION CAN ALSO BE FOUND ONLINE: http://markibolya7.pythonanywhere.com/

Follow these steps to run the application using Docker:

1. git clone https://github.com/MarkIbolya7/VacationManagement.git
2. open the VacationManagement folder - cd VacationManagement
3. sudo docker build -t vacation-management:latest .
4. docker run -d -p 5000:5000 vacation-management
5. Open your browser and go to link: http://localhost:5000/
6. A Google login screen will welcome you, and after logging in you will receive Administrator access
7. The Admin panel can be found here: http://localhost:5000/admin

About the application:

You can find the application here: http://localhost:5000/ or http://markibolya7.pythonanywhere.com/
First user to log in with his/her Google Account will receive Admin access
All other users will receive "pending" access, which means it can't access anything till an Admin approved his/her account
From the admin panel (http://localhost:5000/admin or http://markibolya7.pythonanywhere.com/admin) any admin can change other users group and approve/decline or put back a vacation request to pending.
Approved users (except viewers) can request vacation from the front page.