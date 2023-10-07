class Star_Cinema:
    hall_list = []
    def entry_hall(self, hall):
        self.hall_list.append(hall)
    
class Hall:
    def __init__(self, rows, cols, hall_no):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {} 
        self.show_list = [] 
    def entry_show(self, id, movie_name, time):
        show_info = {"id": id, "movie_name": movie_name, "time": time}
        self.show_list.append(show_info)
        
        seat_allocation = [['0' for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[id] = seat_allocation
    
    def book_seats(self, show_id, row, col):
        show_exists = False
        for show in self.show_list:
            if show["id"] == show_id:
                show_exists = True
                

        if show_exists:
            if 0 <= row < self.rows and 0 <= col < self.cols:
                if self.seats[show_id][row][col] == '0':
                    self.seats[show_id][row][col] = '1'
                    print(f'Seat ({row}, {col}) booked for Show ID {show_id}')
                else:
                    print(f'Seat at Row {row}, Col {col} is already booked for Show ID {show_id}')
            else:
                print('Invalid row or column')
        else:
            print(f'Show ID {show_id} does not exist')


    def view_show_list(self):
        print("List of Shows:")
        for show in self.show_list:
            print(f"Show ID: {show['id']}, Movie Name: {show['movie_name']}, Time: {show['time']}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            seat_allocation = self.seats[show_id]
            print(f"Available Seats for Show ID {show_id}:")
            for row in range(self.rows):
                for col in range(self.cols):
                    if seat_allocation[row][col] == '0':
                        print(f"seat({row}, {col})")
            print(f'update seats Matrix for Hall {self.hall_no}\n')
            
            for row in range(self.rows):
                row_str = ""
                for col in range(self.cols):
                    if seat_allocation[row][col] == '0':
                        row_str += "0"
                    else:
                        row_str += "1"
                print(" ".join(row_str))
            print('\n')
        else:
            return "Show not found with the provided ID."

        
bts=Star_Cinema()
hall1 = Hall(5, 5,1)
hall1.entry_show(12,'jawan maji','10.00 pm')
hall1.entry_show(13,'kawan maji','11.00 pm')
hall1.entry_show(14,'gawan maji','12.00 pm')


while True:
    print('1. VIEW ALL SHOW TODAY')
    print('2. VIEW AVAILABLE SEATS')
    print('3. BOOK TICKET')
    print('4. EXIT')
    ch = int(input('ENTER OPTION: '))
    if ch == 1:
        for show in hall1.show_list:
            print(f"Show ID: {show['id']}, Movie Name: {show['movie_name']}, Time: {show['time']}")
    elif ch==2:
        show_id = int(input('Enter the Show ID: '))
        available_seats = hall1.view_available_seats(show_id)
        if isinstance(available_seats, list):
            if not available_seats:
                print("No available seats for this show.")
            else:
                print("\nAvailable Seats for Show ID", show_id)
                for row, col in available_seats:
                    print(f"Row {row}, Col {col}")
    elif ch==3:
        show_id = int(input("SHOW ID: "))
        cnt_ticket = int(input("NUMBER OF TICKET:? "))
        row = int(input("ENTER SEAT ROW: "))
        col = int(input("ENTER SEAT COL: "))
        hall1.book_seats(show_id, row, col)
    elif ch ==4:
        print('Exitting....')
        break
    else:
        print("Invalid Option!")
    
