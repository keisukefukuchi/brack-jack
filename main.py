# -*- coding: utf-8 -*-
import random

reGame = 2
game_count = 0

while reGame == 2:
    if game_count != 0:
        print('持ち金は、' + str(player_money) + 'です')
    else:
        player_money = input('持ち金を決めてください\n')

    bet_money = input('掛け金を決めてください\n')

    print('持ち金 : ' + str(player_money))
    print('掛け金 : ' + str(bet_money))

    print('それでは、ゲームを始めます。')

    deck = []
    symbol_list = ['H', 'S', 'D', 'C']
    for symbol in symbol_list:
        for number in range(1, 14):
            # 11以上と1は置き換え
            if number == 1:
                card = symbol + '-' + 'A'
            elif number == 11:
                card = symbol + '-' + 'J'
            elif number == 12:
                card = symbol + '-' + 'Q'
            elif number == 13:
                card = symbol + '-' + 'K'
            else:
                # 10以下ならそのまま
                card = symbol + '-' + str(number)
            deck.append(card)
    random.shuffle(deck)

    # 初期のカードの取得
    player_card = []
    dealer_card = []
    player_card.append(deck[0])
    player_card.append(deck[2])
    dealer_card.append(deck[1])
    dealer_card.append(deck[3])


    player_num = 0
    dealer_num = 0


    # カードから数値を計算
    for card in player_card:
        num = []
        num = card.split('-')
        if num[1] == 'A':
            num[1] = '11'
        elif num[1] == 'J' or num[1] == 'Q' or num[1] == 'K':
            num[1] = '10'
        player_num += int(num[1])

    for card in dealer_card:
        num = []
        num = card.split('-')
        if num[1] == 'A':
            num[1] = '11'
        elif num[1] == 'J' or num[1] == 'Q' or num[1] == 'K':
            num[1] = '10'
        dealer_num += int(num[1])

    count = 0
    for reCard in range(4,53):
        # プレイヤーのカードの合計値が21以上の時の判定する
        if player_num > 21:
            player_num = 0
            for card in player_card:
                num = []
                num = card.split('-')
                if num[1] == 'A':
                    print('プレイヤーのカード : ' + str(player_card))
                    print('プレイヤーの数 : ' + str(player_num))
                    change = input('バーストしました。Aの数を変更しますか？[no = 1 or yes = 2]\n')
                    if change == 2:
                        num[1] = '1'
                    else:
                        num[1] = '11'            
                elif num[1] == 'J' or num[1] == 'Q' or num[1] == 'K':
                    num[1] = '10'
                player_num += int(num[1])

        print('プレイヤーのカード : ' + str(player_card))
        print('プレイヤーの数 : ' + str(player_num))

        # バーストした時
        if player_num > 21:
            print('バーストしました。カード変更をできません。')
            break
        # ブラックジャックした時
        elif player_num == 21:
            print('ブラックジャックです。カード変更を行いません。')
            break
        # それ以外
        else:
            reHit = input('もう一枚もらいますか？[no = 1 or yes = 2]\n')
            if reHit == 2:
                re_player_card = []
                player_card.append(deck[reCard])
                re_player_card.append(deck[reCard])
                for card in re_player_card:
                    num = []
                    num = card.split('-')
                    if num[1] == 'A':
                        num[1] = '11'
                    elif num[1] == 'J' or num[1] == 'Q' or num[1] == 'K':
                        num[1] = '10'
                    player_num += int(num[1])
            else:
                break
        count += 1

    print('カードをこちらでセットします。')

    print('プレイヤーのカード : ' + str(player_card))
    print('プレイヤーの数 : ' + str(player_num))

    # ディーラー16以下の時の処理
    for reCard in range(4+count,53):
        if dealer_num <= 16:
            re_dealer_card = []
            dealer_card.append(deck[reCard])
            re_dealer_card.append(deck[reCard])
            for card in re_dealer_card:
                num = []
                num = card.split('-')
                if num[1] == 'A':
                    num[1] = '11'
                elif num[1] == 'J' or num[1] == 'Q' or num[1] == 'K':
                    num[1] = '10'
                dealer_num += int(num[1])
        else:
            break

    print('ディーラーのカード : ' + str(dealer_card))
    print('ディーラーの数 : ' + str(dealer_num))

    # 条件
    #プレイヤーとディーラーが引き分け
    if (player_num == 21 and dealer_num == 21) or (player_num > 21 and dealer_num > 21):
        print('引き分けです。掛け金を返金します。')

    #プレイヤーが勝ち、ディーラーが負け
    elif (player_num == 21 and dealer_num > 21) or (player_num == 21 and dealer_num < 21):
        print('ブラックジャックです。プレイヤーの勝利です。')
        print('掛金を獲得します。')
        player_money += bet_money

    elif player_num < 21 and dealer_num > 21:
        print('ディーラーがバーストしました。プレイヤーの勝利です。')
        print('掛金を獲得します。')
        player_money += bet_money

    #プレイヤーが負け、ディーラーが勝ち
    elif (player_num > 21 and dealer_num == 21) or (player_num > 21 and dealer_num < 21):
        print('バーストしました。ディーラーの勝利です。')
        print('掛金を没収します。')
        player_money -= bet_money

    elif player_num < 21 and dealer_num == 21:
        print('ディーラーがブラックジャックです。ディーラーの勝利です。')
        print('掛金を没収します。')
        player_money -= bet_money

    #その他、プレイヤーとディーラーが21より下の時
    else:
        if player_num == dealer_num:
            print('引き分けです。掛け金を返金します。')
        elif player_num > dealer_num:
            print('プレイヤーの勝利です。')
            print('掛金を獲得します。')
            player_money += bet_money
        else:
            print('ディーラーの勝利です。')
            print('掛金を没収します。')
            player_money -= bet_money


    print('ゲームを終了します。')
    print('プレイヤーの金額 : ' + str(player_money))

    if player_money == 0:
        print('ゲームを終了します')
        reGame = 1
    else:
        reGame = input('ゲームを続けますか？[no = 1 or yes = 2]\n')
        if reGame == 2:
            print('ゲームを続けます。')
            game_count += 1
        else:
            print('ゲームを終了します。')
