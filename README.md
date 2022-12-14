# MADPass : Site-Specific-Password-Generator
This tool combines your password with a name for a website to produce a
password unique to the site.  Using this tool, you only have to memorize
one password for all your Web logins, without worrying that anyone who
knows your password for one site will be able to use it on another one.

There are three input fields:

        Your password
                A string that you can remember.  It should still be hard for others
                to guess because this tool uses a well-known algorithm and you
                use a well-known site name.  Case sensitive.
        Site name
                Your name for the site.  For example, Schwab or Amazon.
                Case insensitive.
        Nb Char
                Allows you to define the number of characters your final password will have.

The site-specific password appears in the fourth field.  It will be composed of the number of ASCII characters that you will have predefined in the drop-down menu.  Click "Copy to Clipboard" or just press the Enter key to put the
generated password on the clipboard so you can paste it into the password
field on the web site.  If you are using a site that accepts only numbers and
letters in passwords, check "Letters and numbers only

# French
Cet outil combine votre mot de passe avec un nom de site Web pour produire un
mot de passe unique sur le site. En utilisant cet outil, vous n'avez qu'à mémoriser
un mot de passe pour toutes vos connexions Web, sans craindre que quiconque
sait que votre mot de passe pour un site pourra l'utiliser sur un autre.

Il existe trois champs de saisie:

        Votre mot de passe
                Une chaîne dont vous vous souviendrez. Cela devrait encore être difficile pour les autres
                deviner parce que cet outil utilise un algorithme bien connu et vous
                utilisez un nom de site bien connu. Sensible aux majuscules et minuscules.
        Nom du site
                Votre nom pour le site. Par exemple, Schwab ou Amazon.
                Insensible à la casse.
        Nb Char
                Permet de définir le nombre de caractères qu'aura votre mot de passe final

Le mot de passe spécifique au site apparaît dans le quatrième champ. Il sera composé du nombre caractère ASCII que vous aurez prédéfini dans le menu déroulant. 
Cliquez sur "Copier dans le presse-papiers" ou appuyez simplement sur la touche Entrée pour
mot de passe généré dans le presse-papiers afin que vous puissiez le coller dans le mot de passe
sur le site Web. Si vous utilisez un site qui n'accepte que des chiffres et
lettres dans les mots de passe, cochez "Lettres et chiffres uniquement.

# Installation
## Prérequis
- Installation de git, python3, pip, tkinter et pillow pour Python3 
```console 
foo@bar:~$ sudo apt install python3
foo@bar:~$ sudo apt install python3-tk
foo@bar:~$ sudo apt install python3-pip
foo@bar:~$ python3 -m pip install --upgrade pip
foo@bar:~$ python3 -m pip install --upgrade Pillow
```

- Clone the repository and copy file on **/usr/bin/**
```console 
foo@bar:~$ git clone https://github.com/EmGeI/MADPass/
foo@bar:~$ cd MADPass
foo@bar:~$ python3 MADPass.py
```

Vous pouvez ensuite créer un raccourci sur votre bureau si vous le souhaitez.
