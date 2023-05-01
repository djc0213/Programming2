from typing import List

class Client:
    active: bool

def email(client: Client) -> None:
    pass

def get_active_clients(clients: List[Client]) -> List[Client]:
    """Filter active clients.
    """
    return [client for client in clients if client.active]

def email_clients(clients: List[Client]) -> None:
    """Send an email to a given list of clients.
    """
    for client in get_active_clients(clients):
        email(client)

def create_file(filename: str, temp: bool):
    f = open(filename, 'w')
    f.close()
def create_temp_file(filename: str):
    create_file('temp_' + filename)