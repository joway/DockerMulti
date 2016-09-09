PASS=${ROOT_PASS:-$(pwgen -s 12 1)}
echo "root:$PASS" | chpasswd

echo "\n \
          ========================================================================\n \
          You can now connect to this Ubuntu container via SSH using:\n\n \
          ssh -p <port> root@<host>\n \
          and enter the root password '$PASS' when prompted\n\n \
          Please remember to change the above password as soon as possible! \n \
          ========================================================================\n"


exec /usr/sbin/sshd -D