#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ticket_dict = {}
    route = []

    for ticket in tickets:
        ticket_dict[ticket.source] = ticket.destination

    destination = ticket_dict["NONE"]
    route.append(destination)
    while destination != "NONE":
        destination = ticket_dict[destination]
        route.append(destination)

    return route


if __name__ == "__main__":
    ticket_1 = Ticket("PIT", "ORD")
    ticket_2 = Ticket("XNA", "SAP")
    ticket_3 = Ticket("SFO", "BHM")
    ticket_4 = Ticket("FLG", "XNA")
    ticket_5 = Ticket("NONE", "LAX")
    ticket_6 = Ticket("LAX", "SFO")
    ticket_7 = Ticket("SAP", "SLC")
    ticket_8 = Ticket("ORD", "NONE")
    ticket_9 = Ticket("SLC", "PIT")
    ticket_10 = Ticket("BHM", "FLG")

    tickets = [ticket_1, ticket_2, ticket_3, ticket_4, ticket_5, 
        ticket_6, ticket_7, ticket_8, ticket_9, ticket_10]

    result = reconstruct_trip(tickets, 10)

    print(result)
