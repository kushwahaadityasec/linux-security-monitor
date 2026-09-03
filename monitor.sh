#!/bin/bash

echo "=========================================="
echo "       LINUX SECURITY SYSTEM CHECK"
echo "=========================================="

echo
echo "[1] Current User"
whoami

echo
echo "[2] Logged-in Users"
who

echo
echo "[3] IP Addresses"
ip -brief address

echo
echo "[4] Disk Usage"
df -h /

echo
echo "[5] Running Processes"
ps aux | head -10

echo
echo "[6] Recent Authentication Events"
journalctl --no-pager -n 20

echo
echo "=========================================="
echo "             CHECK COMPLETE"
echo "=========================================="
