#!/bin/bash 
while [[ 1 -eq 1 ]]
do
registr=0               
echo 'Введите логин! '
read ul
while read login
do
if [[ $ul == $login ]]  
then
registr=1
fi
done < database            
if [[ $registr -eq 1 ]]     
then
echo "Логин занят! "
else
echo "Введите пароль! "
read -s password
echo "$ul" >>database
echo "$password" >>database
break
fi
done