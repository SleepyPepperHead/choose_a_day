print("codes to decide which day you date with friends in weekends if you guys don't know which day to choose")

color = input('color of your panty today:')
color_l = list(color)
nums = map(ord, color_l)
if sum(nums) % 2:
    print('Sun.')
else:
    print('Sat.')
