ymaps.ready(init);

function init () {
    var coords = [55.776882, 37.581352]
    // Создаем карту.
    var myMap = new ymaps.Map("map", {
            center: [55.776882, 37.581352],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        });

    // Создаем метку.
    var myPlacemark = new ymaps.Placemark([55.776882, 37.581352], {
        iconContent:'Ст. Метро Белорусская'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu').css('display') == 'block') {
            $('#menu').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс.чел./час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark);

// Создаем метку.
    var myPlacemark3 = new ymaps.Placemark([55.77378, 37.54412], {
        iconContent:'Ст. Метро Беговая'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark3.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu1').css('display') == 'block') {
            $('#menu1').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu1">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс.чел./час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu1').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu1 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu1').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark3);

// Создаем метку.
    var myPlacemark4 = new ymaps.Placemark([55.774584, 37.560923], {
        iconContent:'Дорога из центра'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark4.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu2').css('display') == 'block') {
            $('#menu2').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu2">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu2').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu2 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu2').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark4);

    // Создаем метку.
    var myPlacemark5 = new ymaps.Placemark([55.775503, 37.571737], {
        iconContent:'Дорога в центр'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark5.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu3').css('display') == 'block') {
            $('#menu3').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu3">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu3').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu3 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu3').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark5);

    // Создаем метку.
    var myPlacemark6 = new ymaps.Placemark([55.773229, 37.554314], {
        iconContent:'Дорога'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark6.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu4').css('display') == 'block') {
            $('#menu4').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu4">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu4').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu4 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu4').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark6);

    // Создаем метку.
    var myPlacemark7 = new ymaps.Placemark([55.770859, 37.567703], {
        iconContent:'Дорога из центра'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark7.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu5').css('display') == 'block') {
            $('#menu5').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu5">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu5').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu5 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu5').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark7);

    // Создаем метку.
    var myPlacemark8 = new ymaps.Placemark([55.772581, 37.572870], {
        iconContent:'Дорога в центр'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark8.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu6').css('display') == 'block') {
            $('#menu6').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu6">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu6').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu6 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu6').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark8);

    // Создаем метку.
    var myPlacemark9 = new ymaps.Placemark([55.773887, 37.579179], {
        iconContent:'Дорога из центра'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark9.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu7').css('display') == 'block') {
            $('#menu7').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu7">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu7').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu7').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark9);

    // Создаем метку.
    var myPlacemark10 = new ymaps.Placemark([55.775097, 37.582827], {
        iconContent:'Дорога в центр'
    }, {
        // Красная иконка, растягивающаяся под содержимое.
        preset: "islands#greenStretchyIcon"
    });

    // Контекстное меню, позволяющее изменить параметры метки.
    // Вызывается при нажатии правой кнопкой мыши на метке.
    myPlacemark10.events.add('contextmenu', function (e) {
        // Если меню метки уже отображено, то убираем его.
        if ($('#menu7').css('display') == 'block') {
            $('#menu7').remove();
        } else {
            // HTML-содержимое контекстного меню.
            var menuContent =
                '<div id="menu7">\
                    <ul id="menu_list">\
                        <li>Пиковая нагрузка:</li>\
                        <li>9,6</li>\
                        <li>тыс. авто/час пик</li>\
                        <li>53%</li>\
                    </ul>\
                </div>';

            // Размещаем контекстное меню на странице
            $('body').append(menuContent);

            // Задаем позицию меню.
            $('#menu7').css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $('#menu7 input[type="submit"]').click(function () {
                // Удаляем контекстное меню.
                $('#menu7').remove();
            });
        }
    });

    myMap.geoObjects.add(myPlacemark10);

    coords = [21.324580, 0.951634];
    myPlacemark1 = new ymaps.Placemark(coords,{}, {preset: "islands#redIcon", draggable: true});
 
    myMap.geoObjects.add(myPlacemark1);

    myPlacemark1.events.add("dragend", function (e) {
        coords = this.geometry.getCoordinates();
        myPlacemark1.geometry.setCoordinates(coords );
        
        return coords;
        }, myPlacemark1);

        //Отслеживаем событие щелчка по карте
    myMap.events.add('click', function (e) {        
        coords = e.get('coords');
        myPlacemark1.geometry.setCoordinates(coords );
        return coords;
        
        });    

    var select = document.getElementById('metro_station');
    select.onchange = function(){
        console.log(select.value)
        if (select.value === 'Беговая'){
            myMap.setCenter([55.771150, 37.543381])
        }
        else if (select.value === 'Белорусская'){
            myMap.setCenter([55.776882, 37.581352])
        }
    }
}
