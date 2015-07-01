/*
    This file contains the Abstract Set Class along with two concrete subclasses: SetAsList and SetAsOC.
    These classes handle two sets of ints - A and B.  The sets are either LinkedLists or OrderedCollections.
    To be specific, each class has an A and a B but those classes will themselves be instances of either SetAsList or SetAsOC (with their own A and B = NULL).
    A and B are Set pointers in all cases (polymorphic identifiers).
    The sets do not contain duplicates.
    It also contains a Main() that handles interacting with the classes via the command line.
    How to Use:

    First compile Set.cpp on the command line as so:
    g++ Set.cpp
    
    then run the resulting a.exe (or a.out if using ubuntu). You will be prompted for a command. Enter any of the letters below and
    then hit 'enter'.  If you choose the 'a' command, you will then be asked to input an int. Input the int and hit 'enter'.

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
    

*/




//#ifndef __Set_H_INCLUDED__
//#define __Set_H_INCLUDED__
#include <stdio.h>
#include <iostream>
#include "474LinkedList.cpp"
#include "474OC.cpp"
using namespace std;

//Abstract Superclass
class Set
{
    public:
        Set * A;
        Set * B;      
        
        Set()
        {
            A = NULL;
            B = NULL;
        }
        
        //Stores the union of A and B into A.
        void Union()
        {
          int theSize = B->Size();
          int current;
          for(int i = 0; i < theSize; ++i)
            {
                current = (*B)[i];
                this->AddElement(current);
            } 
        };      
         
        //Stores the intersection of A and B into A.
        //The shared elements are always in the same order they were in in B.
        void intersection()
        {
          int theSize = B->Size();
          int otherSize = A->Size();
          int current;
          bool done = false;
          int innerI = 0;
          int tempValues[theSize];
          int numTemp = 0;
          for(int i = 0; i < theSize; ++i)
            {
                current = (*B)[i];
                while(innerI < otherSize && done == false)
                {                
                    if(current == (*A)[innerI])
                    {
                      tempValues[numTemp] = current;
                      ++numTemp;
                      done = true;
                    }
                    ++innerI;
                }
                innerI = 0;
                done = false;
            }
          this->Erase();
          for(int i = 0; i < numTemp; ++i)
          {
                this->AddElement(tempValues[i]);
          }
        
        };
        
        void Switch()
        {
            Set * Z = A;
            A = B;
            B = Z;
            Z = NULL;
        };

        virtual int &operator[](int i) = 0;            
        virtual void Erase() = 0;
        virtual void DisplaySetContents() = 0;
        virtual void AddElement(int Element) = 0; 
        virtual int Size() = 0;
        virtual ~Set()
        {
            if(A != NULL) //At least some A's are guaranteed to be null, since each A has an A has an A, etc.
            {
                delete A;
            }
            if(B != NULL)
            {
                delete B;
            }
        }
        
        virtual Set& operator=(Set& other)
        {
            A = other.A;
            B = other.B; 
            return *this;
        }
};

//Derived class of Set that uses an OrderedCollections to represent a set.
class SetAsOC: public Set
{
    public:
        OrderedCollection * theCollection;

        SetAsOC()
        {
            theCollection = new OrderedCollection;
        }       
        
        void Erase()
        {
            delete A;
            A = new SetAsOC;
        };
        
       void AddElement(int Element)
        {
            dynamic_cast<SetAsOC*>(A)->theCollection->Add(Element);
        }; 
        
        void DisplaySetContents()
        {
            dynamic_cast<SetAsOC*>(A)->theCollection->displaySetContents();
            dynamic_cast<SetAsOC*>(B)->theCollection->displaySetContents();
        };        
        
       int &operator[](int i)
        {
            return theCollection->returnAtLoc(i);
        } 

        SetAsOC& operator=(Set& other)
        {
            Set::operator =(other);
            try
            {
               *(theCollection) = *(dynamic_cast<SetAsOC&>(other).theCollection);
            }catch(std::exception const& e){}
            return *this;
        } 
        
        virtual SetAsOC& operator=(SetAsOC& other)
        {
            Set::operator =(other);
            theCollection = other.theCollection;
            return *this;
        }       
        
       int Size()
        {
            int wanted = theCollection->returnSize();
            return wanted;
        }
       virtual ~SetAsOC()
        {
          delete theCollection;
        }
        

};

//Derived Class of Set that a Linked List to represent a set.
class SetAsList: public Set
{
    public:
        LinkedList * theList;
        
        SetAsList()
        {
            theList = new LinkedList;
        }
        
        void Erase()
        {
            delete A;
            A = new SetAsList;
        };

        void DisplaySetContents()
        {
            dynamic_cast<SetAsList*>(A)->theList->displaySetContents();
            dynamic_cast<SetAsList*>(B)->theList->displaySetContents();
        };
        
        void AddElement(int Element)
        {
            dynamic_cast<SetAsList*>(A)->theList->Add(Element);
        };

        int &operator[](int i)
        {
            return theList->returnAtLoc(i);
        }         
        
        int Size()
        {
            int wanted = theList->returnSize();       
            return wanted;
        }
        
       virtual ~SetAsList()
        {
          delete theList;
        } 
        
        SetAsList& operator=(Set& other)
        {
            Set::operator =(other);
            try
            {
                *(theList) = *(dynamic_cast<SetAsList&>(other).theList);
            }catch(std::exception const& e){}
            
            return *this;
        } 
        
        virtual SetAsList& operator=(SetAsList& other)
        {
            Set::operator =(other);
            theList = other.theList;

            return *this;
        } 
        

};

int main()
{
    char aChar = 'z';
    int anInt = 35505;
    Set * theManager = NULL;
    
    bool initalized = false;
    while(aChar != 'q')
    {
        cout << "Please Input a command:" << endl;
        cin >> aChar;
        aChar = tolower(aChar);
        
        if(aChar == 'l')
        {
            delete theManager;
            theManager = new SetAsList;
            theManager->A = new SetAsList;
            theManager->B = new SetAsList;
            initalized = true;
        }
        
        if(aChar == 'o')
        {
            delete theManager;
            theManager = new SetAsOC;
            theManager->A = new SetAsOC;
            theManager->B = new SetAsOC;           
            initalized = true;
        }
        
        if(initalized == true)
        {
            if(aChar == 'e')
            {
                theManager->Erase();
            }
            
            if(aChar == 's')
            {
                theManager->Switch();
            }  
            
            if(aChar == 'c')
            {
                *(theManager->B) = *(theManager->A);
            }  

            if(aChar == 'd')
            {
                theManager->DisplaySetContents();
            }   

            if(aChar == 'u')
            {
                theManager->Union();
            }            

            if(aChar == 'i')
            {
                theManager->intersection();
            } 

            if(aChar == 'a')
            {
                cout << "Please enter an integer:" << endl;
                cin >> anInt;
                theManager->AddElement(anInt);
            }              
        
        }       
    }
    
    delete theManager;
    return 0;
}

