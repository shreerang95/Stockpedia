import matplotlib.dates as mdates

def year_week_calculator(i_int_start_date,i_int_end_date,i_int_day,week1,week2,week3,week4,week5,week6):
    # print(mdates.num2date(i_int_start_date),mdates.num2date(i_int_end_date))
    week1_flag = 0
    week2_flag = 0
    week3_flag = 0
    week4_flag = 0
    week5_flag = 0
    week6_flag = 0

    i_int_date = i_int_start_date
    # print(mdates.num2date(i_int_date))

    while (i_int_date <= i_int_end_date):
        day=[]
        i_date = mdates.num2date(i_int_date)
        day.append(i_date)
        day_index = (i_date.weekday() + 1) % 7
        if(week1_flag==0 and day_index<7):
            week1_index=((i_date.month-1)*7) + day_index
            # print(week1_index)
            week1[week1_index] = day
            if(day_index==6):
                week1_flag=1

        elif(week2_flag==0 and day_index<7):
            week2_index=((i_date.month-1)*7)+day_index
            week2[week2_index] = day
            if(day_index==6):
                week2_flag=1

        elif(week3_flag==0 and day_index<7):
            week3_index=((i_date.month-1)*7)+day_index
            week3[week3_index] = day
            if(day_index==6):
                week3_flag=1

        elif(week4_flag==0 and day_index<7):
            week4_index=((i_date.month-1)*7)+day_index
            week4[week4_index] = day
            if(day_index==6):
                week4_flag=1

        elif(week5_flag==0 and day_index<7):
            week5_index=((i_date.month-1)*7)+day_index
            week5[week5_index] = day
            if(day_index==6):
                week5_flag=1

        elif(week6_flag==0 and day_index<7):
            week6_index=((i_date.month-1)*7)+day_index
            week6[week6_index] = day
            if(day_index==6):
                week6_flag=1

        i_int_date += 1
        i_date_check = mdates.num2date(i_int_date)
        if(i_date_check.month != i_date.month):
            week1_flag = 0
            week2_flag = 0
            week3_flag = 0
            week4_flag = 0
            week5_flag = 0
            week6_flag = 0