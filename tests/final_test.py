import pytest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

driver = webdriver.Chrome(executable_path="chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.labirint.ru/")

main_button_data = [
    {"link": "Книги", "class_name": "genre-name", "expected_text": "Книги"},
    {"link": "Школа", "class_name": "school-cap__header", "expected_text": "Все учебники в Лабиринте"},
    {"link": "Игрушки", "class_name": "genre-name", "expected_text": "Игры и игрушки"},
    {"link": "Канцтовары", "class_name": "genre-name", "expected_text": "Канцелярские товары"}
]


@pytest.mark.parametrize("data", main_button_data)
def test_main_button(data):
    # Параметризованныей тест на кнопки основного меню. 4 теста

    btn = driver.find_element_by_link_text(data.get("link"))
    btn.click()

    result = driver.find_elements_by_class_name(data.get("class_name"))[0].text
    assert result == data.get("expected_text")


book_data = [
    "Билингвы и книги на иностранных языках",
    "Книги для детей",
    "Комиксы, Манга, Артбуки",
    "Молодежная литература",
    "Нехудожественная литература",
    "Периодические издания",
    "Религия",
    "Учебная, методическая литература и словари",
    "Художественная литература",
    "Главные книги отдела"
]


def test_open_book():
    # Проверяем открытие страницы книг по явной ссылке
    driver.get("https://www.labirint.ru/books/")
    driver.find_elements_by_class_name("genre-name")


@pytest.mark.parametrize("link", book_data)
def test_link_book(link):
    btn = driver.find_element_by_link_text(link)
    assert btn is not None


def test_open_school():
    # Проверяем открытие страницы Школа по явной ссылке
    driver.get("https://www.labirint.ru/school/")
    driver.find_elements_by_class_name("school-cap__header")


school_data = [
    "Все для школы",
    "Учебники",
    "ЕГЭ",
    "ВПР",
    "Подготовка к школе",
    "Канцтовары"
]


@pytest.mark.parametrize("link", school_data)
def test_link_school(link):
    btn = driver.find_element_by_link_text(link)
    assert btn is not None


def test_open_child_handmade():
    # Проверяем ссылки в раздел детское творечество
    driver.get("https://www.labirint.ru/games/")
    btn = driver.find_element_by_link_text("Детское творчество")
    btn.click()


handmade_data = [
    "Алмазные мозаики",
    "Гравюры",
    "Другие виды творчества",
    "Конструирование из бумаги и другого материала",
    "Лепка",
    "Наборы для рукоделия",
    "Наклейки детские",
    "Скрапбук",
    "Сопутствующие товары для детского творчества",
    "Творческие наборы для раскрашивания"
]


@pytest.mark.parametrize("link", handmade_data)
def test_child_handmade(link):
    btn = driver.find_element_by_link_text(link)
    assert btn is not None


def test_open_games():
    # Проверяем ссылки в раздел детское творечество
    driver.get("https://www.labirint.ru/games/")
    btn = driver.find_element_by_link_text("Игры и Игрушки")
    btn.click()


games_data = [
    "Все для праздника",
    "Головоломки",
    "Игрушки для самых маленьких",
    "Книжки-игрушки",
    "Конструкторы",
    "Магнитные буквы, цифры, игры",
    "Настольные игры",
    "Научные игры для детей",
    "Пазлы",
    "Сборные модели"
]


@pytest.mark.parametrize("link", games_data)
def test_games(link):
    btn = driver.find_element_by_link_text(link)
    assert btn is not None


def test_find_book():
    driver.find_element_by_link_text("Книги")
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.send_keys("Гарри Поттер")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    count_string = driver.find_element_by_css_selector(
        "#stab-slider-frame > ul > li.b-stab-e-slider-item.b-stab-e-slider-item-m-active > a > span.b-stab-e-slider-item-e-txt-m-small.js-search-tab-count").text
    count = int(count_string)
    assert count > 0


def test_find_fake_book():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys("blablablablablabla")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    error_element = driver.find_elements_by_class_name("search-error")
    assert error_element is not None


def test_find_fake_backspace():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys("   ")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    error_element = driver.find_elements_by_class_name("search-error")
    assert error_element is not None


def test_find_many_simbols():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys(
        "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    error_element = driver.find_elements_by_class_name("search-error")
    assert error_element is not None



def test_find_paints():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys("Раскраска")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    count_string = driver.find_element_by_css_selector(
        "#stab-slider-frame > ul > li.b-stab-e-slider-item.b-stab-e-slider-item-m-active > a > span.b-stab-e-slider-item-e-txt-m-small.js-search-tab-count").text
    assert count_string is not None


def test_find_phones():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys("Телефон")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    count_string = driver.find_element_by_css_selector(
        "#stab-slider-frame > ul > li.b-stab-e-slider-item.b-stab-e-slider-item-m-active > a > span.b-stab-e-slider-item-e-txt-m-small.js-search-tab-count").text
    assert count_string is not None


def test_find_bear():
    search_field = driver.find_element_by_css_selector("#search-field")
    search_field.clear()
    search_field.send_keys("Медведь")
    btn = driver.find_element_by_class_name("b-header-b-search-e-btntxt")
    btn.click()
    count_string = driver.find_element_by_css_selector(
        "#stab-slider-frame > ul > li.b-stab-e-slider-item.b-stab-e-slider-item-m-active > a > span.b-stab-e-slider-item-e-txt-m-small.js-search-tab-count").text

    assert count_string is not None

    driver.close()
    driver.quit()