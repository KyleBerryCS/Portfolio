/*This classes implements an Ordered Collection architecture, with the array doubling in size as needed. 
specifically one that does not accept duplicate values.
This particular Ordered Collection architecture also overloads the = operator.
*/


#include <stdio.h>
#include <iostream>
using namespace std;


class OrderedCollection
{
    public:
        int * theArr;
        int size;
        int maxSize;
        
        OrderedCollection()
        {
            theArr = new int[100];
            maxSize = 100;
            size = 0;
        }

        void doubleSize()
        {
            maxSize = maxSize * 2;
            int * newArr = new int[(maxSize)];
            for(int i = 0; i < size; ++i)
            {
                newArr[i] = theArr[i];
            }
            delete[] theArr;
            theArr = newArr;
        }        
        
        void displaySetContents()
        {
          for(int i = 0; i < size; ++i)
          {
                cout << theArr[i] << " ";
          }
          cout << endl;
        };
 
         //First checks to see if the element is already in the Ordered Collection (if so, it does nothing)
        void Add(int element)
        {
            bool found = false;
            for(int i = 0; i < size; ++i)
            {
                if(theArr[i] == element)
                {
                    found = true;
                    break;
                }
            }
            
            if(found == false)
            {
                if(size >= maxSize)
                {
                    doubleSize();  
                }
                size = size + 1;
                theArr[(size-1)] = element;
            }
        };

        //Returns the address of the int at the location in the OrderedCollection.
        int& returnAtLoc(int loc)
        {        
          if(loc < size)
          {
                return theArr[loc];
          }
          
          cout << "No value at that location! See returnAtLoc method of class OrderedCollection" << endl;
          return theArr[0];        
        }         
        
        int returnSize()
        {
            return size; 
        } 

        ~OrderedCollection()
        {
            delete[] theArr;
        }       

        OrderedCollection &operator=(OrderedCollection & other)
        {
            maxSize = other.maxSize;
            size = 0;
            
            delete[] theArr;
            theArr = new int[maxSize];  
            int otherSize = other.size;
            for(int i = 0; i < otherSize; ++i)
            {
              Add((other.theArr[i]));
            }         
            return *this;
        }   
        
};






