def calcWinrateper100bb(hands):
    cumulativeBB = 0
    for hand in hands:
        cumulativeBB += hand.profit_from_hand / hand.bb_stakes
    print(f'Winrate of {(cumulativeBB * 100) / len(hands):.2f}BB/100')
    return (cumulativeBB * 100) / len(hands)

def handStats(hands):
    cumulativeProfit = 0
    profitWShowdown = 0
    profitWOShowdown = 0
    profitList = []
    bbprofitList = []
    noSDprofitList = []
    SDprofitList = []
    for hand in hands:
        cumulativeProfit += hand.profit_from_hand
        profitList.append(cumulativeProfit)
        bbprofitList.append(cumulativeProfit / hand.bb_stakes)
        if hand.showdown:
            profitWShowdown += hand.profit_from_hand
        else:
            profitWOShowdown += hand.profit_from_hand
        SDprofitList.append(profitWShowdown)
        noSDprofitList.append(profitWOShowdown)

    print(f'Cumulative profit is ${cumulativeProfit:.2f}\n Won ${profitWShowdown:.2f} at showdown and Won ${profitWOShowdown:.2f} w/o showdown')
    return profitList, SDprofitList, noSDprofitList, bbprofitList