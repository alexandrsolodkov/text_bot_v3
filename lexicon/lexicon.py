LEXICON: dict[str, str] = {
    'welcome_text': 'Привет, {}!\n\nКупить рекламу в канале, поделиться вакансией, задать вопрос админу и '
                    'предложить пост.\n\nЖмите - /menu',
    'menu': 'Что вас интересует? 🧐',
    'buy_advertising_btn': '💲 Купить рекламу',
    'offer_vacancy_btn': '📄 Прислать вакансию',
    'subscribe': '🎓 Вступить в клуб',
    'offer_news_btn': '🖐 Предложить пост в канал',
    'sign_up_for_mentoring': '💵 Записаться на менторство',
    'additional_services_btn': '⚡️Дополнительные услуги',
    'help': 'Привет! Это бот-помощник Лены из «Копилки текстов».\n\nОн умеет:\n\n'
            '— объяснять условия рекламы на канале;\n'
            '— принимать тексты вакансий и ваши находки для постов;\n'
            '— рассказывать о менторской программе админа.',
    'to_menu': 'В меню',
    # 'buy_advertising': '<b>Форматы и стоимость размещений</b>\n\n'
    #                    'Реклама выходит 1 раз в неделю.\n\n'
    #                    '🔹 <b>Нативный пост 8/72 (8 часов часов в топе, 72 часа в ленте) — 8 000₽</b>\n\n'
    #                    'Вы присылаете тезисы о своём канале или продукте, далее я оформляю пост, отправляю на '
    #                    'согласование. В конце поста будет тег #рекомендую\n\n'
    #                    '🔹 <b>Нативный пост без удаления, 8 часов в топе — 12 000₽</b>\n\n '
    #                    'Вы присылаете тезисы о своём канале или продукте, далее я оформляю пост, отправляю на '
    #                    'согласование. В конце поста будет тег #рекомендую\n\n'
    #                    '📍2 рекламных поста с нуля (не нативные) — 15 000₽\n\n'
    #                    'Я могу написать для вас посты с нуля — если у вас нет готовых. '
    #                    'В отличие от нативных публикаций, эти тексты вы сможете использовать и в других '
    #                    'телеграм-каналах. Затем эти же посты я опубликую и в «Копилке текстов» с разницей в месяц. '
    #                    'Первый без удаления, второй в формате 8/24. В конце поста будет тег #рекомендую.\n'
    #                    '<a href="https://t.me/smotri_kakoi_text/829">Пример →</a>\n\n'
    #                    '<b>Свободные даты</b>:\n'
    #                    'https://clck.ru/34BjoL\n\n'
    #                    '<b>Как купить рекламу</b>:\n'
    #                    'Выберите свободную дату публикации → свяжитесь с @lena_solodkova → оплатите заказ. '
    #                    'Дату бронирую сразу после оплаты.\n\n'
    #                    'Также я открыта к взаимному пиару — подробности готова обсуждать в личке 🤝',
    'offer_vacancy': 'В «Копилке текстов» вы можете <b>бесплатно разместить вакансию</b>, которая актуальна'
                     ' подписчикам — копирайтерам, редакторам, журналистам, UX-редакторам.\n\n'
                     'Вот как они распределены в процентом соотношении: t.me/smotri_kakoi_text/125\n\n'
                     '<b>Пришлите в ответном сообщении описание вакансии</b> 👇🏻\n'
                     'Обязательно укажите ключевые задачи, формат работы (удалёнка или офис) и оплаты '
                     '(примерная вилка, оформление по ТК, ГПХ или фриланс).',
    'message_reply': 'Сообщение от пользователя:',
    'offer_vacancy_warning': 'То, что вы отправили не похоже на текст вакансии\n\n'
                             'Пожалуйста, введите текст вакансии в соответствии в описанием.\n'
                             'Для отмены нажмите - /cancel',
    'offer_vacancy_answer': 'Спасибо! В течение двух дней я приду к вам в '
                            'личку за уточнениями и согласованием даты публикации',
    'offer_news': 'Поделитесь своей находкой с подписчиками канала. Пришлите скрин или фото со своим'
                  ' комментарием в одном сообщении 👇🏻',
    'offer_news_warning': 'То, что вы отправили не похоже на новость\n\n'
                          'Пожалуйста, отправьте сообщение в соответствии в описанием\n'
                          'Для отмены нажмите - /cancel',
    'offer_news_answer': 'Спасибо за такую находку!',
    # 'additional_services': 'Я, Лена Солодкова, рулю контент-маркетингом и корпоративным блогом в компании Lerna '
    #                        '(Skillbox 2b2), пишу и редактирую статьи на фрилансе, развиваю личные проекты.\n\n'
    #                        'А ещё веду телеграм-каналы @smotri_kakoi_text и @editor_lena\n\n\n'
    #                        'Варианты сотрудничества\n\n'
    #                        '👩🏻‍💼 <b>Консультация по ведению телеграм-канала — 10 000₽</b>\n\n'
    #                        'Актуально, если вы:\n\n'
    #                        '— ведёте личный канал или канал компании и хотите поменять стратегию, обновить или добавить '
    #                        'воронки, усилить контент;\n'
    #                        '— только планируете завести канал.\n\n'
    #                        'Мы предварительно созваниваемся и обсуждаем запрос, далее я собираю и структурирую идеи, '
    #                        'затем мы снова созваниваемся на брейншторм и обсуждение. После поддерживаем общение в '
    #                        'чатике — я готова помогать с оформлением конкретных постов и отвечать на точечные '
    #                        'вопросы.\n\n'
    #                        'Подробности и бронь в личке @lena_solodkova\n\n\n'
    #                        '👩‍🏫 Менторство — 18 000₽\n\n'
    #                        '1 месяц активной работы над вашим портфолио, личным брендом, поиском новой работы или '
    #                        'заказчиков. Будем делать упор на практику и реальный заработок в моменте.\n\n'
    #                        'Актуально для тех, кто:\n\n'
    #                        '— хочет найти работу в сфере копирайтинге или digital-маркетинга, новых заказчиков, выйти '
    #                        'на новый уровень дохода;\n'
    #                        '— обновить или создать портфолио;\n'
    #                        '— завести личный блог,  развивать личный бренд с его помощью;\n'
    #                        '— побороть писательский ступор, перестать писать в стол.\n\n'
    #                        'Формат взаимодействия: общение в чате, еженедельные созвоны. Длительность активного '
    #                        'менторства 1 месяц. Но на связи остаёмся и после.\n\n'
    #                        'Подробности и бронь в личке @lena_solodkova',
    'no_command_text': 'Извините, я не понял команды.\n\nДля перехода в меню нажмите - /menu',
    'subscribe_btn': '🎓 Оформить подписку на клуб\n\n '
                     '<b>Клуб копирайтеров и редакторов «Копилка текстов»</b>\n\n'
                     'Клуб — это: \n\n'
                     '• комьюнити и нетворкинг\n'
                     '• образовательные эфиры 2 раза в месяц\n'
                     '• вакансии и подготовка к отклику или собеседованию\n'
                     '• обмен задачами на фриланс\n'
                     '• совместные проекты каждые 3-4 месяца\n'
                     '• обратная связь по текстам и брейнштормы\n\n'
                     '<a href="https://t.me/editor_lena_cooperation/7">Отзывы участников клуба → </a>\n\n'
                     'Подписка стоит 590 рублей в месяц\n\n'
                     'Присоединяйтесь к нам: https://paywall.pw/wvxrvzlzdzxk',
    'buy_advertising': '💵 Купить рекламу\n\n'
                       'На канале есть реклама.\n\n'
                       'Реклама идёт отдельным постом. Подборки админ самостоятельно не собирает. Маркировка может '
                       'быть с вашей стороны или со стороны «Копилки».\n\n'
                       'Сотрудничаем с каналами и брендами. Открыты к ВП.\n\n'
                       'Пишите менеджеру Еве @HeDjisu — она подскажет стоимость и свободные даты. '
                       'Присылайте сразу ссылку на то, что хотите прорекламировать. ',
    'sign_up_for_mentoring_btn': '🫱🏻‍🫲🏻 Записаться на менторство\n\n'
                                 'Менторство — это месяц активной работы с Леной Солодковой над вашим портфолио, личным'
                                 'брендом, поиском новой работы или заказчиков. Будем делать упор на практику и реальный '
                                 'заработок в моменте.\n\n'
                                 'Лена — редактор и маркетолог, автор проекта «Копилка текстов» и «Админское», '
                                 'главный редактор блога Lerna (b2b Skillbox) и просто общительный человек с большой '
                                 'базой клиентов.\n\n'
                                 'Актуально для тех, кто:\n\n'
                                 '• хочет найти работу в сфере копирайтинге или digital-маркетинга, новых заказчиков, '
                                 'выйти на новый уровень дохода;\n'
                                 '• обновить или создать портфолио;\n'
                                 '• завести личный блог, развивать личный бренд с его помощью;\n'
                                 '• побороть писательский ступор, перестать писать в стол.\n\n'
                                 'Формат взаимодействия: общение в чате, еженедельные созвоны. Длительность активного '
                                 'менторства 1 месяц. Но на связи остаёмся и после.\n\n'
                                 'Менторство поможет вам научиться работать с новыми для себя форматами, найти'
                                 ' работу и начать зарабатывать больше. Разнообразить ваше портфолио и увеличить ваш '
                                 'заработок — главная цель менторства.\n\n'
                                 'Стоимость: 18 000 рублей\n\n'
                                 '<a href="https://t.me/editor_lena_cooperation/6">Отзывы на менторство →</a>\n\n'
                                 'Пишите автору менторства — Лена расскажет подробности @lena_solodkova'
}
