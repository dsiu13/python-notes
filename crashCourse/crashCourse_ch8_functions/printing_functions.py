def printing_models():
    
    unprinted = ['d20', 'tiny robot', '3DS']
    completed = []

    while unprinted:
      current_designs = unprinted.pop()
      print(current_designs + " printed")
      completed.append(current_designs)

    for complete in completed:
      print(completed)
