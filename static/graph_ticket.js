/** * Created by Александра on 19.06.2017. */var chart = AmCharts.makeChart("chartdiv_ticket", {  "type": "serial",  "theme": "light",  "marginRight": 70,  "dataProvider": [/**тут инфа*/{"country": "ТЕАТРЫ МОСКВЫ","visits": 12,"color": "#468ccf"},{"country": "ТЕАТР КВАРТЕТ И","visits": 0,"color": "#468ccf"},{"country": "Театр НИУ ВШЭ","visits": 5,"color": "#468ccf"},{"country": "Театр балета Бориса Эйфмана","visits": 0,"color": "#468ccf"},{"country": "Bolshoi Theatre of Russia / Большой театр России","visits": 1,"color": "#468ccf"},{"country": "Михайловский театр","visits": 0,"color": "#468ccf"},{"country": "Молодежный ТЕАТР НА БУЛАКЕ Казань","visits": 16,"color": "#468ccf"},{"country": "Пермский театр У Моста","visits": 0,"color": "#468ccf"},{"country": "Театральная Вешалка","visits": 5,"color": "#468ccf"},{"country": "ОДИН ТЕАТР","visits": 3,"color": "#468ccf"},{"country": "ВОЛКОВСКИЙ ТЕАТР","visits": 1,"color": "#468ccf"},{"country": "Театр Красный факел","visits": 26,"color": "#468ccf"},{"country": "Московский театр мюзикла","visits": 2,"color": "#468ccf"},{"country": "Санкт-Петербургский театр Мастерская","visits": 4,"color": "#468ccf"},/**тут инфа кончилась*/],  "valueAxes": [{    "axisAlpha": 0,    "position": "left",    "title": "Средняя длинна предложений"  }],  "startDuration": 1,  "graphs": [{    "balloonText": "<b>[[category]]: [[value]]</b>",    "fillColorsField": "color",    "fillAlphas": 0.9,    "lineAlpha": 0.2,    "type": "column",    "valueField": "visits"  }],  "chartCursor": {    "categoryBalloonEnabled": false,    "cursorAlpha": 0,    "zoomable": false  },  "categoryField": "country",  "categoryAxis": {    "gridPosition": "start",    "labelRotation": 90  },  "export": {    "enabled": true  }});