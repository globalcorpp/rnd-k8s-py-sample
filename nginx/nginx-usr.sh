#!/bin/bash

echo Please, specify the filename properly - example is .htpasswd :
read filename
echo Please, specify the username:
read username

sh -c "echo -n '$username:' >> $PWD/$filename"
sh -c "openssl passwd -apr1 >> $PWD/$filename"
