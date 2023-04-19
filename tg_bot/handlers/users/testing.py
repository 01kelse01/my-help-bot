# from aiogram import types, Dispatcher
# from aiogram.dispatcher import FSMContext
# from aiogram.dispatcher.filters import Command
#
# from tg_bot.misc import Test
#
#
# async def enter_test(message: types.Message):
#     text = [
#         "Ви почали тестування!",
#         "Запитання № 1:",
#         "Скільки Вам років?"
#     ]
#     await message.answer('\n'.join(text))
#     await Test.Q1.set()
#
#
# async def answer_q1(message: types.Message, state: FSMContext):
#     answer = message.text
#     await state.update_data(answer1=answer)
#     text = [
#         "Запитання № 2:",
#         "Який у Вас настрій?"
#     ]
#     await message.answer('\n'.join(text))
#     await Test.next()
#
#
# async def answer_q2(message: types.Message, state: FSMContext):
#     data = await state.get_data()
#     answer1 = data.get('answer1')
#     answer2 = message.text
#
#     await message.answer("Дякуємо за Ваші відповіді!")
#     await message.answer(f"Відповідь № 1: {answer1}")
#     await message.answer(f"Відповідь № 2: {answer2}")
#
#     await state.reset_state()
#
#
# def register_test(dp: Dispatcher):
#     dp.register_message_handler(enter_test, Command('test'))
#     dp.register_message_handler(answer_q1, state=Test.Q1)
#     dp.register_message_handler(answer_q2, state=Test.Q2)
