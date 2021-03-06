"""
Required Settings:

    hostname            - The hostname of the server to check (For example, your servers hostname or IP address)
    recipient_email     - The email where downtime alerts will be sent to
    monitor_email       - The email address to be sent from
    monitor_password    - The password of the email address to be sent from
    monitor_server      - The email server to send the emails from
    monitor_server_port - The email server smtp port

Optional Settings:

    email_subject       - The subject of the email to send

"""
sites = (
    '8.8.8.8',
    '8.8.4.4',
)

settings = {
    "recipient_email": 'recipient@yourdomain.com',
    "monitor_email": 'monitor@yourdomain.com',
    "monitor_password": 'monitor email password',

    # Leave as it is to use gmail as the server
    "monitor_server": 'smtp.gmail.com',
    "monitor_server_port": 587,

    # Optional Settings
    "email_subject": 'Server Monitor Alert'
}
