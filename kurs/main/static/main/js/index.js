//Функция создания таблицы расписания
function generateTable (lessons) {
    document.getElementById("lessonsTable").innerHTML = "";
    var data
    let timearr = ["08.30-10.00", "10.10-11.40", "12.10-13.40","14.10-15.40","15.50-17.20","17.30-19.00","19.10-20.40"];
    var html = '<table class=Table1><tr class="firstRow"><th></th><th>Понедельник</th><th>Вторник</th><th>Среда</th><th>Четверг</th><th>Пятница</th><th>Суббота</th></tr>';
    for (var t = 0; t < 7; t++) {
        html+='<tr><th class=Time>'+timearr.shift()+'</th>'
        for(var d=0;d < 6; d++){
        data = lessons.slice()
        html+='<td>';
            for (var l=0;l<lessons.length;l++) {
                var curless=data.shift();
                if (curless.time==t && curless.day==d){
                    if (curless.week==0){ //присваиваем класс в зависимости от недели
                        html+='<div class ="bothWeek">';
                        }
                    else if(curless.week==1){
                        html+='<div class ="upWeek">';
                        }
                    else{
                        html+='<div class ="botWeek">';
                        }
                    html+='<div class ="subject" data-toggle="tooltip" data-placement="bottom" title="'+curless.name+'">'+curless.name+'</div>';
                    if(curless.teacher!=null){
                        html+='<div class ="teacher">'+curless.teacher+'</div>';
                        }
                    if(curless.classroom!=null){
                    html+='<div class ="classroom">'+curless.classroom+'</div>';
                    }
                    html+='</div>';

                }
            }
        html+='</td>';
        }
        html+='</tr>';
    }
    html += '</table>';
    document.getElementById("lessonsTable").innerHTML = html;
}

function loadNews(news){
    var html ="";
    var data=news.slice();
    for (var i = 0; i < news.length; i++) {
        var curNews=data.shift();
        html+='<div class ="newsBlock">';
        html+='<h2>'+curNews.header+'</h2>'
        html+=curNews.text;
        html+='</div>';
    }
      document.getElementById("newsPanel").innerHTML = html;
}