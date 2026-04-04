#!/usr/bin/env bash
set -e

APP_NAME="bruteban"
INSTALL_DIR="/usr/local/lib/$APP_NAME"
CONFIG_DIR="/etc/$APP_NAME"
LOG_DIR="/var/log/$APP_NAME"
SERVICE_FILE="$APP_NAME.service"

check_root() {
  if [[ $EUID -ne 0 ]]; then
    echo "Запустить от имени root."
    exit 1
  fi
}

install_deps() {
  if command -v apt >/dev/null 2>&1; then
    apt install python3 python3-venv python3-pip iptables libsystemd-dev pkg-config
  elif command -v dnf >/dev/null 2>&1; then
    dnf install python3 python3-venv python3-pip iptables systemd-devel pkgconf-pkg-config
  elif command -v yum >/dev/null 2>&1; then
    yum install python3 python3-venv python3-pip iptables systemd-devel pkgconfig
  elif command -v pacman >/dev/null 2>&1; then
    pacman install python3 python3-venv python3-pip iptables
  elif command -v zypper >/dev/null 2>&1; then
    zypper install python3 python3-venv python3-pip iptables
  fi
}

install_app() {
  rm -rf "$INSTALL_DIR"
  mkdir -p "$INSTALL_DIR"
  cp -r . "$INSTALL_DIR"

  mkdir -p "$CONFIG_DIR"
  cp "$PWD"/config/bruteban.conf $CONFIG_DIR
  cp "$PWD"/config/sshd.conf $CONFIG_DIR
  mkdir -p "$LOG_DIR"

  python3 -m venv "$INSTALL_DIR/venv"
  "$INSTALL_DIR/venv/bin/pip" install --upgrade pip

  if [[ -f "$INSTALL_DIR/requirements.txt" ]]; then
    "$INSTALL_DIR/venv/bin/pip" install -r "$INSTALL_DIR/requirements.txt"
  fi

  cp "$INSTALL_DIR/systemd/$SERVICE_FILE" /etc/systemd/system/$SERVICE_FILE
}

main() {
  echo "[*] Проверка прав root..."
  check_root
  echo "[*] Установка зависимостей..."
  install_deps
  echo "[*] Установка приложения..."
  install_app
  echo "[*] $APP_NAME установлен успешно."
}

main