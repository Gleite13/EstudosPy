from time import sleep
import emoji
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(emoji.emojize(":fireworks: Fogos :fireworks:" , language='alias'))
