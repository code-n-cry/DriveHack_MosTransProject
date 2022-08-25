var coords = [21.324580, 0.951634]

ymaps.ready(init);
function init () {
    var myMap = new ymaps.Map("map", {
            center: [55.776882, 37.581352],
            zoom: 16
        }, {
            searchControlProvider: 'yandex#search'
        });
    function addMark(coords, iconContentVal, presetVal, menuContentVal, elemTag, percent){
        var myPlacemark = new ymaps.Placemark(coords, {
        iconContent: iconContentVal
    }, {
        preset: presetVal
    });
        myPlacemark.events.add('contextmenu', function (e) {
        if ($(elemTag).css('display') == 'block') {
            $(elemTag).remove();
        } else {
            var menuContent = menuContentVal
            $('body').append(menuContent);
            $(elemTag).css({
                left: e.get('pagePixels')[0],
                top: e.get('pagePixels')[1]
            });

            $(`${elemTag} input[type="submit"]`).click(function () {
                $(elemTag).remove();
            });
        }
    });
    myMap.geoObjects.add(myPlacemark);
    
    return percent;
    
    }
    var mark1 = addMark([55.776882, 37.581352], 'Ст. Метро Белорусская', "islands#greenStretchyIcon", '<div id="menu">\ <ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс.чел./час пик</li>\<li>53%</li>\</ul>\</div>', '#menu', 30)
    
    var mark2 = addMark([55.77378, 37.54412], 'Ст. Метро Беговая', "islands#greenStretchyIcon", '<div id="menu1">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс.чел./час пик</li>\<li>53%</li>\</ul>\</div>', "#menu1" )
    var mark3 = addMark([55.774584, 37.560923], 'Дорога из центра', "islands#greenStretchyIcon", '<div id="menu2">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', "#menu2")
    var mark4 = addMark([55.775503, 37.571737], "Дорога в центр", "islands#greenStretchyIcon", '<div id="menu3">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', "#menu3")
    var mark5 = addMark([55.773229, 37.554314], "Дорога", "islands#greenStretchyIcon", '<div id="menu4">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', '#menu4' )
    var mark6 = addMark([55.770859, 37.567703], "Дорога из центра", "islands#greenStretchyIcon", '<div id="menu5">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', '#menu5' )
    var mark7 = addMark([55.772581, 37.572870], "Дорога в центр", "islands#greenStretchyIcon", '<div id="menu6">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', "#menu6")
    var mark8 = addMark([55.773887, 37.579179], "Дорога из центра", "islands#greenStretchyIcon", '<div id="menu7">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', '#menu7')
    var mark9 = addMark([55.775097, 37.582827], "Дорога в центр", "islands#greenStretchyIcon", '<div id="menu8">\<ul id="menu_list">\<li>Пиковая нагрузка:</li>\<li>9,6</li>\<li>тыс. авто/час пик</li>\<li>53%</li>\</ul>\</div>', '#menu8' )
    myPlacemark1 = new ymaps.Placemark([21.324580, 0.951634],{}, {preset: "islands#redIcon", draggable: true});
    
    
    myMap.geoObjects.add(myPlacemark1);
    myPlacemark1.events.add("dragend", function (e) {
        let coords = this.geometry.getCoordinates();
        myPlacemark1.geometry.setCoordinates(coords );
        
        return coords;
        }, myPlacemark1);

    myMap.events.add('click', function (e) {        
        let coords = e.get('coords');
        myPlacemark1.geometry.setCoordinates(coords );
        return coords;
        
        }); 

    var select = document.getElementById('station');
    select.onchange = function(){
        console.log(select.value)
        if (select.value === 'Беговая'){
            myMap.setCenter([55.771150, 37.543381])

            
        }
        else if (select.value === 'Белорусская'){
            myMap.setCenter([55.776882, 37.581352])
        }
        
    }
    function changeColor(id, color, mark){
        var element = document.getElementById(id);
        alert('зашел в функцию')
        if (mark <= 40){
            element.style.background = 'green';
            alert('в условии')
        }
        else if (mark > 40 && mark <= 65){
            element.style.background = 'yellow'
            alert('в условии')
        }
        else if (mark > 65){
            element.style.background = 'red'
            alert('в условии')
        }
    }

    mark1 = changeColor('#menu', mark1)
    
}
var select = document.getElementById('type_change');
var btn = document.getElementById('ok_btn')
select.onchange = function () {
    if (select.value === 'ЖК') {
            document.getElementById('qnt').style.visibility = 'visible'
    } else {
            document.getElementById('qnt').style.visibility = 'hidden'
    }
}
btn.onclick = function () {
    let type = select.value
    let dict = {
        "ЖК": "/api/houses/",
        "Жилое": "/api/house/",
        "Отель": "/api/hotel/",
        "Офис": "/api/office/",
    }
    let area = document.getElementById('square').value
    let floors = document.getElementById('floors').value
    let distance = 200
    let important = 2
    if (type === 'ЖК') {
        let houses = document.getElementById('houses').value
    }
    let json = { 'area': area, 'floors': floors, 'type': type, 'coeff': 0.2, 'important_num': important, 'distance': distance }
    fetch(dict[select.value], { method: 'POST', body: JSON.stringify(json) })
}
