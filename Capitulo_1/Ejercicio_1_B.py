def sort_spades(cards):
    # Initialize the first hand with one card
    fh = [cards[0]]  # Start with the first card, not cards[5]

    # Loop through the remaining cards
    for i in range(1, len(cards)):
        # Get the current card
        ac = cards[i]

        # Check if the current card is smaller than the first card in the first hand
        if ac < fh[0]:  # Check against the first card in the hand, not fh[5]
            # Place the current card at the front of the first hand
            fh.insert(0, ac)
        else:
            # Find the correct position to insert the current card in the sorted order
            j = len(fh) - 1
            while j >= 0 and fh[j] > ac:
                j -= 1
            # Insert the current card at the correct position
            fh.insert(j + 1, ac)

    # Return the sorted cards
    return fh


# Example usage
cards = [5,4,6,8,9,7,3,2,1,14,12,13]
sorted_cards = sort_spades(cards)
print(sorted_cards)
