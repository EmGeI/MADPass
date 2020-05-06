# Site-Specific-Password-Generator
This tool combines your password with a name for a website to produce a
password unique to the site.  Using this tool, you only have to memorize
one password for all your Web logins, without worrying that anyone who
knows your password for one site will be able to use it on another one.

There are two input fields:

        Your password
                A string that you can remember.  It should still be hard for others
                to guess because this tool uses a well-known algorithm and you
                use a well-known site name.  Case sensitive.
        Site name
                Your name for the site.  For example, Schwab or Amazon.
                Case insensitive.

The site-specific password appears in the third field.  It will be 12 ASCII
characters.  Click "Copy to Clipboard" or just press the Enter key to put the
generated password on the clipboard so you can paste it into the password
field on the web site.  If you are using a site that accepts only numbers and
letters in passwords, check "Letters and numbers only

# French
Cet outil combine votre mot de passe avec un nom de site Web pour produire un
mot de passe unique sur le site. En utilisant cet outil, vous n'avez qu'à mémoriser
un mot de passe pour toutes vos connexions Web, sans craindre que quiconque
sait que votre mot de passe pour un site pourra l'utiliser sur un autre.

Il existe deux champs de saisie:
> Votre mot de passe
  > - Une chaîne dont vous vous souviendrez. Cela devrait encore être difficile pour les autres deviner parce que cet outil utilise un algorithme bien connu et vous utilisez un nom de site bien connu. 
  > - Sensible aux majuscules et minuscules.
  
> Nom du site
  > - Votre nom pour le site. Par exemple, Schwab ou Amazon.
  > - Insensible à la casse.

Le mot de passe spécifique au site apparaît dans le troisième champ. Il sera composé de 12 caractère ASCII. 
Cliquez sur "Copier dans le presse-papiers" ou appuyez simplement sur la touche Entrée pour
mot de passe généré dans le presse-papiers afin que vous puissiez le coller dans le mot de passe
sur le site Web. Si vous utilisez un site qui n'accepte que des chiffres et
lettres dans les mots de passe, cochez "Lettres et chiffres uniquement.

# Installation
## Prérequis
- Installation de tkinter pour Python3 
```console 
foo@bar:~$ sudo apt install python3-tkinter
```

- Clone the repository and copy file on **/usr/bin/**
```console 
foo@bar:~$ git clone https://github.com/EmGeI/Site-Specific-Password-Generator/
foo@bar:~$ cd Site-Specific-Password-Generator
foo@bar:~$ sudo cp ssp.pyw /usr/bin/
```

You can create a launcher on the desktop for convenience
