from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

#кнопки меню
btnMainFunc = KeyboardButton('Рассчитать стоимость ТС', row_width = 1)
btnConsultation = KeyboardButton('Нужна консультация', row_width = 2)
btnInfo = KeyboardButton('Информация', row_width = 2)
btnWebPage = KeyboardButton('Перейти на сайт', row_width = 2)
btnChat = KeyboardButton('Чат сообщества', row_width = 2)
btnMyHistory = KeyboardButton('История моих расчетов', row_width = 1)
btnSpecialHistory = KeyboardButton('История всех расчетов', row_width = 1)

#кнопки ПТС
ptsWithGlonas = InlineKeyboardButton('С кнопкой ГЛОНАСС', row_width = 1)
ptsWithoutGlonas = InlineKeyboardButton('Без кнопки ГЛОНАСС', row_width = 1)

#общие инлайн
cancelForAll = InlineKeyboardButton(text='Отмена', callback_data='cancel')

#inline menu первого поста
firstPost = InlineKeyboardMarkup(row_width=1)

mainFunc = InlineKeyboardButton(text='Я готов, давайте посчитаем!', callback_data='mainfunc_inline')
firstPost.insert(mainFunc)

#inline menu info
infoPost = InlineKeyboardMarkup(row_width=1)

mainFuncInfo = InlineKeyboardButton(text='Рассчитать стоимость ТС', callback_data='mainfunc_inline')
infoPost.insert(mainFuncInfo)

consultationInfo = InlineKeyboardButton(text='Нужна консультация', callback_data='consultation_inline')
infoPost.insert(consultationInfo)

webPageInfo = InlineKeyboardButton(text='Перейти на сайт', callback_data='webpage_inline')
infoPost.insert(webPageInfo)

chatInfo = InlineKeyboardButton(text='Чат сообщества', callback_data='chat_inline')
infoPost.insert(chatInfo)

infoPost.insert(cancelForAll)

backToInfo = InlineKeyboardMarkup(row_width=1)

backInfo= InlineKeyboardButton(text='Назад', callback_data='info_back')
backToInfo.insert(backInfo)

backToInfo.insert(cancelForAll)

#inline menu выбора ТС
techCheck = InlineKeyboardMarkup(row_width=1)

auto = InlineKeyboardButton(text='Автомобиль', callback_data='auto')
techCheck.insert(auto)

moto = InlineKeyboardButton(text='Мотоцикл', callback_data='moto')
techCheck.insert(moto)

electro = InlineKeyboardButton(text='Электромобиль', callback_data='electro')
techCheck.insert(electro)

comercial = InlineKeyboardButton(text='Коммерческий транспорт', callback_data='comercial')
techCheck.insert(comercial)

techCheck.insert(cancelForAll)

#inline menu выбора данных или ссылки
autoCheck = InlineKeyboardMarkup(row_width=1)

infoAuto = InlineKeyboardButton(text='Есть общие данные', callback_data='data')
autoCheck.insert(infoAuto)

linkAuto = InlineKeyboardButton(text='Есть ссылка на конкретный автомобиль', callback_data='link')
autoCheck.insert(linkAuto)

backAuto = InlineKeyboardButton(text='Назад', callback_data='auto_back')
autoCheck.insert(backAuto)

autoCheck.insert(cancelForAll)

#inline menu выбора данных или ссылки
motoCheck = InlineKeyboardMarkup(row_width=1)

infoMoto = InlineKeyboardButton(text='Есть общие данные', callback_data='dataMoto')
motoCheck.insert(infoMoto)

linkMoto = InlineKeyboardButton(text='Есть ссылка на конкретный мотоцикл', callback_data='linkMoto')
motoCheck.insert(linkMoto)


motoCheck.insert(backAuto)

motoCheck.insert(cancelForAll)

#inline menu выбора данных или ссылки
electroCheck = InlineKeyboardMarkup(row_width=1)

infoElectro = InlineKeyboardButton(text='Есть общие данные', callback_data='dataElectro')
electroCheck.insert(infoElectro)

linkElectro = InlineKeyboardButton(text='Есть ссылка на конкретный электромобиль', callback_data='linkElectro')
electroCheck.insert(linkElectro)


electroCheck.insert(backAuto)

electroCheck.insert(cancelForAll)

#inline menu выбора данных или ссылки
comercialCheck = InlineKeyboardMarkup(row_width=1)

infoComecial = InlineKeyboardButton(text='Есть общие данные', callback_data='dataComercial')
comercialCheck.insert(infoComecial)

linkComecial = InlineKeyboardButton(text='Есть ссылка на конкретный коммерческий транспорт', callback_data='linkComercial')
comercialCheck.insert(linkComecial)


comercialCheck.insert(backAuto)

comercialCheck.insert(cancelForAll)

#inline menu link wait
linkWaitBtns = InlineKeyboardMarkup(row_width=1)

linkWait = InlineKeyboardButton(text='Вставить ссылку', callback_data='waitLink')
linkWaitBtns.insert(linkWait)

linkWaitBtns.insert(backAuto)

linkWaitBtns.insert(cancelForAll)

#inline menu link wait
LinkErrorMenu = InlineKeyboardMarkup(row_width=1)

RestartLink = InlineKeyboardButton(text='Начать расчет заново', callback_data='RestartLink')
LinkErrorMenu.insert(RestartLink)

HelpLink = InlineKeyboardButton(text='Нужна помощь', callback_data='HelpLink')
LinkErrorMenu.insert(HelpLink)

LinkErrorMenu.insert(backAuto)
LinkErrorMenu.insert(cancelForAll)

#inline menu link wait
helpLinkMenu = InlineKeyboardMarkup(row_width=1)

QueLink = InlineKeyboardButton(text='Задать свой вопрос', callback_data='QueLink')
helpLinkMenu.insert(QueLink)

helpLinkMenu.insert(RestartLink)

helpLinkMenu.insert(backAuto)

helpLinkMenu.insert(cancelForAll)

#inline menu link wait
linkWaitBtnsMoto = InlineKeyboardMarkup(row_width=1)

linkWaitMoto = InlineKeyboardButton(text='Вставить ссылку', callback_data='waitLinkMoto')
linkWaitBtnsMoto.insert(linkWaitMoto)

linkWaitBtnsMoto.insert(backAuto)

linkWaitBtnsMoto.insert(cancelForAll)

#inline menu link wait
linkWaitBtnsElectro = InlineKeyboardMarkup(row_width=1)

linkWaitElectro = InlineKeyboardButton(text='Вставить ссылку', callback_data='waitLinkElectro')
linkWaitBtnsElectro.insert(linkWaitElectro)

linkWaitBtnsElectro.insert(backAuto)

linkWaitBtnsElectro.insert(cancelForAll)

#inline menu link wait
linkWaitBtnsComercial = InlineKeyboardMarkup(row_width=1)

linkWaitComercial = InlineKeyboardButton(text='Вставить ссылку', callback_data='waitLinkComercial')
linkWaitBtnsComercial.insert(linkWaitComercial)

linkWaitBtnsComercial.insert(backAuto)

linkWaitBtnsComercial.insert(cancelForAll)

#inline menu pts link
ptsBtnsLink = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasLink = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_link')
ptsBtnsLink.insert(ptsWithGlonasLink)

ptsWithoutGlonasLink = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_link')
ptsBtnsLink.insert(ptsWithoutGlonasLink)

ptsBtnsLink.insert(backAuto)
ptsBtnsLink.insert(cancelForAll)

#inline menu pts link
ptsBtnsLinkMoto = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasLinkMoto = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_linkMoto')
ptsBtnsLinkMoto.insert(ptsWithGlonasLinkMoto)

ptsWithoutGlonasLinkMoto = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_linkMoto')
ptsBtnsLinkMoto.insert(ptsWithoutGlonasLinkMoto)

ptsBtnsLinkMoto.insert(backAuto)
ptsBtnsLinkMoto.insert(cancelForAll)

#inline menu pts link
ptsBtnsLinkElectro = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasLinkElectro = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_linkElectro')
ptsBtnsLinkElectro.insert(ptsWithGlonasLinkElectro)

ptsWithoutGlonasLinkElectro = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_linkElectro')
ptsBtnsLinkElectro.insert(ptsWithoutGlonasLinkElectro)

ptsBtnsLinkElectro.insert(backAuto)
ptsBtnsLinkElectro.insert(cancelForAll)

#inline menu pts link
ptsBtnsLinkComercial = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasLinkComercial = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_linkComercial')
ptsBtnsLinkComercial.insert(ptsWithGlonasLinkComercial)

ptsWithoutGlonasLinkComercial = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_linkComercial')
ptsBtnsLinkComercial.insert(ptsWithoutGlonasLinkComercial)

ptsBtnsLinkComercial.insert(backAuto)
ptsBtnsLinkComercial.insert(cancelForAll)

#inline menu выбора цены
priceCheck = InlineKeyboardMarkup(row_width=1)

priceNetto = InlineKeyboardButton(text='Ввести НЕТТО цену', callback_data='netto')
priceCheck.insert(priceNetto)

priceBrutto = InlineKeyboardButton(text='Ввести БРУТТО цену', callback_data='brutto')
priceCheck.insert(priceBrutto)

priceCheck.insert(backAuto)

priceCheck.insert(cancelForAll)

#inline menu выбора цены
priceCheckMoto = InlineKeyboardMarkup(row_width=1)

priceNettoMoto = InlineKeyboardButton(text='Ввести НЕТТО цену', callback_data='nettoMoto')
priceCheckMoto.insert(priceNettoMoto)

priceBruttoMoto = InlineKeyboardButton(text='Ввести БРУТТО цену', callback_data='bruttoMoto')
priceCheckMoto.insert(priceBruttoMoto)

priceCheckMoto.insert(backAuto)

priceCheckMoto.insert(cancelForAll)

#inline menu выбора цены
priceCheckElectro = InlineKeyboardMarkup(row_width=1)

priceNettoElectro = InlineKeyboardButton(text='Ввести НЕТТО цену', callback_data='nettoElectro')
priceCheckElectro.insert(priceNettoElectro)

priceBruttoElectro = InlineKeyboardButton(text='Ввести БРУТТО цену', callback_data='bruttoElectro')
priceCheckElectro.insert(priceBruttoElectro)

priceCheckElectro.insert(backAuto)

priceCheckElectro.insert(cancelForAll)

#inline menu выбора цены
priceCheckComercial = InlineKeyboardMarkup(row_width=1)

priceNettoComercial = InlineKeyboardButton(text='Ввести НЕТТО цену', callback_data='nettoComercial')
priceCheckComercial.insert(priceNettoComercial)

priceBruttoComercial = InlineKeyboardButton(text='Ввести БРУТТО цену', callback_data='bruttoComercial')
priceCheckComercial.insert(priceBruttoComercial)

priceCheckComercial.insert(backAuto)

priceCheckComercial.insert(cancelForAll)

#inline menu отмена/назад
cancelBack = InlineKeyboardMarkup(row_width=1)

cancelBack.insert(backAuto)

cancelBack.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceNettoAuto = InlineKeyboardMarkup(row_width=1)

backPriceNettoAuto = InlineKeyboardButton(text='Назад', callback_data='backPriceNettoAuto')
cancelBackPriceNettoAuto.insert(backPriceNettoAuto)

cancelBackPriceNettoAuto.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceNettoMoto = InlineKeyboardMarkup(row_width=1)

backPriceNettoMoto = InlineKeyboardButton(text='Назад', callback_data='backPriceNettoMoto')
cancelBackPriceNettoMoto.insert(backPriceNettoMoto)

cancelBackPriceNettoMoto.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceNettoElectro = InlineKeyboardMarkup(row_width=1)

backPriceNettoElectro = InlineKeyboardButton(text='Назад', callback_data='backPriceNettoElectro')
cancelBackPriceNettoElectro.insert(backPriceNettoElectro)

cancelBackPriceNettoElectro.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceBruttoAuto = InlineKeyboardMarkup(row_width=1)

backPriceBruttoAuto = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoAuto')
cancelBackPriceBruttoAuto.insert(backPriceBruttoAuto)

cancelBackPriceBruttoAuto.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceBruttoMoto = InlineKeyboardMarkup(row_width=1)

backPriceBruttoMoto = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoMoto')
cancelBackPriceBruttoMoto.insert(backPriceBruttoMoto)

cancelBackPriceBruttoMoto.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceBruttoElectro = InlineKeyboardMarkup(row_width=1)

backPriceBruttoElectro = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoElectro')
cancelBackPriceBruttoElectro.insert(backPriceBruttoElectro)

cancelBackPriceBruttoElectro.insert(cancelForAll)

#inline menu отмена/назад
cancelBackPriceBruttoComercial = InlineKeyboardMarkup(row_width=1)

backPriceBruttoComercial = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoComercial')
cancelBackPriceBruttoComercial.insert(backPriceBruttoComercial)

cancelBackPriceBruttoComercial.insert(cancelForAll)

#inline menu неправильный ввод нетто
againNetto = InlineKeyboardMarkup(row_width=1)

priceNettoAgain = InlineKeyboardButton(text='Ввести НЕТТО цену заново', callback_data='NettoAgain')
againNetto .insert(priceNettoAgain )

helpPriceNetto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceNetto')
againNetto .insert(helpPriceNetto)

againNetto.insert(backAuto)

againNetto.insert(cancelForAll)

#inline menu неправильный ввод нетто
helpPriceNettoMenu = InlineKeyboardMarkup(row_width=1)

Que = InlineKeyboardButton(text='Задать свой вопрос', callback_data='Que')
helpPriceNettoMenu.insert(Que)

BackPriceNetto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceNetto')
helpPriceNettoMenu.insert(BackPriceNetto)

RestartError = InlineKeyboardButton(text='Начать расчет заново', callback_data='RestartError')
helpPriceNettoMenu.insert(RestartError)

helpPriceNettoMenu.insert(cancelForAll)

#inline menu неправильный ввод нетто MOTO
againNettoMoto = InlineKeyboardMarkup(row_width=1)

priceNettoAgainMoto = InlineKeyboardButton(text='Ввести НЕТТО цену заново', callback_data='NettoAgainMoto')
againNettoMoto.insert(priceNettoAgainMoto)

helpPriceNettoMoto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceNettoMoto')
againNettoMoto.insert(helpPriceNettoMoto)

againNettoMoto.insert(backAuto)

againNettoMoto.insert(cancelForAll)

#inline menu неправильный ввод нетто
helpPriceNettoMenuMoto = InlineKeyboardMarkup(row_width=1)

helpPriceNettoMenuMoto.insert(Que)

BackPriceNettoMoto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceNettoMoto')
helpPriceNettoMenuMoto.insert(BackPriceNettoMoto)

helpPriceNettoMenuMoto.insert(RestartError)

helpPriceNettoMenuMoto.insert(cancelForAll)

#inline menu неправильный ввод нетто Electro
againNettoElectro = InlineKeyboardMarkup(row_width=1)

priceNettoAgainElectro = InlineKeyboardButton(text='Ввести НЕТТО цену заново', callback_data='NettoAgainElectro')
againNettoElectro.insert(priceNettoAgainElectro)

helpPriceNettoElectro = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceNettoElectro')
againNettoElectro.insert(helpPriceNettoElectro)

againNettoElectro.insert(backAuto)

againNettoElectro.insert(cancelForAll)

#inline menu неправильный ввод нетто
helpPriceNettoMenuElectro = InlineKeyboardMarkup(row_width=1)

helpPriceNettoMenuElectro.insert(Que)

BackPriceNettoElectro = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceNettoElectro')
helpPriceNettoMenuElectro.insert(BackPriceNettoElectro)

helpPriceNettoMenuElectro.insert(RestartError)

helpPriceNettoMenuElectro.insert(cancelForAll)


#inline menu неправильный ввод брутто
againBrutto = InlineKeyboardMarkup(row_width=1)

priceBruttoAgain = InlineKeyboardButton(text='Ввести Брутто цену заново', callback_data='BruttoAgain')
againBrutto .insert(priceBruttoAgain)

helpPriceBrutto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceBrutto')
againBrutto .insert(helpPriceBrutto)

againBrutto.insert(backAuto)

againBrutto.insert(cancelForAll)

#inline menu неправильный ввод нетто
helpPriceBruttoMenu = InlineKeyboardMarkup(row_width=1)


helpPriceBruttoMenu.insert(Que)

BackPriceBrutto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceBrutto')
helpPriceBruttoMenu.insert(BackPriceBrutto)

helpPriceBruttoMenu.insert(RestartError)

helpPriceBruttoMenu.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
againBruttoMoto = InlineKeyboardMarkup(row_width=1)

priceBruttoAgainMoto = InlineKeyboardButton(text='Ввести Брутто цену заново', callback_data='BruttoAgainMoto')
againBruttoMoto.insert(priceBruttoAgainMoto)

helpPriceBruttoMoto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceBruttoMoto')
againBruttoMoto.insert(helpPriceBruttoMoto)

againBruttoMoto.insert(backAuto)

againBruttoMoto.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpPriceBruttoMenuMoto = InlineKeyboardMarkup(row_width=1)

helpPriceBruttoMenuMoto.insert(Que)

BackPriceBruttoMoto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceBruttoMoto')
helpPriceBruttoMenuMoto.insert(BackPriceBruttoMoto)

helpPriceBruttoMenuMoto.insert(RestartError)

helpPriceBruttoMenuMoto.insert(cancelForAll)

#inline menu неправильный ввод брутто Electro
againBruttoElectro = InlineKeyboardMarkup(row_width=1)

priceBruttoAgainElectro = InlineKeyboardButton(text='Ввести Брутто цену заново', callback_data='BruttoAgainElectro')
againBruttoElectro.insert(priceBruttoAgainElectro)

helpPriceBruttoElectro = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceBruttoElectro')
againBruttoElectro.insert(helpPriceBruttoElectro)

againBruttoElectro.insert(backAuto)

againBruttoElectro.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpPriceBruttoMenuElectro = InlineKeyboardMarkup(row_width=1)

helpPriceBruttoMenuElectro.insert(Que)

BackPriceBruttoElectro = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceBruttoElectro')
helpPriceBruttoMenuElectro.insert(BackPriceBruttoElectro)

helpPriceBruttoMenuElectro.insert(RestartError)

helpPriceBruttoMenuElectro.insert(cancelForAll)

#inline menu неправильный ввод брутто Comercial
againBruttoComercial = InlineKeyboardMarkup(row_width=1)

priceBruttoAgainComercial = InlineKeyboardButton(text='Ввести Брутто цену заново', callback_data='BruttoAgainComercial')
againBruttoComercial.insert(priceBruttoAgainComercial)

helpPriceBruttoComercial = InlineKeyboardButton(text='Нужна помощь', callback_data='helpPriceBruttoComercial')
againBruttoComercial.insert(helpPriceBruttoComercial)

againBruttoComercial.insert(backAuto)

againBruttoComercial.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpPriceBruttoMenuComercial = InlineKeyboardMarkup(row_width=1)

helpPriceBruttoMenuComercial.insert(Que)

BackPriceBruttoComercial = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackPriceBruttoComercial')
helpPriceBruttoMenuComercial.insert(BackPriceBruttoComercial)

helpPriceBruttoMenuComercial.insert(RestartError)

helpPriceBruttoMenuComercial.insert(cancelForAll)



#inline menu неправильный ввод объема брутто
againBruttoVolume = InlineKeyboardMarkup(row_width=1)

volumeBruttoAgain = InlineKeyboardButton(text='Ввести объем двигателя заново', callback_data='BruttoVolumeAgain')
againBruttoVolume.insert(volumeBruttoAgain)

helpVolumeBrutto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpVolumeBrutto')
againBruttoVolume.insert(helpVolumeBrutto)

againBruttoVolume.insert(backAuto)

againBruttoVolume.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpVolumeBruttoMenu = InlineKeyboardMarkup(row_width=1)

helpVolumeBruttoMenu.insert(Que)

BackVolumeBrutto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackVolumeBrutto')
helpVolumeBruttoMenu.insert(BackVolumeBrutto)

helpVolumeBruttoMenu.insert(RestartError)

helpVolumeBruttoMenu.insert(cancelForAll)

#inline menu неправильный ввод объема брутто Moto
againBruttoVolumeMoto = InlineKeyboardMarkup(row_width=1)

volumeBruttoAgainMoto = InlineKeyboardButton(text='Ввести объем двигателя заново', callback_data='BruttoVolumeAgainMoto')
againBruttoVolumeMoto.insert(volumeBruttoAgainMoto)

helpVolumeBruttoMoto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpVolumeBruttoMoto')
againBruttoVolumeMoto.insert(helpVolumeBruttoMoto)

againBruttoVolumeMoto.insert(backAuto)

againBruttoVolumeMoto.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpVolumeBruttoMenuMoto = InlineKeyboardMarkup(row_width=1)

helpVolumeBruttoMenuMoto.insert(Que)

BackVolumeBruttoMoto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackVolumeBruttoMoto')
helpVolumeBruttoMenuMoto.insert(BackVolumeBruttoMoto)

helpVolumeBruttoMenuMoto.insert(RestartError)

helpVolumeBruttoMenuMoto.insert(cancelForAll)


#inline menu неправильный ввод объема нетто
againNettoVolume = InlineKeyboardMarkup(row_width=1)

volumeNettoAgain = InlineKeyboardButton(text='Ввести объем двигателя заново', callback_data='NettoVolumeAgain')
againNettoVolume.insert(volumeNettoAgain)

helpVolumeNetto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpVolumeNetto')
againNettoVolume.insert(helpVolumeNetto)

againNettoVolume.insert(backAuto)

againNettoVolume.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpVolumeNettoMenu = InlineKeyboardMarkup(row_width=1)

helpVolumeNettoMenu.insert(Que)

BackVolumeNetto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackVolumeNetto')
helpVolumeNettoMenu.insert(BackVolumeBruttoMoto)

helpVolumeNettoMenu.insert(RestartError)

helpVolumeNettoMenu.insert(cancelForAll)

#inline menu неправильный ввод объема нетто Moto
againNettoVolumeMoto = InlineKeyboardMarkup(row_width=1)

volumeNettoAgainMoto = InlineKeyboardButton(text='Ввести объем двигателя заново', callback_data='NettoVolumeAgainMoto')
againNettoVolumeMoto.insert(volumeNettoAgainMoto)

helpVolumeNettoMoto = InlineKeyboardButton(text='Нужна помощь', callback_data='helpVolumeNettoMoto')
againNettoVolumeMoto.insert(helpVolumeNettoMoto)

againNettoVolumeMoto.insert(backAuto)

againNettoVolumeMoto.insert(cancelForAll)

#inline menu неправильный ввод брутто Moto
helpVolumeNettoMenuMoto = InlineKeyboardMarkup(row_width=1)

helpVolumeNettoMenuMoto.insert(Que)

BackVolumeNettoMoto = InlineKeyboardButton(text='Вернуться к моему расчету', callback_data='BackVolumeNettoMoto')
helpVolumeNettoMenuMoto.insert(BackVolumeNettoMoto)

helpVolumeNettoMenuMoto.insert(RestartError)

helpVolumeNettoMenuMoto.insert(cancelForAll)

#inline menu выбора цены
final = InlineKeyboardMarkup(row_width=1)

purchaseFinal = InlineKeyboardButton(text='Заказать автомобиль', callback_data='purchase')
final.insert(purchaseFinal)

finalConsult = InlineKeyboardButton(text='Нужна помощь', callback_data='finalConsult')
final.insert(finalConsult)

againFinal = InlineKeyboardButton(text='Произвести новый расчет', callback_data='againGet')
final.insert(againFinal)

final.insert(backAuto)

final.insert(cancelForAll)

#inline menu выбора цены
finalAgain = InlineKeyboardMarkup(row_width=1)

finalAgain.insert(purchaseFinal)

finalAgain.insert(finalConsult)

finalAgain.insert(cancelForAll)



#inline menu выбора цены Moto
finalMoto = InlineKeyboardMarkup(row_width=1)

purchaseFinalMoto = InlineKeyboardButton(text='Заказать мотоцикл', callback_data='purchaseMoto')
finalMoto.insert(purchaseFinalMoto)

finalMoto.insert(finalConsult)

againFinalMoto = InlineKeyboardButton(text='Произвести новый расчет', callback_data='againGetMoto')
finalMoto.insert(againFinalMoto)

finalMoto.insert(backAuto)

finalMoto.insert(cancelForAll)

#inline menu выбора цены
finalAgainMoto = InlineKeyboardMarkup(row_width=1)

finalAgainMoto.insert(purchaseFinalMoto)

finalAgainMoto.insert(finalConsult)

finalAgainMoto.insert(cancelForAll)

#inline menu выбора цены Electro
finalElectro = InlineKeyboardMarkup(row_width=1)

purchaseFinalElectro = InlineKeyboardButton(text='Заказать электромобиль', callback_data='purchaseElectro')
finalElectro.insert(purchaseFinalElectro)

finalElectro.insert(finalConsult)

againFinalElectro = InlineKeyboardButton(text='Произвести новый расчет', callback_data='againGetElectro')
finalElectro.insert(againFinalElectro)

finalElectro.insert(backAuto)

finalElectro.insert(cancelForAll)

#inline menu выбора цены
finalAgainElectro = InlineKeyboardMarkup(row_width=1)

finalAgainElectro.insert(purchaseFinalElectro)

finalAgainElectro.insert(finalConsult)

finalAgainElectro.insert(cancelForAll)

#inline menu выбора цены Comercial
finalComercial = InlineKeyboardMarkup(row_width=1)

purchaseFinalComercial = InlineKeyboardButton(text='Заказать коммерческий транспорт', callback_data='purchaseComercial')
finalComercial.insert(purchaseFinalComercial)

finalComercial.insert(finalConsult)

againFinalComercial = InlineKeyboardButton(text='Произвести новый расчет', callback_data='againGetComercial')
finalComercial.insert(againFinalComercial)

finalComercial.insert(backAuto)

finalComercial.insert(cancelForAll)

#inline menu выбора цены
finalAgainComercial = InlineKeyboardMarkup(row_width=1)

finalAgainComercial.insert(purchaseFinalComercial)

finalAgainComercial.insert(finalConsult)

finalAgainComercial.insert(cancelForAll)

#inline menu года
yearBtnsNetto = InlineKeyboardMarkup(row_width=1)

yearThreeNetto = InlineKeyboardButton(text='До 3 лет', callback_data='three_netto')
yearBtnsNetto.insert(yearThreeNetto)

yearLessNetto = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_netto')
yearBtnsNetto.insert(yearLessNetto)

yearMoreNetto = InlineKeyboardButton(text='Более 5 лет', callback_data='more_netto')
yearBtnsNetto.insert(yearMoreNetto)

backVolumeNettoAuto = InlineKeyboardButton(text='Назад', callback_data='backVolumeNettoAuto')
yearBtnsNetto.insert(backVolumeNettoAuto)
yearBtnsNetto.insert(cancelForAll)

#inline menu года Moto
yearBtnsNettoMoto = InlineKeyboardMarkup(row_width=1)

yearThreeNettoMoto = InlineKeyboardButton(text='До 3 лет', callback_data='three_nettoMoto')
yearBtnsNettoMoto.insert(yearThreeNettoMoto)

yearLessNettoMoto = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_nettoMoto')
yearBtnsNettoMoto.insert(yearLessNettoMoto)

yearMoreNettoMoto = InlineKeyboardButton(text='Более 5 лет', callback_data='more_nettoMoto')
yearBtnsNettoMoto.insert(yearMoreNettoMoto)

backVolumeNettoMoto = InlineKeyboardButton(text='Назад', callback_data='backVolumeNettoMoto')
yearBtnsNettoMoto.insert(backVolumeNettoMoto)
yearBtnsNettoMoto.insert(cancelForAll)

#inline menu года Electro
yearBtnsNettoElectro = InlineKeyboardMarkup(row_width=1)

yearThreeNettoElectro = InlineKeyboardButton(text='До 3 лет', callback_data='three_nettoElectro')
yearBtnsNettoElectro.insert(yearThreeNettoElectro)

yearLessNettoElectro = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_nettoElectro')
yearBtnsNettoElectro.insert(yearLessNettoElectro)

yearMoreNettoElectro = InlineKeyboardButton(text='Более 5 лет', callback_data='more_nettoElectro')
yearBtnsNettoElectro.insert(yearMoreNettoElectro)

backPriceNettoElectro = InlineKeyboardButton(text='Назад', callback_data='backPriceNettoElectro')
yearBtnsNettoElectro.insert(backPriceNettoElectro)
yearBtnsNettoElectro.insert(cancelForAll)

#inline menu года brutto
yearBtnsBrutto = InlineKeyboardMarkup(row_width=1)

yearThreeBrutto = InlineKeyboardButton(text='До 3 лет', callback_data='three_brutto')
yearBtnsBrutto.insert(yearThreeBrutto)

yearLessBrutto = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_brutto')
yearBtnsBrutto.insert(yearLessBrutto)

yearMoreBrutto = InlineKeyboardButton(text='Более 5 лет', callback_data='more_brutto')
yearBtnsBrutto.insert(yearMoreBrutto)

backVolumeBruttoAuto = InlineKeyboardButton(text='Назад', callback_data='backVolumeBruttoAuto')
yearBtnsBrutto.insert(backVolumeBruttoAuto)
yearBtnsBrutto.insert(cancelForAll)

#inline menu года brutto Moto
yearBtnsBruttoMoto = InlineKeyboardMarkup(row_width=1)

yearThreeBruttoMoto = InlineKeyboardButton(text='До 3 лет', callback_data='three_bruttoMoto')
yearBtnsBruttoMoto.insert(yearThreeBruttoMoto)

yearLessBruttoMoto = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_bruttoMoto')
yearBtnsBruttoMoto.insert(yearLessBruttoMoto)

yearMoreBruttoMoto = InlineKeyboardButton(text='Более 5 лет', callback_data='more_bruttoMoto')
yearBtnsBruttoMoto.insert(yearMoreBruttoMoto)

backVolumeBruttoMoto = InlineKeyboardButton(text='Назад', callback_data='backVolumeBruttoMoto')
yearBtnsBruttoMoto.insert(backVolumeBruttoMoto)
yearBtnsBruttoMoto.insert(cancelForAll)

#inline menu года brutto Electro
yearBtnsBruttoElectro = InlineKeyboardMarkup(row_width=1)

yearThreeBruttoElectro = InlineKeyboardButton(text='До 3 лет', callback_data='three_bruttoElectro')
yearBtnsBruttoElectro.insert(yearThreeBruttoElectro)

yearLessBruttoElectro = InlineKeyboardButton(text='От 3 до 5 лет', callback_data='less_bruttoElectro')
yearBtnsBruttoElectro.insert(yearLessBruttoElectro)

yearMoreBruttoElectro = InlineKeyboardButton(text='Более 5 лет', callback_data='more_bruttoElectro')
yearBtnsBruttoElectro.insert(yearMoreBruttoElectro)

backPriceBruttoElectro = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoElectro')
yearBtnsBruttoElectro.insert(backPriceBruttoElectro)
yearBtnsBruttoElectro.insert(cancelForAll)

#inline menu года brutto Comercial
yearBtnsBruttoComercial = InlineKeyboardMarkup(row_width=1)

yearThreeBruttoComercial = InlineKeyboardButton(text='До 3 лет', callback_data='three_bruttoComercial')
yearBtnsBruttoComercial.insert(yearThreeBruttoComercial)

yearMoreBruttoComercial = InlineKeyboardButton(text='Старше 3 лет', callback_data='more_bruttoComercial')
yearBtnsBruttoComercial.insert(yearMoreBruttoComercial)

backPriceBruttoComercial = InlineKeyboardButton(text='Назад', callback_data='backPriceBruttoComercial')
yearBtnsBruttoComercial.insert(backPriceBruttoComercial)
yearBtnsBruttoComercial.insert(cancelForAll)

#inline menu года brutto Comercial
#inline menu pts netto
ptsBtnsNetto = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasNetto = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_netto')
ptsBtnsNetto.insert(ptsWithGlonasNetto)

ptsWithoutGlonasNetto = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_netto')
ptsBtnsNetto.insert(ptsWithoutGlonasNetto)

backPtsNettoAuto = InlineKeyboardButton(text='Назад', callback_data='backPtsNettoAuto')
ptsBtnsNetto.insert(backPtsNettoAuto)
ptsBtnsNetto.insert(cancelForAll)

#inline menu pts netto Moto
ptsBtnsNettoMoto = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasNettoMoto = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_nettoMoto')
ptsBtnsNettoMoto.insert(ptsWithGlonasNettoMoto)

ptsWithoutGlonasNettoMoto = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_nettoMoto')
ptsBtnsNettoMoto.insert(ptsWithoutGlonasNettoMoto)

backPtsNettoMoto = InlineKeyboardButton(text='Назад', callback_data='backPtsNettoMoto')
ptsBtnsNettoMoto.insert(backPtsNettoMoto)
ptsBtnsNettoMoto.insert(cancelForAll)

#inline menu pts netto Electro
ptsBtnsNettoElectro = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasNettoElectro = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_nettoElectro')
ptsBtnsNettoElectro.insert(ptsWithGlonasNettoElectro)

ptsWithoutGlonasNettoElectro = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_nettoElectro')
ptsBtnsNettoElectro.insert(ptsWithoutGlonasNettoElectro)

backPtsNettoElectro = InlineKeyboardButton(text='Назад', callback_data='backPtsNettoElectro')
ptsBtnsNettoElectro.insert(backPtsNettoElectro)
ptsBtnsNettoElectro.insert(cancelForAll)

#inline menu pts brutto
ptsBtnsBrutto = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasBrutto = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_brutto')
ptsBtnsBrutto.insert(ptsWithGlonasBrutto)

ptsWithoutGlonasBrutto = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_brutto')
ptsBtnsBrutto.insert(ptsWithoutGlonasBrutto)

backPtsBruttoAuto = InlineKeyboardButton(text='Назад', callback_data='backPtsBruttoAuto')
ptsBtnsBrutto.insert(backPtsBruttoAuto)
ptsBtnsBrutto.insert(cancelForAll)

#inline menu pts brutto Moto
ptsBtnsBruttoMoto = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasBruttoMoto = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_bruttoMoto')
ptsBtnsBruttoMoto.insert(ptsWithGlonasBruttoMoto)

ptsWithoutGlonasBruttoMoto = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_bruttoMoto')
ptsBtnsBruttoMoto.insert(ptsWithoutGlonasBruttoMoto)

backPtsBruttoMoto = InlineKeyboardButton(text='Назад', callback_data='backPtsBruttoMoto')
ptsBtnsBruttoMoto.insert(backPtsBruttoMoto)
ptsBtnsBruttoMoto.insert(cancelForAll)

#inline menu pts brutto Electro
ptsBtnsBruttoElectro = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasBruttoElectro = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_bruttoElectro')
ptsBtnsBruttoElectro.insert(ptsWithGlonasBruttoElectro)

ptsWithoutGlonasBruttoElectro = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_bruttoElectro')
ptsBtnsBruttoElectro.insert(ptsWithoutGlonasBruttoElectro)

backPtsBruttoElectro = InlineKeyboardButton(text='Назад', callback_data='backPtsBruttoElectro')
ptsBtnsBruttoElectro.insert(backPtsBruttoElectro)
ptsBtnsBruttoElectro.insert(cancelForAll)

#inline menu pts brutto Comercial
ptsBtnsBruttoComercial = InlineKeyboardMarkup(row_width=1)

ptsWithGlonasBruttoComercial = InlineKeyboardButton(text='С кнопкой ГЛОНАСС', callback_data='has_bruttoComercial')
ptsBtnsBruttoComercial.insert(ptsWithGlonasBruttoComercial)

ptsWithoutGlonasBruttoComercial = InlineKeyboardButton(text='Без кнопки ГЛОНАСС', callback_data='not_bruttoComercial')
ptsBtnsBruttoComercial.insert(ptsWithoutGlonasBruttoComercial)

backPtsBruttoComercial = InlineKeyboardButton(text='Назад', callback_data='backPtsBruttoComercial')
ptsBtnsBruttoComercial.insert(backPtsBruttoComercial)
ptsBtnsBruttoComercial.insert(cancelForAll)

#inline menu выбора истории
myHistoryBtns = InlineKeyboardMarkup(row_width=1)

todayHistory = InlineKeyboardButton(text='Расчеты за сегодня', callback_data='today')
myHistoryBtns.insert(todayHistory)

weekHistory = InlineKeyboardButton(text='Расчеты за неделю', callback_data='week')
myHistoryBtns.insert(weekHistory)

monthHistory = InlineKeyboardButton(text='Расчеты за месяц', callback_data='month')
myHistoryBtns.insert(monthHistory)

allHistory = InlineKeyboardButton(text='Расчеты за все время', callback_data='allTime')
myHistoryBtns.insert(allHistory)

deleteHistory = InlineKeyboardButton(text='Очистить историю расчетов', callback_data='deleteAll')
myHistoryBtns.insert(deleteHistory)

myHistoryBtns.insert(cancelForAll)

historyBack= InlineKeyboardButton(text='Назад', callback_data='historyBack')
myHistoryBtns.insert(historyBack)

historyDeleteBtns = InlineKeyboardMarkup(row_width=1)

deleteAccept = InlineKeyboardButton(text='Подтвердить', callback_data='deleteAccept')
historyDeleteBtns.insert(deleteAccept)

historyDeleteBtns.insert(historyBack)

historyDeleteBtns.insert(cancelForAll)

deleteAcceptBtns = InlineKeyboardMarkup(row_width=1)

acceptBack = InlineKeyboardButton(text='Создать новый расчет ТС', callback_data='acceptBack')
deleteAcceptBtns.insert(acceptBack)
deleteAcceptBtns.insert(cancelForAll)

def genmarkup(data):

    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    for i in data:
        str = f'getItemHistory_{i[0]}'
        markup.add(InlineKeyboardButton(i[3], callback_data=str))
    markup.insert(historyBack)
    markup.insert(cancelForAll)
    return markup

itemHistory = InlineKeyboardMarkup(row_width=1)

itemHistory.insert(historyBack)
itemHistory.insert(cancelForAll)
#все менюшки с ресайзами
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.row(btnMainFunc)
mainMenu.row(btnConsultation, btnInfo)
mainMenu.row(btnWebPage, btnChat)
mainMenu.row(btnMyHistory)

adminMenu = ReplyKeyboardMarkup(resize_keyboard = True)
adminMenu.row(btnMainFunc)
adminMenu.row(btnConsultation, btnInfo)
adminMenu.row(btnWebPage, btnChat)
adminMenu.row(btnMyHistory)
adminMenu.row(btnSpecialHistory)

ptsMenu = ReplyKeyboardMarkup(resize_keyboard = True)
ptsMenu.row(ptsWithGlonas)
ptsMenu.row(ptsWithoutGlonas)
