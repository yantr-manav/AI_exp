% Tic-Tac-Toe AI Implementation using Prolog

% Define winning conditions
win(Player, Board) :-
    Board = [Player, Player, Player, _, _, _, _, _, _];
    Board = [_, _, _, Player, Player, Player, _, _, _];
    Board = [_, _, _, _, _, _, Player, Player, Player];
    Board = [Player, _, _, Player, _, _, Player, _, _];
    Board = [_, Player, _, _, Player, _, _, Player, _];
    Board = [_, _, Player, _, _, Player, _, _, Player];
    Board = [Player, _, _, _, Player, _, _, _, Player];
    Board = [_, _, Player, _, Player, _, Player, _, _].

% Check if a position is free
free(Position, Board) :-
    nth0(Position, Board, empty).

% AI move: take the winning move if possible
best_move(Board, Move) :-
    nth0(Move, Board, empty),
    nth0(Move, NewBoard, x, Board),
    win(x, NewBoard), !.

% AI move: block the opponent if they are about to win
best_move(Board, Move) :-
    nth0(Move, Board, empty),
    nth0(Move, NewBoard, o, Board),
    win(o, NewBoard), !.

% AI move: choose the first available move
best_move(Board, Move) :-
    nth0(Move, Board, empty).

% Display the board
print_board([A, B, C, D, E, F, G, H, I]) :-
    format('~w | ~w | ~w~n', [A, B, C]),
    format('---------~n'),
    format('~w | ~w | ~w~n', [D, E, F]),
    format('---------~n'),
    format('~w | ~w | ~w~n', [G, H, I]).

