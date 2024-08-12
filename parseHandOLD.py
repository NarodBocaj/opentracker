#text to the right of hand result has the amount gained
#all text next to position except followed by "in chips" is a bet
import os
import re





def parseHands(directory):
    hand_count = 0
    bb = "someinput"
    bb_gain = 0
    session_count = 0
    spent_in_hand = 0
    win_in_hand = 0

    hands = [] #This should be a list of hand objects

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)


        with open(file_path, 'r') as file:
            session_count += 1
            session_hand_count = 0
            session_gain = 0
            #create hand object
            for line in file:
                #igntionHandParse(line, handobject)
                if "Ignition Hand" in line:
                    session_hand_count += 1
                    spent_in_hand = 0
                    win_in_hand = 0
                    hand_number = re.search(r'Hand #(\d+)', line)
                    hand_number = hand_number.group(1)
                
                if ": Big blind" in line:
                    temp = re.findall(r'\d+\.\d+', line)
                    bb = float(temp[0])
                
                if "[ME]" in line and "in chips" in line:
                    temp = re.findall(r'\d+\.\d+', line)
                    if not temp:
                        temp = re.findall(r'\d+', line)
                    if len(temp) > 1:
                        chip_count = float(temp[1])
                    else:
                        chip_count = float(temp[0])
                    # print(f"Sitting on ${chip_count} as of hand: {hand_number}")

                if "[ME]" in line and "in chips" not in line and "$" in line and "Hand result" not in line and "Return uncalled" not in line and "Table deposit" not in line:
                    temp = re.findall(r'\d+\.\d+', line)
                    if not temp:
                        temp = re.findall(r'\d+', line)
                    spent_in_hand += float(temp[0])
                
                if "[ME]" in line and "Return uncalled" in line:
                    temp = re.findall(r'\d+\.\d+', line)
                    if not temp:
                        temp = re.findall(r'\d+', line)
                    spent_in_hand -= float(temp[0])
                
                if "Hand result" in line and "[ME]" in line:
                    temp = re.findall(r'\d+\.\d+', line)
                    if not temp:
                        temp = re.findall(r'\d+', line)
                    win_in_hand += float(temp[0]) - spent_in_hand
                    session_gain += win_in_hand
                    bb_gain += win_in_hand / bb
                    # print(f'Won hand, Netted {win_in_hand:.2f} in hand for a total gain/loss {bb_gain:.2f} in BB so far as of hand number: {hand_number}')
                    spent_in_hand = 0
                
                if "SUMMARY" in line and spent_in_hand:
                    win_in_hand = -spent_in_hand
                    session_gain += win_in_hand
                    bb_gain += win_in_hand / bb
                    # print(f'Lost hand, Netted {win_in_hand:.2f} in hand for a total gain/loss {bb_gain:.2f} in BB so far as of hand number: {hand_number}')
            print(f"Session gain is ${session_gain:.2f} with {session_hand_count} hands")
            hand_count += session_hand_count
    print(f"\nPlayed a total of {hand_count} hands in {session_count} sessions")
    print(f"Won/loss {bb_gain:.2f}BB for a total net of ${bb_gain * bb:.2f}")
    print(f"\nWinrate of {(bb_gain * 100)/hand_count:.2f}BB/100")


if __name__ == "__main__":
   directory = "handhistory"
    # directory = "test_handhistory"
    # directory = "example_handhistory"
    # directory = "test1"
   parseHands(directory)