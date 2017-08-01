print("================================================\n\
1. print all buildings \n\
2. print all performances \n\
3. print all audiences \n\
4. insert a new building \n\
5. remove a building \n\
6. insert a new performance \n\
7. remove a performance \n\
8. insert a new audience \n\
9. remove a audience \n\
10. assign a performance to a building \n\
11. book a performances \n\
12. print all performances wich assigned at a building \n\
13. print all audiences who booked for a performance \n\
14. print ticket booking status of a performance \n\
15. exit \n\
================================================")

number = eval(input("Select your action: "))
sqls = ["select * from buildings"]
