class Clients:
    connections = dict()
    __users = dict()

    @classmethod
    def get_user(cls, user_id):
        return cls.__users[user_id] if user_id in cls.__users else []

    @classmethod
    def set_connection(cls, connection, fd):
        if fd not in cls.connections:
            cls.connections[fd] = (connection, None)

    @classmethod
    def remove_connection(cls, fd):
        if fd in cls.connections:
            user_id = cls.connections[fd][1]
            if user_id is not None:
                cls.__users[user_id].discard(fd)
            del cls.connections[fd]

    @classmethod
    def set_client(cls, user_id, fd):
        if user_id not in cls.__users:
            cls.__users[user_id] = {fd}
        else:
            cls.__users[user_id].add(fd)
