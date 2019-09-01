def day_color_map(week,week_color,d1,p1,n1):
    negative_colors=["#fc9272","#ef3b2c","#a50f15","#67000d"]
    positive_colors=["#a1d99b","#41ab5d","#006d2c","#00441b"]
    index=0
    # print(d1[0])
    for i in range(len(week)):
        if(week[i] == []):
            week_color[i]='w'
        else:
            if(d1.count(week[i][0])>0):
                index=d1.index(week[i][0])
                if(p1[index]>=0):
                    temp_colors=positive_colors
                elif(p1[index]<0):
                    temp_colors=negative_colors
                if(n1[index]>0.25):
                    if(n1[index]>0.50):
                        if(n1[index]>0.75):
                            week_color[i]=temp_colors[3]
                        else:
                            week_color[i]=temp_colors[2]
                    else:
                        week_color[i] = temp_colors[1]
                else:
                    week_color[i] = temp_colors[0]
            else:
                week_color[i] = 'w'

            # print(week_color)