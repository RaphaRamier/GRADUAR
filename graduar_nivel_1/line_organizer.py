import random


def service_time_generator():
    return random.randint(5, 15)


class LineOrganizer:
    def __init__(self):
        self.queue={}
        self.next_ticket=1
        self.ticket_attended={}

    def add_client(self, client):
        ticket=len(self.queue) + 1
        self.queue.update({ticket: client})

    def call_ticket(self):
        for key, value in self.queue.items():
            if key == self.next_ticket:
                print(f'Calling {value} Ticket number: {key}')
                break
            else:
                print("Queue is empty.")

    def drop_ticket(self):
        if self.queue:
            client=self.queue[self.next_ticket]
            del self.queue[self.next_ticket]
            service_time=service_time_generator()
            self.ticket_attended[self.next_ticket]=service_time
            print(f'Calling client: {client} Ticket number: {self.next_ticket}.')
            self.next_ticket+=1

        else:
            return print("Queue is empty.")

    def view_queue(self):
        if self.queue:
            print("Current Queue:")
            for ticket, client in self.queue.items():
                print(f"Ticket number: {ticket}, Client: {client}")
        else:
            print("Queue is empty.")

    def calculate_stats(self):
        avg_time=sum(self.ticket_attended.values()) / len(self.ticket_attended)
        print("Statistics:")
        print(f"Waiting average time: {avg_time:.2f} minutes")


def main():
    organizer=LineOrganizer()

    while True:
        print("\nOptions:")
        print("1. Add client to queue")
        print("2. View queue")
        print("3. Calling ticket")
        print("4. Drop ticket")
        print("5. Calculate statistics")
        print("6. Exit")
        choice=input("Enter your choice: ")

        if choice == "1":
            client_name=input("Enter client name: ")
            organizer.add_client(client_name)
        elif choice == "2":
            organizer.view_queue()
        elif choice == "3":
            organizer.call_ticket()
        elif choice == "4":
            organizer.drop_ticket()
        elif choice == "5":
            organizer.calculate_stats()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()


