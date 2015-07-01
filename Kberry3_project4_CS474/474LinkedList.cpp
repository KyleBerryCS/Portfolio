/*These classes (Node and LinkedList)implements a linked list architecture, 
specifically one that does not accept duplicate values.
This particular link list architecture also overloads the = operator.
*/

#include <stdio.h>
#include <iostream>
using namespace std;


class Node
{
    public:
        
        Node()
        {
            next = NULL;
        };
        
        void setValue(int anInt)
        {
            value = anInt;
        };
        
        void setNext(Node * aNode)
        {
            next = aNode;
        };
        
        int getValue()
        {
            return value;
        }
        
        Node * getNext()
        {
            return next;
        }
        
      /*  ~Node() //LinkedList handles deleting all of the nodes.
        {
            if(next != NULL)
            {
                delete next;
            }
        }*/
        
        Node * next;
        int value;
};

class LinkedList
{
    public:
        Node * Head;
        int theSize;
        
        LinkedList()
        {
            Head = NULL;
            theSize = 0;
        }

        void displaySetContents()
        {
          Node * current = Head;
          while(current != NULL)
          {
            cout << (current->getValue()) << " ";
            current = current->getNext();
          }
          cout << endl;
        };
        
        //First checks to see if the element is already in the list (if so, it does nothing)
        void Add(int element)
        {
          Node * current = Head;
          Node * formerCurrent = Head;
          bool found = false;
          while(current != NULL)
          {
                formerCurrent = current;
                if((current->getValue()) == element)
                {
                    found = true;
                    break;
                }
                current = current->getNext();
          }
          
          if(found == false)
          {
                Node * neoNode = new Node();
                neoNode->setValue(element);
                if(formerCurrent == NULL) //the list was empty
                {
                    Head = neoNode;
                }
                else
                {
                    formerCurrent->setNext(neoNode); 
                }
                theSize = theSize + 1;
          }
        };

        //Returns the address of the int at the location in the LinkedList.
        int& returnAtLoc(int loc)
        {
          Node * current = Head;
          int count = 0;
          while(count < loc && current != NULL)
          {
                current = current->getNext();
                ++count;
          }
          
          if(current != NULL)
          {
                return current->value;
          }
          
          cout << "Out of Bounds Error!  See LinkedList Class returnAtLoc method." << endl;
          return current->value;        
        }         
        
        int returnSize()
        {
            return theSize; 
        }
        
        //This method is called by the destructor to ensure all of the nodes are deleted
        //(Which is done recursively).
        void nestedDelete(Node * current)
        {
          if(current != NULL)
          {
            nestedDelete(current->getNext());
          }
          delete current;
        }
        
       ~LinkedList()
        {
          if(Head != NULL)
          {
            nestedDelete(Head);
          }
        } 

        LinkedList &operator=(LinkedList & other)
        {
            if(Head != NULL)
            {
                nestedDelete(Head);
            }
            Node * current = other.Head;
            int count = 0;
            while(current != NULL)
            {
                Add(current->getValue());
                current = current->getNext();
                ++count;
            }
            theSize = other.theSize;           
            return *this;
        }         
        
};



