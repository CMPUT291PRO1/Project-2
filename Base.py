#
#    Copyright (C) {2015}  {Nicholas Carroll}

#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License along
#    with this program; if not, write to the Free Software Foundation, Inc.,
#    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

#import bsddb3 as bsddb

import sys;
import Create

option = sys.argv[1]

while(True):
    
    print("\n1. Create and populate a database")
    print("2. Retrieve records with a given key")
    print("3. Retrieve records with a given data")
    print("4. Retrieve records with a given range of key values")
    print("5. Destroy the database")
    print("6. Quit \n")
    selection = raw_input("Please select your program number:\n")
    
    try:
        digit = int(selection)
        if digit == 1:
            Create.progOption(option)
        elif digit == 2:
            pass
        elif digit == 3:
            pass
        elif digit == 4:
            pass
        elif digit == 5:
            pass
        elif digit == 6:
            break
        else:
            print("Must be between 1 and 6")
                
    except ValueError:
            print("Please enter a digit or 'exit'")
    
                 
