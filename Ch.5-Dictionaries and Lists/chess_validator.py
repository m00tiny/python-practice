#!/usr/bin/env python3
# validate a chess board
ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
files = ["a", "b", "c", "d", "e" ,"f", "g", "h"]
white_pawns = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
black_pawns = ["p1", "p2", "p3", "p4", "p5", "p6", "p7", "p8"]
white_rooks = ["queens_rook", "kings_rook"]
black_rooks = ["queens_rook", "kings_rook"]
white_bishops = ["queens_bishop", "kings_bishop"]
black_bishops = ["queens_bishop", "kings_bishop"]
white_knights = ["queens_knight", "kings_knight"]
black_knights = ["queens_knight", "kings_knight"]
white_queen = ["white_queen"]
black_queen = ["black_queen"]
white_king = ["white_king"]
black_king = ["black_king"]
light_square = ["___"]
dark_square =["+++"]
board = {}
for i in range(len(files)):
    board = {files: ranks}
print(board)
