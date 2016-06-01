Injectables
=======================

This is a super lightweight library for creating dependency injectables
::
    from injectables import injectable


    @injectable
    def how_are_you():
      return "how_are_you?"


    @injectable
    def im_fine(how_are_you):
      print(how_are_you)
      return 'I am fine'


    @injectable
    def conversation(im_fine):
      print (im_fine)
      print ('good to hear')


    conversation()
    # how are you?
    # I am fine
    # good to hear
