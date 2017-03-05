def main(): #{
    board = "H,H,H,H,H,T,T,T,T,T" #//I'll be using commas as delineators
    boardArray = board.split(',') #//Remove said delineators
    counter = 0
    gapLocation = 0
    needToFillGap = False
    while (counter < 5): #{

        #//Start Pre-Processing
        firstValidSelection = False
        secondValidSelection = False
        print ("Turn: ", counter+1)
        board = board.replace(',', '')
 
        gapLocation = board.find('-') 
        if (gapLocation != -1): #{ //Hyphen has been found, meaning that the next move must fill the gap.
            print ("Gap location:" , gapLocation)
            needToFillGap = True
        #}
        else: #{ //If there are no hyphens, that means that the only valid moves are placing the two coins on either extreme end of the coin
            needToFillGap = False
        #}
        #//End Preprocessing


        #Start getting valid input
        while firstValidSelection == False: #{
            print (board)
            firstSelection = input()
            firstPos = len(firstSelection)
            if ((boardArray[firstPos] != ' ' and boardArray[firstPos + 1] != ' ') and (boardArray[firstPos] != '-' and boardArray[firstPos +1] != '-')): #{
                firstValidSelection = True
            #}
            else: #{
                print("Invalid selection, please try again.")
                firstValidSelection = False
            #}
        #}
                
        while secondValidSelection == False: #{
            print (board)
            secondSelection = input()
            secondPos = len(secondSelection)
            
            if needToFillGap == True: #{
                print(needToFillGap)
                if secondPos == gapLocation: #{
                    secondValidSelection = True
                #}
                else: #{
                    print ("Invalid selection, please try again")
                    secondValidSelection = False
                #}
            #}
                    
            if needToFillGap == False: #{
                if secondPos == 0: #{
                    secondValidSelection = True
                #}
                elif secondPos > 0 and (len(boardArray) < secondPos): #{
                    secondValidSelection = True
                #}
                else: #{
                    print ("Invalid selection, please try again.")
                    secondValidSelection = False
                #}
            #}
                    
        if needToFillGap == True: #{
            boardArray[secondPos] = boardArray[firstPos]
            boardArray[secondPos+1] = boardArray[firstPos+1]
            boardArray[firstPos] = ' '
            boardArray[firstPos+1] = ' '
        #}

        else: #{
            if secondPos > len(boardArray): #{
                boardArray.append(boardArray[firstPos])
                boardArray.append(boardArray[firstPos+1])
                boardArray[firstPos] = '-'
                boardArray[firstPos+1] = '-'
            #}
                
            else: #{
                boardArray.insert(0, boardArray[firstPos+1])
                boardArray.insert(0, boardArray[firstPos])
                boardArray[firstPos] = '-'
                boardArray[firstPos+1] = '-'
            #}
                
        if needToFillGap == True: #{
            boardArray.remove(' ')
            boardArray.remove(' ')
        board = ",".join(boardArray)
        #}
        
        counter += 1
    #}
        
#}



if __name__ == '__main__': #{
    main()
#}
