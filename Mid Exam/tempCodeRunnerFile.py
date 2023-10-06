 # def book_seats(self, show_id, seats_to_book):
    #     # Check if the show with the provided ID exists
    #     show_exists = False
    #     for show in self.show_list:
    #         if show['id'] == show_id:
    #             show_exists = True
    #             break
        
    #     if not show_exists:
    #         return "Show not found with the provided ID."
        
    #     # Check if the seats are available and mark them as booked
    #     if show_id in self.seats:
    #         seat_allocation = self.seats[show_id]
    #         for row, col in seats_to_book:
    #             if 0 <= row < self.rows and 0 <= col < self.cols:
    #                 if seat_allocation[row][col] == 'Free':
    #                     seat_allocation[row][col] = 'Booked'
    #                 else:
    #                     return f"Seat at row {row}, col {col} is already booked."
    #             else:
    #                 return f"Seat at row {row}, col {col} does not exist."
    #         return "Seats booked successfully."
    #     else:
    #         return "Seats for the provided show ID are not available."