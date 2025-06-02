import paramiko

def try_ssh_login(server, username, password):
    client = paramiko.SSHClient()
    # Automatically add the server's host key (not secure for production)
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        client.connect(server, username=username, password=password)
        # If we get here, the password is correct
        client.close()
        return True
    except paramiko.AuthenticationException:
        # Wrong password
        return False
    except Exception as e:
        # Other errors (network, timeout, etc.)
        print(f"Error: {e}")
    finally:
        client.close()