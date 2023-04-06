jury = int(input())
grade = 0
presentations = 0
command = input()

while command != 'Finish':
    cur_presentation_name = command
    presentations += 1
    avr_presentation_grade = 0
    for pres_grade in range(jury):
        grade_now = float(input())
        avr_presentation_grade += grade_now
    avr_presentation_grade /= jury
    grade += avr_presentation_grade
    print(f'{cur_presentation_name} - {avr_presentation_grade:.2f}.')
    command = input()
final = grade / presentations
print(f"Student's final assessment is {final:.2f}.")
