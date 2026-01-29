#!/usr/bin/env bash
set -e

APP_NAME="bruteban"
INSTALL_DIR="/opt/$APP_NAME"
SERVICE_FILE="$APP_NAME.service"

echo "[*] Installing $APP_NAME..."

# проверка root
if [[ $EUID -ne 0 ]]; then
  echo "Run as root"
  exit 1
fi

# зависимости
echo "[*] Installing dependencies..."
dnf update
dnf install -y python3 python3-venv python3-pip

# копирование файлов
echo "[*] Copying files..."
rm -rf "$INSTALL_DIR"
mkdir -p "$INSTALL_DIR"
cp -r . "$INSTALL_DIR"

# venv
echo "[*] Creating virtualenv..."
python3 -m venv "$INSTALL_DIR/venv"
"$INSTALL_DIR/venv/bin/pip" install --upgrade pip

if [[ -f "$INSTALL_DIR/requirements.txt" ]]; then
  "$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"
fi

# systemd unit
echo "[*] Installing systemd unit..."
cp "$INSTALL_DIR/systemd/$SERVICE_FILE" /etc/systemd/system/$SERVICE_FILE

systemctl daemon-reload
systemctl enable $APP_NAME
systemctl restart $APP_NAME

echo "[✓] $APP_NAME installed and running"
