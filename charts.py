import matplotlib.pyplot as plt

def plotWinRate(profitList, SDprofitList, noSDprofitList):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(profitList) + 1), profitList, label='My C Won', color='green')
    plt.plot(range(1, len(SDprofitList) + 1), SDprofitList, label='Money Won With Showdown', color='blue')
    plt.plot(range(1, len(noSDprofitList) + 1), noSDprofitList, label='Money Won Without Showdown', color='red')
    
    plt.title('My Currency Won in USD over Hands Played')
    plt.xlabel('Hands Played')
    ax = plt.gca()
    ax.yaxis.set_label_position('right')
    ax.yaxis.tick_right()
    plt.ylabel('$', labelpad=20)

    plt.legend(loc='upper left')
    plt.xlim(left=1, right=len(profitList))
    plt.margins(x=0)
    plt.grid(True)
    plt.show()