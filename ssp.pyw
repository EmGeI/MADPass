# Copyright 2002, Hewlett-Packard
#
# A little program to hash a user password with a site-specific string
# The result is a random looking string that can be used as a password
# on that site.  This tool lets you enter the same password string for
# all sites, but gives you a unique password to use for each site.
#
# 2002-02-07 - Initial VERSION 0.1
# 2002-02-07 - Changed result field so it can be cut and pasted, VERSION 0.2
# 2005-04-24 - Added alphanumeric option and clipboard handling, VERSION 0.3
# 2020-05-07 - Rewrite for Python3 compatibility, VERSION 0.4
#
# To do:
# 1. Make a browser plugin that pops up when a password field appears
# 2. Port to Jornada
#
# Alan Karp, alan.karp@hp.com, 7 February 2002
# Ka-Ping Yee, zestyping@hp.com, 24 April 2005
# Madenn Munten, madenn@munten.name, 7 May 2020

import hashlib
from tkinter import *
import base64
from PIL import Image, ImageTk

VERSION="0.4"
LABEL_FONT=('Helvetica', 9)
ENTRY_FONT=('Courier', 10)

def show_help_fr():
    """Display the help window."""
    window = Toplevel()
    Message(window, text="""
                                Générateur de mot de passe spécifique par site
                                (Brevet en instance, Hewlett-Packard)

Cet outil combine votre mot de passe avec un nom de site Web pour produire un
mot de passe unique sur le site. En utilisant cet outil, vous n'avez qu'à mémoriser
un mot de passe pour toutes vos connexions Web, sans craindre que quiconque
sait que votre mot de passe pour un site pourra l'utiliser sur un autre.

Il existe deux champs de saisie:

        Votre mot de passe
                Une chaîne dont vous vous souviendrez. Cela devrait encore être difficile pour les autres
                deviner parce que cet outil utilise un algorithme bien connu et vous
                utilisez un nom de site bien connu. Sensible aux majuscules et minuscules.
        Nom du site
                Votre nom pour le site. Par exemple, Schwab ou Amazon.
                Insensible à la casse.

Le mot de passe spécifique au site apparaît dans le troisième champ. Il sera composé de 12 caractère ASCII. 
Cliquez sur "Copier dans le presse-papiers" ou appuyez simplement sur la touche Entrée pour
mot de passe généré dans le presse-papiers afin que vous puissiez le coller dans le mot de passe
sur le site Web. Si vous utilisez un site qui n'accepte que des chiffres et
lettres dans les mots de passe, cochez "Lettres et chiffres uniquement".
        """, font=LABEL_FONT).pack()
    Button(window, text='Close', font=LABEL_FONT, command=window.destroy).pack()

def show_help():
    """Display the help window."""
    window = Toplevel()
    Message(window, text="""
                                Site-Specific Password Generator
                                (Patent Pending, Hewlett-Packard)

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
letters in passwords, check "Letters and numbers only".
        """, font=LABEL_FONT).pack()
    Button(window, text='Close', font=LABEL_FONT, command=window.destroy).pack()


def generate_password(password, sitename, alphanumeric=0):
    """Compute a site-specific password."""
    # Use the MD5 hash algorithm to combine the inputs.
    digest = hashlib.md5(str(sitename.lower() + password).encode('utf-8'))
    digest = digest.digest()
    digest = base64.encodebytes(digest).decode('utf-8')
    if alphanumeric:
    	digest = digest.replace('/', '').replace('+', '')
    return digest[:12]

class SitePasswordForm:
    def __init__(self, parent):
        self.parent = parent
        
        # variables
        self.password = StringVar(parent)
        self.sitename = StringVar(parent)
        self.result = StringVar(parent)
        self.alpha = BooleanVar(parent)
        self.password.trace('w', self.update_password)
        self.sitename.trace('w', self.update_password)
        self.alpha.trace('w', self.update_password)

        # password entry field
        self.password_label = Label(parent, text='Your password:', font=LABEL_FONT)
        self.password_entry = Entry(parent, show='*', font=ENTRY_FONT,
                              textvar=self.password)

        # site entry field
        self.sitename_label = Label(parent, text='Site name:', font=LABEL_FONT)
        self.sitename_entry = Entry(parent, font=ENTRY_FONT, textvar=self.sitename)

        # output field
        self.result_label = Label(parent, text='Site password:', font=LABEL_FONT)
        self.result_entry = Entry(parent, state='readonly', relief=RIDGE,
                                  font=ENTRY_FONT, textvar=self.result)

        # check box
        self.alpha_check = Checkbutton(parent, text='Letters and numbers only',
                                       font=LABEL_FONT, variable=self.alpha)

        # buttons
        self.button_frame = Frame(parent)
        self.copy_button = Button(self.button_frame, text='Copy to Clipboard (Enter)',
                                  font=LABEL_FONT, command=self.copy_result, padx=10)
        self.help_fr_button = Button(self.button_frame, text='Aide',
                                  font=LABEL_FONT, command=show_help_fr, padx=10)
        self.help_button = Button(self.button_frame, text='Help',
                                  font=LABEL_FONT, command=show_help, padx=10)

        # layout
        self.password_label.grid(row=0, column=0, sticky=E)
        self.password_entry.grid(row=0, column=1)
        self.sitename_label.grid(row=1, column=0, sticky=E)
        self.sitename_entry.grid(row=1, column=1)
        self.result_label.grid(row=2, column=0, sticky=E)
        self.result_entry.grid(row=2, column=1)
        self.alpha_check.grid(row=3, column=1, sticky=W)
        self.copy_button.pack(side=LEFT)
        self.help_button.pack(side=LEFT)
        self.help_fr_button.pack(side=LEFT)
        self.button_frame.grid(row=4, column=0, columns=2)

        # key bindings
        self.password_entry.bind('<Return>', self.handle_return)
        self.sitename_entry.bind('<Return>', self.handle_return)

        # startup
        self.update_password()
        self.password_entry.focus()
        
    def update_password(self, *args):
        """Update the site-specific password field."""
        password = self.password.get().strip()
        sitename = self.sitename.get().strip()
        alpha = self.alpha.get()
        if password and sitename:
            self.result.set(generate_password(password, sitename, alpha))
            self.copy_button['state'] = ACTIVE
        else:
            self.result.set('')
            self.copy_button['state'] = DISABLED

    def handle_return(self, *args):
        """When the user presses Enter, advance to the next obvious step."""
        if not self.password.get().strip():
            self.password_entry.focus()
        elif not self.sitename.get().strip():
            self.sitename_entry.focus()
        else:
            self.copy_result()

    def copy_result(self, *args):
        """Place the site-specific password on the clipboard."""
        if self.result.get():
            self.result_entry.focus()
            self.result_entry.selection_range(0, 'end')
            self.parent.clipboard_clear()
            self.parent.clipboard_append(self.result.get())

root = Tk()
root.title('Site-Specific Password ' + VERSION)
SitePasswordForm(root)
root.mainloop()
