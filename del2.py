import Leap, sys, thread, time
from random import randint
import matplotlib.pyplot as plt
import pickle
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.patches as mpatches
import matplotlib

def main():
    

    database = pickle.load(open('userData/database.p','rb'))
    
    
    
    userName = raw_input('Please enter your name: ')
    if userName in database:
        database[userName]['logins'] += 1
        
        print 'welcome back ' + userName + '.'
    else:
        database[userName] = {}
        database[userName]['logins'] = 1
        database[userName]['attempted 0'] = 0
        database[userName]['attempted 1'] = 0
        database[userName]['attempted 2'] = 0
        database[userName]['attempted 3'] = 0
        database[userName]['attempted 4'] = 0
        database[userName]['attempted 5'] = 0
        database[userName]['attempted 6'] = 0
        database[userName]['attempted 7'] = 0
        database[userName]['attempted 8'] = 0
        database[userName]['attempted 9'] = 0
        database[userName]['success 0'] = 0
        database[userName]['success 1'] = 0
        database[userName]['success 2'] = 0
        database[userName]['success 3'] = 0
        database[userName]['success 4'] = 0
        database[userName]['success 5'] = 0
        database[userName]['success 6'] = 0
        database[userName]['success 7'] = 0
        database[userName]['success 8'] = 0
        database[userName]['success 9'] = 0
        
        
        print 'welcome ' + userName + '.'
    
    if (database[userName]['attempted 0'] == 0):
        successPercentage0 = 0
    else:
        successPercentage0 = (float(database[userName]['success 0']) / float(database[userName]['attempted 0'])) * 100

    if (database[userName]['attempted 1'] == 0):
        successPercentage1 = 0
    else:
        successPercentage1 = (float(database[userName]['success 1']) / float(database[userName]['attempted 1'])) * 100
    if (database[userName]['attempted 2'] == 0):
        successPercentage2 = 0
    else:
        successPercentage2 = (float(database[userName]['success 2']) / float(database[userName]['attempted 2'])) * 100

    if (database[userName]['attempted 3'] == 0):
        successPercentage3 = 0
    else:
        successPercentage3 = (float(database[userName]['success 3']) / float(database[userName]['attempted 3'])) * 100

    if (database[userName]['attempted 4'] == 0):
        successPercentage4 = 0
    else:
        successPercentage4 = (float(database[userName]['success 4']) / float(database[userName]['attempted 4'])) * 100

    if (database[userName]['attempted 5'] == 0):
        successPercentage5 = 0
    else:
        successPercentage5 = (float(database[userName]['success 5']) / float(database[userName]['attempted 5'])) * 100

    if (database[userName]['attempted 6'] == 0):
        successPercentage6 = 0
    else:
        successPercentage6 = (float(database[userName]['success 6']) / float(database[userName]['attempted 6'])) * 100

    if (database[userName]['attempted 7'] == 0):
        successPercentage7 = 0
    else:
        successPercentage7 = (float(database[userName]['success 7']) / float(database[userName]['attempted 7'])) * 100

    if (database[userName]['attempted 8'] == 0):
        successPercentage8 = 0
    else:
        successPercentage8 = (float(database[userName]['success 8']) / float(database[userName]['attempted 8'])) * 100

    if (database[userName]['attempted 9'] == 0):
        successPercentage9 = 0
    else:
        successPercentage9 = (float(database[userName]['success 9']) / float(database[userName]['attempted 9'])) * 100


    #print database
    
    pickle.dump(database,open('userData/database.p','wb'))
    
    clf = pickle.load(open('userData/classifier.p','rb'))
    testData = np.zeros((1,30),dtype='f')
    controller = Leap.Controller()
    matplotlib.interactive(True)


    fig5 = plt.figure(figsize = (4,4))
    ax5 = fig5.add_subplot(111)
    fig2 = plt.figure(figsize = (5,5))
    
    ax2 = fig2.add_subplot(111)
    if (database[userName]['logins'] == 1):
        image = plt.imread('all.png')
        plt.imshow(image)
        plt.axis('off')
    else:
        ax2.text(0.1, .1, 'Personal LeaderBoard\nDigit\n0: ' + str(successPercentage0) + ' %\n1: ' + str(successPercentage1) + ' %\n2: ' + str(successPercentage2) + ' %\n3: ' + str(successPercentage3) + ' %\n4: ' + str(successPercentage4) + ' %\n5: ' + str(successPercentage5) + ' %\n6: ' + str(successPercentage6) + ' %\n7: ' + str(successPercentage7) + ' %\n8: ' + str(successPercentage8) +  ' %\n9: ' + str(successPercentage9) + ' %')
    plt.draw()
    fig3 = plt.figure(figsize = (5,5))
    ax3 = fig3.add_subplot(111)
    plt.draw()
    fig = plt.figure( figsize = (8,6) )
    ax = fig.add_subplot( 111, projection = '3d')
    
    ax.set_xlim(-260,260)
    ax.set_ylim(-100,265)
    ax.set_zlim(0,590)
    ax.view_init(azim=90)
    counter = 0
    incorrectCounter = 0
    
    plt.draw()
    while (True):
        frame = controller.frame()
        lines = []
        counter += 1
        if (counter == 1):
            plt.figure(fig3.number)
            plt.clf()
            random = randint(0,9)
            print "please sign the digit " + str(random)
            ax3 = fig3.add_subplot(111)
            image = plt.imread(str(random) + '.png')
            plt.imshow(image)
            plt.axis('off')
            plt.draw()
        if (len(frame.hands) > 0):
            k = 0
            hand = frame.hands[0]
            for i in range(0,5):
                finger = frame.fingers[i]
                for j in range(0,4):
                    bone = finger.bone(j)
                    boneBase = bone.prev_joint
                    boneTip = bone.next_joint
            
            
                    xBase = boneBase[0]
                    yBase = boneBase[1]
                    zBase = boneBase[2]
                    xTip = boneTip[0]
                    yTip = boneTip[1]
                    zTip = boneTip[2]
                    lines.append(ax.plot([-xBase,-xTip],[zBase,zTip],[yBase,yTip],'r'))
                    if ((j ==0) | (j==3)):
                        testData[0,k] = xTip
                        testData[0,k+1] = yTip
                        testData[0,k+2] = zTip
                        k = k+3
            
            testData = CenterData(testData)
            predictedClass = clf.predict(testData)
            
            
            if (random == predictedClass):
                counter = 0
                database[userName]['attempted ' + str(random)] += 1
                database[userName]['success ' +str(random)] += 1
                if (random == 0):
                    successPercentage0 = (float(database[userName]['success 0']) / float(database[userName]['attempted 0'])) * 100
                elif (random == 1):
                    successPercentage1 = (float(database[userName]['success 1']) / float(database[userName]['attempted 1'])) * 100

                elif(random == 2):
                    successPercentage2 = (float(database[userName]['success 2']) / float(database[userName]['attempted 2'])) * 100
                    
                elif(random == 3):
                    successPercentage3 = (float(database[userName]['success 3']) / float(database[userName]['attempted 3'])) * 100

                elif(random == 4):
                    successPercentage4 = (float(database[userName]['success 4']) / float(database[userName]['attempted 4'])) * 100
                    
                elif(random == 5):
                    successPercentage5 = (float(database[userName]['success 5']) / float(database[userName]['attempted 5'])) * 100
                    
                elif(random == 6):
                    successPercentage6 = (float(database[userName]['success 6']) / float(database[userName]['attempted 6'])) * 100
                    
                elif(random == 7):
                    successPercentage7 = (float(database[userName]['success 7']) / float(database[userName]['attempted 7'])) * 100
                    
                elif(random == 8):
                    successPercentage8 = (float(database[userName]['success 8']) / float(database[userName]['attempted 8'])) * 100
                   
                elif(random == 9):
                    successPercentage9 = (float(database[userName]['success 9']) / float(database[userName]['attempted 9'])) * 100
                
                plt.figure(fig2.number)
                plt.clf()
                ax2 = fig2.add_subplot(111)
                ax2.text(0.1, .1, 'Personal LeaderBoard\nDigit\n0: ' + str(successPercentage0) + ' %\n1: ' + str(successPercentage1) + ' %\n2: ' + str(successPercentage2) + ' %\n3: ' + str(successPercentage3) + ' %\n4: ' + str(successPercentage4) + ' %\n5: ' + str(successPercentage5) + ' %\n6: ' + str(successPercentage6) + ' %\n7: ' + str(successPercentage7) + ' %\n8: ' + str(successPercentage8) + ' %\n9: ' + str(successPercentage9) + ' %')
            
                plt.draw()
                plt.figure(fig5.number)
                plt.clf()
                ax5 = fig5.add_subplot(111)
                image = plt.imread('thumbsup.png')
                plt.imshow(image)
                plt.axis('off')
                plt.draw()
                
                incorrectCounter = 0
            elif (random != predictedClass):
                database[userName]['attempted ' + str(random)] += 1
                if (random == 0):
                    successPercentage0 = (float(database[userName]['success 0']) / float(database[userName]['attempted 0'])) * 100
                elif (random == 1):
                    successPercentage1 = (float(database[userName]['success 1']) / float(database[userName]['attempted 1'])) * 100

                elif(random == 2):
                    successPercentage2 = (float(database[userName]['success 2']) / float(database[userName]['attempted 2'])) * 100
                    
                elif(random == 3):
                    successPercentage3 = (float(database[userName]['success 3']) / float(database[userName]['attempted 3'])) * 100

                elif(random == 4):
                    successPercentage4 = (float(database[userName]['success 4']) / float(database[userName]['attempted 4'])) * 100
                    
                elif(random == 5):
                    successPercentage5 = (float(database[userName]['success 5']) / float(database[userName]['attempted 5'])) * 100
                    
                elif(random == 6):
                    successPercentage6 = (float(database[userName]['success 6']) / float(database[userName]['attempted 6'])) * 100
                    
                elif(random == 7):
                    successPercentage7 = (float(database[userName]['success 7']) / float(database[userName]['attempted 7'])) * 100
                    
                elif(random == 8):
                    successPercentage8 = (float(database[userName]['success 8']) / float(database[userName]['attempted 8'])) * 100
                   
                elif(random == 9):
                    successPercentage9 = (float(database[userName]['success 9']) / float(database[userName]['attempted 9'])) * 100
                
                plt.figure(fig2.number)
                plt.clf()
                ax2 = fig2.add_subplot(111)
                ax2.text(0.1, .1, 'Personal LeaderBoard\nDigit\n0: ' + str(successPercentage0) + ' %\n1: ' + str(successPercentage1) + ' %\n2: ' + str(successPercentage2) + ' %\n3: ' + str(successPercentage3) + ' %\n4: ' + str(successPercentage4) + ' %\n5: ' + str(successPercentage5) + ' %\n6: ' + str(successPercentage6) + ' %\n0: ' + str(successPercentage7) + ' %\n7: ' + str(successPercentage8) + ' %\n0: ' + str(successPercentage8) + ' %\n9: ' + str(successPercentage9) + ' %')

                plt.draw()
                plt.figure(fig5.number)
                plt.clf()
                ax5 = fig5.add_subplot(111)
                image = plt.imread('X.png')
                plt.imshow(image)
                plt.axis('off')
                plt.draw()
                incorrectCounter+=1
                if (incorrectCounter == 5):
                    counter = 0
                    incorrectCounter = 0
            plt.figure(fig.number)
            plt.draw()
            pickle.dump(database,open('userData/database.p','wb'))
            while ( len(lines) > 0):
                ln = lines.pop()
                ln.pop(0).remove()
                del ln
                ln = []
        
def CenterData(X):
    allXCoordinates = X[0,::3]
    meanValue = allXCoordinates.mean()
    X[0,::3] = allXCoordinates - meanValue
    allYCoordinates = X[0,1::3]
    meanValue = allYCoordinates.mean()
    X[0,1::3] = allYCoordinates - meanValue
    allZCoordinates = X[0,2::3]
    meanValue = allZCoordinates.mean()
    X[0,2::3] = allZCoordinates - meanValue
    return X

main()
        
    
