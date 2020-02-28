import asyncio
from datetime import datetime, timedelta
from pydub import AudioSegment
from pydub.playback import play


ding = AudioSegment.from_wav('ding.wav')
tick = AudioSegment.from_wav('tick.wav')


def prompt_continue_or_quit(timer_name):
    cont = True
    result = input(f"Press enter to start {timer_name} timer or q to quit: ")
    if result.upper().startswith('Q'):
        cont = False
    return cont


async def countdown(minutes):
    stop_time = datetime.now() + timedelta(minutes=minutes)
    asyncio.create_task(play_sound(tick))
    while datetime.now() < stop_time:
        time_left = stop_time - datetime.now()
        hours, remainder = divmod(time_left.total_seconds(), 3600)
        tl_min, tl_sec = divmod(remainder, 60)
        tl_min = int(tl_min)
        tl_sec = int(tl_sec)
        print(f'Time remaining: {tl_min:02}:{tl_sec:02}')
        await asyncio.sleep(1)
    await play_sound(ding)


async def play_sound(sound):
    play(sound)


async def main():
    cont = True
    while cont:        
        cont = prompt_continue_or_quit('work')
        if cont:
            await countdown(25)
            cont = prompt_continue_or_quit('break')
            if cont:                
                await countdown(5)


if __name__ == "__main__":
    asyncio.run(main())