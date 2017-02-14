#twilio project

from twilio.rest import TwilioRestClient
import random
# put your own credentials here
ACCOUNT_SID = 'AC58137527b8fd0afec8025668e4e775e8'
AUTH_TOKEN = 'e7ee1fde133b36dab0d9ba7fbcd47fd9'

client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN)

text = ['Quote: Princess Caroline, what are we doing???', 'If youre a bird, Im a bird']
pics = ['https://c1.staticflickr.com/3/2661/32417720530_02cebca7b3_b.jpg',
        'https://c1.staticflickr.com/3/2167/32417720860_5357e98e71_b.jpg',
        'https://c1.staticflickr.com/3/2637/32757845116_b920669d59_b.jpg',
        'https://c1.staticflickr.com/3/2188/32417721110_a5e63af144_b.jpg',
        'https://c2.staticflickr.com/4/3913/32757845506_8475fab25d_b.jpg',
        'https://c1.staticflickr.com/3/2700/32417721360_fcf470783d_b.jpg',
        'https://c1.staticflickr.com/1/425/32757846306_f5979431ce_b.jpg',
        'https://c1.staticflickr.com/3/2892/32417721610_8f7401efac_b.jpg',
        'https://c1.staticflickr.com/1/620/32757846506_d21910138d_b.jpg',
        'https://c1.staticflickr.com/1/679/32757846596_ed3c6de101_b.jpg',
        'https://c1.staticflickr.com/3/2904/32757846606_1ebebc27a8_b.jpg',
        'https://c1.staticflickr.com/3/2062/32757846676_ba6581969f_b.jpg',
        'https://c1.staticflickr.com/1/673/32757846816_9d01e9ce97_b.jpg',
        'https://c1.staticflickr.com/1/620/32757846876_bc4e79e1b0_b.jpg',
        'https://c1.staticflickr.com/3/2296/32757847016_a15d547442_b.jpg',
        'https://c1.staticflickr.com/1/718/32757847096_e615a2c3a6_b.jpg',
        'https://c1.staticflickr.com/1/753/32757847326_34c19af470_b.jpg',
        'https://c1.staticflickr.com/3/2802/32757847586_663f795581_b.jpg',
        'https://c1.staticflickr.com/1/416/32757844976_d63ff47f75_b.jpg',
        ]
# ['bopeep', 'cherry', 'cradle', 'cs_days', 'dazed', 'derp', 'dora', 'interview', 'legpop', 'minion1', 'minion2', 'ocean', 'peanuts', 'smiles', 'smooch', 'stadium', 'swaggy', 'view', 'yellow']


client.messages.create(
    to = '+16023203025',
    from_ = '+14804189544',
    body = 'Good morning\n Quote:' + random.choice(text),
    media_url = random.choice(pics)
    # '~/images/' + random.choice(pics) + '.JPG'
)

