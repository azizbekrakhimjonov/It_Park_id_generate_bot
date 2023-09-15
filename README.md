Id card bot 
dev: @azizbekrahimjonov571

#////////////////////////////////
systemctl enable idcardbot.service
systemctl restart idcardbot.service
systemctl status idcardbot.service

#////////////////////////////////
[Unit]
Description=Aiogram delete all links
After=network.target

[Service]
ExecStart=/root/idcardbot/venv/bin/python run_main.py
ExecReload=/root/idcardbot/venv/bin/python run_main.py
WorkingDirectory=/root/idcardbot/
KillMode=process
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target

#////////////////////////////////
journalctl -u idcardbot.service -n 100