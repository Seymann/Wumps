curl -d "type=newgame&game=Test" http://127.0.0.1:5000
curl -d "type=addName&game=Test&name=Bob" http://127.0.0.1:5000
curl -d "type=addName&game=Test&name=Bobby" http://127.0.0.1:5000
curl -d "type=addName&game=Test&name=BobbyBoi" http://127.0.0.1:5000
curl -d "type=taketurn&game=Test&name=Bobby&turn=0" http://127.0.0.1:5000
curl -d "type=taketurn&game=Test&name=BobbyBoi&turn=1" http://127.0.0.1:5000
curl -d "type=taketurn&game=Test&name=Bob&turn=1" http://127.0.0.1:5000