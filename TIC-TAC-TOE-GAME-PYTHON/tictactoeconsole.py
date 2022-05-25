import pyrebase
firebaseConfig = {
    'apiKey': "AIzaSyCmddj80nuQKHN1kMprSNhkfkMFCjO-5gM",
    'authDomain': "tictactoepython-97cdc.firebaseapp.com",
    'databaseURL': "https://tictactoepython-97cdc-default-rtdb.firebaseio.com/",
    'projectId': "tictactoepython-97cdc",
    'storageBucket': "tictactoepython-97cdc.appspot.com",
    'messagingSenderId': "767593943919",
    'appId': "1:767593943919:web:0b9f9e74d1eb4263a4ce9a"
}
firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
game_id = input("Please enter a unique 4-digit GAME ID to start playing: ")
print("OK, lets play!")
won = False
while won is False:
	print(f"""
		{one}   {two}   {three}
    	{four}   {five}   {six}
    	{seven}   {eight}   {nine}""")
	player = "player1"
	if player == "player1":
		print("Player 1 (X), your turn (use numbers): ")
		choice = input()
		if choice == "1":
			one = "X"
			data = {
			'1': one,
			'2': two,
			'3': three,
			'4': four,
			'5': five,
			'6': six,
			'7': seven,
			'8': eight,
			'9': nine,
			'player1': "X",
			'player2': "O"
		}	
			db.child(game_id).set(data)
		if choice == "2":
			two = "X"
			data = {
				'1': one,
				'2': two,
				'3': three,
				'4': four,
				'5': five,
				'6': six,
				'7': seven,
				'8': eight,
				'9': nine,
				'player1': "X",
				'player2': "O"
		}
db.child(game_id).set(data)
        if choice == "3":
            three = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "4":
            four = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "5":
            five = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "6":
            six = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "7":
            seven = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "8":
            eight = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O"
            }
            db.child(game_id).set(data)
        if choice == "9":
            nine = "X"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        player = "player2"
    if player == "player2":
        print(f"""
        {one}   {two}   {three}
        {four}   {five}   {six}
        {seven}   {eight}   {nine}""")
        print("Excellent! Now, Player 2 (O) will go: ")
        choice = input()
        if choice == "1":
            one = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "2":
            two = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "3":
            three = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "4":
            four = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "5":
            five = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "6":
            six = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "7":
            seven = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "8":
            eight = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        if choice == "9":
            nine = "O"
            data = {
                '1': one,
                '2': two,
                '3': three,
                '4': four,
                '5': five,
                '6': six,
                '7': seven,
                '8': eight,
                '9': nine,
                'player1': "X",
                'player2': "O",
                'player': player
            }
            db.child(game_id).set(data)
        player = "player1"
if one == two and two == three:
    won = True
if four == five and five == six:
    won = True
if seven == eight and eight == nine:
    won = True
if one == five and five == nine:
    won = True
if three == five and five == seven:
    won = True
if one == four and four == seven:
    won = True
if two == five and five == eight:
    won = True
if three == six and six == nine:
    won = True


if won == True:
    # Because it will change the player variable after the opponent has made their winning move
    if player == "player1":
        print("Congratulations, Player 2! You have won this game!")
    if player == "player2":
        print("Congratulations, Player 1! You have won this game!")
    
