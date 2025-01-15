from django.shortcuts import render, redirect

# Helper function to get or initialize the session state
def initialize_game(request):
    if 'board' not in request.session:
        request.session['board'] = [["", "", ""],
                                    ["", "", ""],
                                    ["", "", ""]]
    if 'current_player' not in request.session:
        request.session['current_player'] = "X"
    if 'winner' not in request.session:
        request.session['winner'] = ""
    if 'winning_cells' not in request.session:
        request.session['winning_cells'] = []

def home(request):
    return render(request, 'tic_tac_toe/home.html')

def play(request):
    # Initialize game state
    initialize_game(request)
    board = request.session['board']
    current_player = request.session['current_player']
    winner = request.session.get('winner', "")
    winning_cells = request.session.get('winning_cells', [])

    # Preprocess winning cells as strings (e.g., "0-1" for row 0, col 1)
    winning_cells_set = {f"{row}-{col}" for row, col in winning_cells}

    # Preprocess the board into a list of rows with cell data
    board_with_coords = [
        [{'value': board[r][c], 'row': r, 'col': c} for c in range(3)] for r in range(3)
    ]

    if request.method == 'POST':
        # Handle reset request
        if 'reset' in request.POST:
            request.session.flush()
            return redirect('play')

        # Handle game move
        row = int(request.POST['row'])
        col = int(request.POST['col'])

        # Update the board if valid move
        if board[row][col] == "" and not winner:
            board[row][col] = current_player
            request.session['board'] = board

            # Check for winner
            result = check_winner(board, current_player)
            if result:
                request.session['winner'] = current_player
                request.session['winning_cells'] = result
            else:
                # Switch player
                request.session['current_player'] = "O" if current_player == "X" else "X"

        return redirect('play')

    return render(request, 'tic_tac_toe/play.html', {
        'board': board_with_coords,  # Preprocessed board with coordinates
        'current_player': current_player,
        'winner': winner,
        'winning_cells': winning_cells_set,  # Preprocessed winning cells
    })



def check_winner(board, player):
    # Define all winning combinations
    winning_combinations = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combination in winning_combinations:
        if all(board[row][col] == player for row, col in combination):
            return combination  # Return the winning combination

    return None  # No winner yet
