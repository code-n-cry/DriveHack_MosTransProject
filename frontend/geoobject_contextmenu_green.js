ymaps.ready(init);

function init () {
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

    coords = [21.324580, 0.951634];
    myPlacemark = new ymaps.Placemark(coords,{}, {preset: "islands#redIcon", draggable: true});    
 
    myMap.geoObjects.add(myPlacemark);  

    myPlacemark.events.add("dragend", function (e) {            
        coords = this.geometry.getCoordinates();
        savecoordinats();
        return coords;
        }, myPlacemark);

        //Отслеживаем событие щелчка по карте
    myMap.events.add('click', function (e) {        
        coords = e.get('coords');
        myPlacemark.geometry.setCoordinates(coords ); 
        return coords;
        });    
    
}
var select = document.getElementById('type_change')
select.getElementById('type_change').onchange = function() {
    if (select.options[select.SelectedIndex].value === 'ЖК') {
        let input = document.createElement('p')
        input.innerHTML = `<label>Зданий в ЖК: </label><input id="floors" class="form-control" name="icon_text" />`
        document.body.insertBefore(input, document.getElementById('station'))
    }
}