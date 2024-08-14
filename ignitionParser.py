from poker_stuff import Hand, Session
import re


def ZoomParser(file: str, handList: list[Hand], sess: Session):
    tempHand = Hand()
    for line in file:
        if "Ignition Hand" in line:
            hand_number = re.search(r'Hand #(\d+)', line)
            hand_number = hand_number.group(1)
            tempHand.handNumber = hand_number

        if ": Big blind" in line:
            temp = re.findall(r'\d+\.\d+', line)
            tempHand.bb_stakes = float(temp[0])
            sess.bb_stakes = float(temp[0])

        if "[ME]" in line and "Card dealt to a spot" in line:
            pos_match = re.match(r'(.*)\s+\[ME\]', line)
            pos = pos_match.group(1) if pos_match else None
            tempHand.pos = pos
            cards_match = re.search(r'\[(?!ME\])([^\]]+)\]', line)
            cards = cards_match.group(1) if cards_match else None
            tempHand.heroHand = cards

        if "[ME]" in line and "in chips" in line:
            temp = re.findall(r'\d+\.\d+', line)
            if not temp:
                temp = re.findall(r'\d+', line)
            if len(temp) > 1:
                chip_count = float(temp[1])
            else:
                chip_count = float(temp[0])
            tempHand.startingChips = chip_count
            # print(f"Sitting on ${chip_count} as of hand: {hand_number}")

        if "[ME]" in line and "in chips" not in line and "$" in line and "Hand result" not in line and "Return uncalled" not in line and "Table deposit" not in line:
            temp = re.findall(r'\d+\.\d+', line)
            if not temp:
                temp = re.findall(r'\d+', line)
            tempHand.profit_from_hand -= float(temp[0])

        if "[ME]" in line and "Return uncalled" in line:
            temp = re.findall(r'\d+\.\d+', line)
            if not temp:
                temp = re.findall(r'\d+', line)
            tempHand.profit_from_hand += float(temp[0])

        if "Return uncalled" in line:
            tempHand.showdown = False

        if "Hand result" in line and "[ME]" in line:
            temp = re.findall(r'\d+\.\d+', line)
            if not temp:
                temp = re.findall(r'\d+', line)
            tempHand.profit_from_hand += float(temp[0])

            # print(f'Won hand, Netted {win_in_hand:.2f} in hand for a total gain/loss {bb_gain:.2f} in BB so far as of hand number: {hand_number}')


        if "SUMMARY" in line:
            handList.append(tempHand)
            sess.sessionHands.append(tempHand)
            sess.sessionProfit += tempHand.profit_from_hand
            tempHand = Hand()
    print(f'Session profit was ${sess.sessionProfit:.2f} in {len(sess.sessionHands)} hands')
