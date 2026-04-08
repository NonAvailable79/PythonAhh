'''
NOTES ON USING TKINTER FROM THE BOOK
ALL FUNCTION NAMES NEED THE MODULE NAME
______________________________________________________

1. Starting
Make a window with Tk().
Set title with window.title('title').

Must have:  a window.mainloop() to call events at the endish of the program.
______________________________________________________

2. Things on the thing

~~~~~Labels~~~~~
Make a label by assigning a variable to
Label(window, text = '')

Pack it with label.pack(padx = , pady = )

Update it with label.configure(anything you want to change)

~~~~~~Buttons~~~~~~~
Create a button on the window by assigning a variable to
Button(window, text = '', command = (any function you define previously))
The command argument should not have any brackets.

Other arguments: activebackground(when touching mouse), activeforeground
(when touching mouse), bd(border width), bg(colour), fg(foreground colour),
font, height, highlightcolour (border when the button is in focus), image
(instead of text), justify(LEFT, CENTER, RIGHT), relief(border style SUNKEN,
RIDGE, RAISED, GROOVE), state(normal or disabled), underline(index number of
the character(s)), width, wraplength(for wrapping text).

Pack it with button.pack(padx= , pady= )

Update it with button.configure(anything you want to change)

~~~~~~~~~~~~~Entry Widgets~~~~~~~~~~~~~~~~~
First define a frame with frame = Frame(window).
Then put the entry on the frame with entry = Entry(frame).

'''

print('Please check documentation')
