Injectables
=======================

This is a super lightweight library for creating dependency injectables
::
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

    
    # run function as injectable, which resolves and injects all dependencies first
    conversation()
    # how are you?
    # I am fine
    # good to hear

    # override injection flow and call normally
    conversation(override=True, im_fine="hey!!!!")
    # hey!!!!
    # good to hear
