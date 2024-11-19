def restock_inventory(available_items, inventory_records, current_day):


    restocked_units = 0

    if current_day == 0: # first day starts with full restock
        restocked_units = 2000
        inventory_records.append([current_day, 0, restocked_units, available_items])  # append the first days record

    if current_day % 7 == 0: # restock every 7 days
    
        restocked_units = 2000 - available_items # restock the available items to 2000 units
        available_items = 2000 
        inventory_records.append([current_day, 0, restocked_units, available_items])      

    return available_items  

