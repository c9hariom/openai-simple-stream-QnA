from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def start_ftp_server():
    authorizer = DummyAuthorizer()

    # 👤 User create karo
    authorizer.add_user(
        username="user",
        password="12345",
        homedir="D:/",   # 👈 change here
        perm="elradfmw"
    )

    # 👤 Anonymous access (optional)
    # authorizer.add_anonymous("C:/ftp")

    handler = FTPHandler
    handler.authorizer = authorizer

    # 🌐 Server start
    server = FTPServer(("0.0.0.0", 21), handler)

    print("🚀 FTP Server running on port 21...")
    server.serve_forever()


if __name__ == "__main__":
    start_ftp_server()