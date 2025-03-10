from unicodedata import category
from django.shortcuts import render

from goods.models import Categories



# Create your views here.
def index(request):

    context = {
        'title': 'R&R',
        'content': 'RentRelay — Аренда вещей',
    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'R&R',
        'title_page': 'О нас — RentRelay',
        'content': 'Информация о проекте',
        'text_on_page': """
        <h3>Добро пожаловать в RentRelay</h1>
        <p>RentRelay — платформа, которая превращает аренду вещей в удобный и доступный процесс!</p>

        <p>Мы понимаем, что не все вещи нужны постоянно. Иногда вам может понадобиться инструмент для ремонта, стильный костюм для мероприятия или гаджет для работы. Зачем покупать то, что можно легко взять в аренду? <strong>RentRelay</strong> создан, чтобы помочь вам арендовать нужное и делиться своими вещами с другими, делая жизнь проще и экономичнее.</p>

        <h3>Наша миссия</h3>
        <p>Мы стремимся к тому, чтобы каждый мог получить доступ к вещам, которые ему нужны, без необходимости покупать их. Это не только выгодно для вашего бюджета, но и помогает сократить избыточное потребление, что важно для экологии.</p>

        <h3>Что мы предлагаем?</h3>
        <ul>
            <li><strong>Широкий выбор вещей:</strong> инструменты, техника, мебель, одежда и многое другое.</li>
            <li><strong>Удобный процесс аренды:</strong> выбирайте, бронируйте и пользуйтесь вещами, когда они вам нужны.</li>
            <li><strong>Безопасность и доверие:</strong> мы заботимся о том, чтобы каждая сделка была безопасной, а все участники чувствовали себя уверенно.</li>
        </ul>

        <h3>Почему выбирают RentRelay?</h3>
        <ul>
            <li><strong>Экономия:</strong> аренда дешевле, чем покупка.</li>
            <li><strong>Экология:</strong> меньше покупок — меньше отходов.</li>
            <li><strong>Сообщество:</strong> мы объединяем людей, которые готовы делиться и помогать друг другу.</li>
        </ul>

        <h3>Присоединяйтесь к нам!</h3>
        <p>С RentRelay вы получаете больше возможностей, затрачивая меньше ресурсов. Будь то временная необходимость или уникальный случай — мы здесь, чтобы помочь.</p>

        <p>Спасибо, что выбираете нас!<br>Ваш <strong>RentRelay</strong>.</p>
        """

    }
    return render(request, 'main/about.html', context)


def contacts(request):
    context = {
        'title': 'R&R',
        'title_page': 'Контактная информация — RentRelay',
        'content': 'Свяжитесь с нами',
        'text_on_page': """
        <p>Мы всегда готовы помочь! Если у вас возникли вопросы, предложения или трудности при использовании платформы <strong>RentRelay</strong>, наша служба поддержки с радостью вам поможет.</p>

        <p><strong>📞 Телефон поддержки:</strong><br>
        +7 (123) 456-78-90 (с 9:00 до 21:00 по МСК)</p>

        <p><strong>✉️ Электронная почта:</strong><br>
        <a href="mailto:support@rentrelay.com">support@rentrelay.com</a></p>

        <p><strong>💬 Онлайн-чат:</strong><br>
        Задавайте вопросы через онлайн-чат на сайте. Мы стараемся отвечать в течение нескольких минут!</p>

        <p><strong>📍 Адрес офиса:</strong><br>
        Москва, ул. Примерная, д. 1, офис 101</p>

        <p>Мы ценим каждого пользователя и стремимся сделать ваш опыт максимально удобным! Спасибо, что выбираете <strong>RentRelay</strong>. 😊</p>
        """

    }
    return render(request, 'main/contacts.html', context)


def delivery(request):
    context = {
        'title': 'R&R',
        'title_page': 'Доставка и оплата — RentRelay',
        'content': 'Условия доставки и оплаты RentRelay',
        'text_on_page': """
        <p>На платформе <strong>RentRelay</strong> пользователи могут сдавать свои вещи в аренду, зарабатывая валюту, которую затем могут потратить на аренду других вещей. Мы стремимся сделать процесс аренды удобным и безопасным для всех.</p>

        <h3>📦 Условия доставки</h3>
        <p>Доставка вещей осуществляется с помощью партнерских курьерских служб. Мы гарантируем, что ваши вещи будут доставлены в целости и сохранности. Вот как это работает:</p>
        <ul>
            <li><strong>Заказ на доставку:</strong> После подтверждения аренды, вы можете выбрать удобное время для доставки.</li>
            <li><strong>Территория доставки:</strong> Мы осуществляем доставку по всей России. При заказе на аренду вещей в другой город, уточняйте возможные условия доставки.</li>
            <li><strong>Стоимость доставки:</strong> Стоимость доставки рассчитывается в зависимости от расстояния и веса вещи. Точную стоимость можно увидеть при оформлении заказа.</li>
            <li><strong>Время доставки:</strong> Время доставки зависит от доступности курьерских служб и дальности пункта назначения.</li>
        </ul>

        <h3>💳 Условия оплаты</h3>
        <p>Мы предлагаем удобные способы оплаты для аренды и доставки вещей:</p>
        <ul>
            <li><strong>Оплата через банковскую карту:</strong> Вы можете оплатить аренду и доставку через вашу банковскую карту, используя безопасную платежную систему.</li>
            <li><strong>Оплата в валюте платформы:</strong> Если у вас есть валюта платформы RentRelay, вы можете использовать её для оплаты аренды или доставки. Валюта зарабатывается при сдаче вещей в аренду.</li>
            <li><strong>Безопасность оплаты:</strong> Все транзакции на нашей платформе защищены с помощью современных технологий шифрования, чтобы гарантировать безопасность ваших данных.</li>
            <li><strong>Возврат средств:</strong> В случае отмены аренды или доставки, возврат средств возможен в течение 7 рабочих дней.</li>
        </ul>

        <p>Мы ценим наших пользователей и стараемся обеспечить максимальную прозрачность и удобство при оформлении аренды. Если у вас возникли вопросы по условиям доставки или оплаты, не стесняйтесь обращаться в нашу службу поддержки!</p>

        <p>Спасибо, что выбираете <strong>RentRelay</strong>! 😊</p>
        """

    }
    return render(request, 'main/delivery.html', context)