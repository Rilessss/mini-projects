import random

MAXL = 3
MAXB = 1000
MINB = 1

ROWS = 3    
COLS = 3 

symbol_count = {
    "!": 2,
    "+": 4,
    "=": 6,
    "-": 8
}
symbol_value = {
    "!": 10,
    "+": 5,
    "=": 2,
    "-": 0.5
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(column[line] == symbol for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    
    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    
    return columns

def print_slots(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
               print(column[row],end=" | ")
            else:
               print(column[row], end = "")

        print()

def deposit():
    while True:
        amount = input("how much do you want to deposit? : $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("amount must be more than 0")
        else:
            print("enter a number")

def get_number_of_lines():
    while True:
        lines = input("how many lines do you want to bet on? (1-" + str(MAXL)+")?")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAXL:
                return lines
            else:
                print("enter a valid number of lines")
        else:
            print("enter a number")

def get_bet():
    while True:
        amount = input("how much do you want to bet on each line? : $")
        if amount.isdigit():
            amount = int(amount)
            if MINB <= amount <= MAXB:
                return amount
            else:
                print(f"amount must be between ${MINB} to ${MAXB}")
        else:
            print("enter a number")

def spin(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet*lines
        
        if total_bet > balance:
            print(f"you have insufficient balance to bet, your current balance is ${balance}")
        else:
            break
    print(f"you are betting ${bet} on {lines} lines, total bet is ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slots(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"you won a total of ${winnings}!")
    print(f"you won from lines:", *winning_lines)
    return balance + winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"current balance: ${balance}")
        a = input("press enter to spin, or press q to quit")
        if a == "q":
            break
        balance = spin(balance)
    print(f"you left the slot machine with ${balance}")

main()