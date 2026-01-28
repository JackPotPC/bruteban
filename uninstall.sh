#!/usr/bin/env bash
set -e

APP_NAME="bruteban"
INSTALL_DIR="/opt/$APP_NAME"

if [[ $EUID -ne 0 ]]; then
  echo "Run as root"
  exit 1
fi

systemctl stop $APP_NAME || true
systemctl disable $APP_NAME || true
rm -f /etc/systemd/system/$APP_NAME.service
systemctl daemon-reload

rm -rf "$INSTALL_DIR"

echo "[✓] $APP_NAME removed"
