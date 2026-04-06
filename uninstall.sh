#!/usr/bin/env bash
set -e

APP_NAME="bruteban"
INSTALL_DIR="/usr/local/lib/$APP_NAME"
CONFIG_DIR="/etc/$APP_NAME"
LOG_DIR="/var/log/$APP_NAME"
SERVICE_FILE="$APP_NAME.service"

check_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "Запустить с sudo"
    exit 1
  fi
}

uninstall_app() {
  rm -rf $INSTALL_DIR
  rm -rf $CONFIG_DIR
  rm -rf $LOG_DIR
}

stop_service() {
  systemctl stop $APP_NAME || true
  systemctl disable $APP_NAME || true
  rm -f /etc/systemd/system/$SERVICE_FILE
  systemctl daemon-reload
}

main() {
  echo "[*] Проверка root..."
  check_root
  echo "[*] Остановка сервиса..."
  stop_service
  echo "[*] Удаление приложения..."
  uninstall_app
  echo "[*] Удаление завершено."
}

main