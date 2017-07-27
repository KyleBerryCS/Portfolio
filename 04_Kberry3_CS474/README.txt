    How to Use:

    First compile Set.cpp on the command line as so:
    g++ Set.cpp
    
    Then run the resulting a.exe (or a.out if using ubuntu). You will be prompted for a command. Enter any of the letters below and
    then hit 'enter'.  If you choose the 'a' command, you will then be asked to input an int. Input the int and hit 'enter'. Commands
    that need initialized sets to function (everything except l, o, and q), will not do anything until the sets have been initialized
    at least once.

   l (lowercase L)— Initialize sets as lists. This command allows interactive users to reset the
    calculator and initialize two new sets A and B using the linked list implementation of sets. The
    current sets A and B, if they exist, are be deleted.
   o — Initialize sets as ordered collections. This command allows interactive users to reset
    the calculator and initialize two new sets A and B using the ordered collection implementation.
    Existing sets A and B are deleted.
   e — Erase set. This command allows interactive users to delete the current A set. The previous
    value stored in A is lost. A is bound to a new, empty set after this command is complete.
   s — Switch sets. The sets associated with A and B are swapped, meaning that A will receive the
    previous B set and vice versa.
   c — Copy set. Set A is deep copied into B. The previous content of B is lost. The content of
    A is not affected. The two sets do not share any data structures, that is, they can be modified
    independently of each other.
   d — Display set contents. The integers stored in the two sets are displayed on the standard
    output stream. The two sets are not modified.
   a — Add element. This function allows a user to add a new integer to A. The value is obtained
    through an appropriate prompt with an interactive user. No action is taken if the integer in question
    is already in the set.
   u — Union. This element takes the set union of A and B and stores the resulting value in A. The
    previous content of A is lost. Set B is not modified by this operation.
   i — Intersection. This command takes the set intersection of A and B and stores the resulting
    value in A. The previous content of A is lost. Set B is not modified by this operation.
   q— Quits the set manager.