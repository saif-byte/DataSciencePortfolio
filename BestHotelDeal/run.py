from booking.booking import Booking
with Booking() as bot:
    
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.search_dest(dest = 'newyork')
    bot.select_date(check_in='2022-06-08' , check_out='2022-07-09')
    bot.select_adults(count =4)
    bot.select_children(ages = [4,7] , count = 2)
    bot.select_room(2)
    bot.click_search()

    bot.filtration()
    bot.refresh()
    bot.hotel_result()