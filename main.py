import random

MAX_LINE = 3
MIN_LINE = 1
MIN_BET = 2
MAX_BET = 50
ROWS = 3
COLS = 3

symbol_count = {
	"A": 3,
	"B": 4,
	"C": 5,
	"D": 6
}

symbol_value = {
	"A": 5,
	"B": 3,
	"C": 8,
	"D": 2
}


def deposit():
	while True:
		deposit = input("What would you like to deposit? : $")
		if deposit.isdigit():
			deposit = int(deposit)
			if deposit > 0:
				break
			else:
				print("The deposit must be geater than zero.")
		else:
			print("Please, enter a number.")
	return deposit


def get_line():
	while True:
		lines = input(f"Amount of lines you would like to bet on ({MIN_LINE} - {MAX_LINE}): ")
		if lines.isdigit():
			lines = int(lines)
			if MIN_LINE <= lines <= MAX_LINE:
				break
			else:
				print(f"Amount of lines must be within ({MIN_LINE} - {MAX_LINE}).")
		else:
			print("Please, enter a number.")
	return lines


def get_bet():
	while True:
		bet = input(f"How much you want ot bet on each line? ({MIN_BET} - {MAX_BET}): $")
		if bet.isdigit():
			bet = int(bet)
			if MIN_BET <= bet <= MAX_BET:
				break
			else:
				print(f"Bet on each line must be within ({MIN_BET} - {MAX_BET}).")
		else:
			print("Please, enter a number.")
	return bet


def get_slot_machine_spin(rows, cols, symbols):
	all_symbols = []
	for symbol, symbol_count in symbols.items():
		for _ in range(symbol_count):
			all_symbols.append(symbol)
	columns = []
	for _ in range(rows):
		column = []
		current_symbols = all_symbols[:]
		for _ in range(cols):
			value = random.choice(current_symbols)
			current_symbols.remove(value)
			column.append(value)
		columns.append(column)
	return columns


def print_slot_machine(columns):
	for row in range(len(columns)):
		for col in columns:
			print(col[row], end=" ")
		print()


def check_winnings(columns, lines, bet, values):
	winnings = 0
	winnings_lines = []
	for line in range(lines):
		symbol = columns[0][line]
		for column in columns:
			symbol_to_check = column[line]
			if symbol != symbol_to_check:
				break
		else:
			winnings += values[symbol] * bet
			winnings_lines.append(line + 1)
	return winnings, winnings_lines


def spin(balance):
	lines = get_line()
	while True:
		bet = get_bet()
		total_bet = bet * lines
		if total_bet < balance:
			break
		else:
			print("You do not have enough to make such a bet. Choose different bet, please.")
	print()
	print(f"Your current balance : ${balance}", f"Amount of line(s) you bet on : {lines}",
	      f"Bet on each line  : ${bet}", f"Total bet : ${total_bet}", sep="\n")
	slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
	print_slot_machine(slots)
	winning, winning_lines = check_winnings(slots, lines, bet, symbol_value)
	print(f"You won ${winning}.")
	print(f"You won on line(s): ", *winning_lines)
	return winning - total_bet


def main():
	balance = deposit()
	while balance > 0:
		print(f"You current balance is: {balance}")
		answer = input("Enter enter to play ('q' to quit)")
		if answer == 'q':
			break
		balance += spin(balance)
		print(f"You left with {balance}")


main()