https://starper55plys.ru/shpargalki/
https://webref.ru/html/a
http://htmlbook.ru/html/value/script
https://htmlbase.ru/html/a
https://html5css.ru/tags/ref_byfunc.php


# Справочник CSS
Стилем или CSS (Cascading Style Sheets, каскадные таблицы стилей) называется набор параметров форматирования, который применяется к элементам документа, чтобы изменить их внешний вид.


# Справочник HTML
HTML (HyperText Markup Language, язык разметки гипертекста) — это система вёрстки, которая определяет, как и какие элементы должны располагаться на веб-странице. Информация на сайте, способ её представления и оформления зависят исключительно от разработчика и тех целей, которые он перед собой ставит.

Каркас HTML документа по версии HTML5
```
<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="utf-8" />
<title>Документ без названия</title>
</head>
<body>
Контент
</body>
</html>
```
Всем тегам HTML в браузерах, по умолчанию, присвоено свойство `display:`, результатом чего существует разделение элементов на блочные и встроенные или строчные.




### Служебные теги
<details> 
  <summary>Служебные теги </summary>

- #### `<!DOCTYPE>`	Определяет тип документа	`none`
- #### `<head></head>`	Контейнер в начале страницы для служебных тегов и подгружаемых функций	`none`
- #### `<title></title>`	Заголовок документа отображаемый во вкладке браузера	`none`
- #### `<meta>`	Метаданные страницы	`none`
- #### `<link>`	Подключает внешние сервисы и таблицы стилей	`none`
- #### `<script></script>`	Подключает скрипты к станице	`none`
- #### `<style></style>`	Подключает глобальные стили к странице	`none`
- #### `<base>`	Базовый URL-адрес — домен	`none`
- #### `<noscript></noscrip>`	Блок не поддерживающий скрипты	`block`
</details>


### Структурные блоки
<details> 
  <summary>Структурные блоки </summary>


- #### `<body></body>`	Тело html документа	`block`
- #### `<main><main>`	Контейнер для всего содержимого страницы	`block`
- #### `<nav></nav>`	Контейнер для навигационного меню	`block`
- #### `<header><header>`	Шапка сайта	`block`
- #### `<article></article>`	Блок основного контента, обычно статья	`block`
- #### `<section></section>`	Часть контента с заголовком	`block`
- #### `<aside></aside>`	Часть контента, имеющая косвенное отношение к основному	`block`
- #### `<footer></footer>`	Подвал страницы	`block`
- #### `<div>`	Применяется для создания блочных контейнеров	`block`
- #### `<span></span>`	Применяется для создания встроенных контейнеров	`block`
- #### `<figure></figure>`	Независимый контейнер. Преимущественно для изображений	`block`
- #### `<figcaption></figcaption>`	Заголовок для figure	`block`
- #### `<details></details>`	Контейнер с дополнительной информацией, который можно свернуть или развернуть	`block`
- #### `<summary></summary>`	Заголовок для details, по которому можно щёлкать, чтоб свернуть или развернуть блок	`block`
</details>


### Текст
<details> 
  <summary>Текст </summary>

- #### `<h1></h1>…<h6></h6>`	Заголовки шесть уровней	`block`
- #### `<p></p>`	Абзац	`block`
- #### `<br>`	Перенос строки	`block`
- #### `<wbr>`	Возможное место разрыва строки	`none`
- #### `<hr>`	Прямая линия	`none`
- #### `<blockquote></blockquote>`	Цитата	`block`
- #### `<q></q>`	Краткая цитата	`inline`
- #### `<cite></cite>`	Источник цитирования	`inline`
- #### `<code></code>`	Фрагмент кода	`inline`
- #### `<pre></pre>`	Неформатированнй код	`block`
- #### `<kbd></kbd>`	Текст моноширным шрифтом	`inline`
- #### `<samp></samp>`	Результат выполнения скрипта	`inline`
- #### `<var></var>`	Выделяет переменные из программ	`inline`
- #### `<del></del>`	Зачёркнутый текст помечается как удалённый	`inline`
- #### `<s></s>`	Зачёркнутый текст	`block`
- #### `<ins><ins>`	Подчёркивает изменения в тексте	`inline`
- #### `<u></u>`	Подчёркнутый текст	`inline`
- #### `<dfn></dfn>`	Выделяет термин курсивом	`inline`
- #### `<em></em>`	Выделяет курсивом важные фрагменты текста	`inline`
- #### `<i></i>`	Выделяет текст курсивом	`inline`
- #### `<strong></strong>`	Выделяет важный текст полужирным	`inline`
- #### `<b></b>`	Выделяет текст полужирным	`inline`
- #### `<mark></mark>`	Выделяет фрагмент текста жёлтым фоном	`inline`
- #### `<small></small>`	Уменьшает размер шрифта	`inline`
- #### `<sub></sub>`	Подстрочное написание H2O	`inline`
- #### `<sup></sup>`	Надстрочное написание R2	`inline`
- #### `<time><time>`	Дата, время выпуска статьи	`inline`
- #### `<abbr></abbr>`	Аббревиатура	`inline`
- #### `<address></address>`	Адрес автора статьи	`inline`
- #### `<bdi></bdi>`	Изолирует текст читаемый справа на лево. Применяется в текстах написанных на двух языках	`inline`
- #### `<bdo></bdo>`	Задаёт направление написания текста	`inline`
- #### `<ruby></ruby>`	Контейнер для Восточно-Азиатских символов	`inline`
- #### `<rp></rp>`	Используется для вывода текста в браузерах, которые не поддерживают тег . В остальных браузерах текст, заключенный в контейнер	`none`
- #### `<rt></rt>`	Расшифровка символов	`block`
</details>


### Таблицы
<details> 
  <summary>Таблицы </summary>

- #### `<table></table>`	Таблица HTML	table
- #### `<tr></tr>`	Строка таблицы	table-row
- #### `<th></th>`	Ячейки заголовков столбцов таблицы	table-cell
- #### `<td></td>`	Ячейки таблицы	table-cell
- #### `<thead></thead>`	Группа верхних строк таблицы. Применяется для общего оформления	table-header-group
- #### `<tfoot></tfoot>`	Группа нижних строк таблицы. Применяется для общего оформления	table-footer-group
- #### `<tbody></tbody>`	Группа строк в середине таблицы. Применяется для общего оформления	table-row-group
- #### `<col>`	Выделяет столбец таблицы	table-column
- #### `<colgroup></colgroup>`	Группирует несколько столбцов таблицы для общего оформления	table-column-group
- #### `<caption></caption>`	Описание таблицы	table-caption
</details>


### Списки
<details> 
  <summary>Списки </summary>

- #### `<ol></ol>`	Упорядоченный нумерованный список	`block`
- #### `<ul></ul>`	Маркированный список	`block`
- #### `<li></li>`	Элемент списка	list-item
- #### `<dl></dl>`	Список с описаниями	`block`
- #### `<dt></dt>`	Строка списка с описаниями	`block`
- #### `<dd></dd>`	Описание строки, списка с описаниями	`block`
</details>


### Изображения
<details> 
  <summary>Изображения </summary>

- #### `<img>`	Изображение html	`inline`
- #### `<>map</map>`	Активные области на карте	`inline`
- #### `<area></area>`	Активная область с гиперссылкой на карте	`inline`
- #### `<canvas></canvas>`	Холст контейнер для динамического отображения изображений созданных с помощью JavaScript	`inline`-`block`
</details>


### Формы HTML
<details> 
  <summary>Формы HTML </summary>

- #### `<form></form>`	Формы HTML	`block`
- #### `<input></input>`	Многофункциональные поля формы	`inline-block`
- #### `<textarea></textarea>`	Многострочное поле формы	`inline-block`
- #### `<label></label>`	Обычно текст формы	`inline`
- #### `<datalist></datalist>`	Создаёт список вариантов, из которых можно сделать выбор.	`none`
- #### `<option></option>`	Опция в раскрывающемся списке	`block`
- #### `<optgroup></optgroup>`	Контейнер с заголовком для группы `<option>`	`block`
- #### `<select></select>`	Контейнер для создания раскрывающегося списка	`inline-block`
- #### `<fieldset></fieldset>`	Группирует связанные элементы формы	`block`
- #### `<legend></legend>`	Заголовок элементов формы, связанных `<fieldset>`	`block`
- #### `<button></button>`	Интерактивная кнопка	`inline-block`
- #### `<keygen></keygen>`	Генератор ключей	`inline-block`
- #### `<progress></progress>`	Отображает процесс выполнения в числовых значениях	`inline-block`
- #### `<meter></meter>`	Используется для отображения числовых значений таких показателей как количество посетителей, величина давления и т.п.	`inline-block`
- #### `<output></output>`	Поле для вывода результатов вычислений	`inline`
</details>


## Встраиваемые элементы
- #### `<audio></audio>`	Аудио файл	`inline-block`
    <details> 
      <summary>Описание </summary>
  
      Элемент <audio> (от англ. audio — звук) добавляет, воспроизводит и управляет настройками аудиозаписи на веб-странице. Путь к файлу задаётся через атрибут src или вложенный элемент <source>. Внутри контейнера <audio> можно написать текст, который будет выводиться в браузерах, не работающих с этим элементом.

      Для универсального воспроизведения в указанных браузерах аудио кодируют с помощью разных кодеков и добавляют файлы одновременно через элемент <source>.
      
      Управление воспроизведением аудио различается между браузерами по своему виду, но основные элементы совпадают. Это кнопка воспроизведения/паузы, длина трека, прошедшее и суммарное время звучания, а также уровень громкости.
    </details>
    <details> 
      <summary>Синтаксис </summary>

      <audio src="<адрес>"></audio>
      <audio>
       <source src="<адрес>">
      </audio>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
  - `autoplay` - Звук начинает играть сразу после загрузки страницы.
  - `controls` - Добавляет панель управления к аудиофайлу.
  - `loop` - Повторяет воспроизведение звука с начала после его завершения.
  - `muted` - Отключает звук при воспроизведении музыки.
  - `preload` - Используется для предварительной загрузки аудиофайла или его данных вместе с загрузкой веб-страницы.
    - `src` - Указывает путь к воспроизводимому файлу.
      </details>
      <details> 
        <summary>Примеры </summary>
  
          <!DOCTYPE html>
          <html>
           <head>
            <meta charset="utf-8">
            <title>audio</title>
           </head>
           <body>
            <p>Александр Клименков - Четырнадцать</p>
            <audio controls>
              <source src="audio/music.ogg" type="audio/ogg; codecs=vorbis">
              <source src="audio/music.mp3" type="audio/mpeg">
              Тег audio не поддерживается вашим браузером. 
              <a href="audio/music.mp3">Скачайте музыку</a>.
            </audio>
           </body>
          </html>
    
      <!DOCTYPE html>
      <html>
       <head>
        <meta charset="utf-8">
        <title>audio</title>
       </head>
       <body>
        <p>Александр Клименков - Четырнадцать</p>
        <audio controls>
          <source src="audio/music.ogg" type="audio/ogg; codecs=vorbis">
          <source src="audio/music.mp3" type="audio/mpeg">
          Тег audio не поддерживается вашим браузером. 
          <a href="audio/music.mp3">Скачайте музыку</a>.
        </audio>
       </body>
      </html>
      </details>
  
      - #### `<video></video>`	Видео файл	`inline-block`
        <details> 
          <summary>Описание </summary>
  
            Добавляет, воспроизводит и управляет настройками видеоролика на веб-странице. Путь к файлу задаётся через атрибут src или вложенный элемент <source>. Список поддерживаемых браузерами аудио и видеокодеков ограничен и приведён в табл. 1.
            Firefox поддерживает AAC частично — только в контейнере MP4 и когда операционная система поддерживает этот формат.
      
            Для универсального воспроизведения в указанных браузерах видео кодируют с помощью разных кодеков и добавляют файлы одновременно (см. пример).
        </details>
        <details> 
          <summary>Синтаксис </summary>
      
            <video>
             <source src="<адрес>">
            </video>
        </details>

        <details> 
          <summary>Атрибуты </summary>
    
        - `autoplay` - Видео начинает воспроизводиться автоматически после загрузки страницы.
        - `controls` - Добавляет панель управления к видеоролику.
        - `height` - Задаёт высоту области для воспроизведения видеоролика.
        - `loop` - Повторяет воспроизведение видео с начала после его завершения.
        - `poster` - Указывает адрес картинки, которая будет отображаться, пока видео не доступно или не воспроизводится.
        - `preload` - Используется для загрузки видео вместе с загрузкой веб-страницы.
        - `src` - Указывает путь к воспроизводимому видеоролику.
        - `width` - Задаёт ширину области для воспроизведения видеоролика.
        </details>
        <details> 
          <summary>Примеры </summary>
      
            <!DOCTYPE html>
            <html>
             <head>
              <meta charset="utf-8">
              <title>video</title>
             </head>
             <body>
              <video width="400" height="300" controls="controls" poster="video/duel.jpg">
               <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
               <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
               <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
               Элемент video не поддерживается вашим браузером. 
               <a href="video/duel.mp4">Скачайте видео</a>.
              </video>
             </body>
            </html>

          <!DOCTYPE html>
          <html>
           <head>
            <meta charset="utf-8">
            <title>video</title>
           </head>
           <body>
            <video width="400" height="300" controls="controls" poster="video/duel.jpg">
             <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
             <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
             <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
             Элемент video не поддерживается вашим браузером. 
             <a href="video/duel.mp4">Скачайте видео</a>.
            </video>
           </body>
          </html>
        </details>
      
      - #### `<source></source>`	указывает местоположение и тип альтернативных файлов для `<video> и <audio>`	`none`
        <details> 
          <summary>Описание </summary>
  
            Вставляет звуковой или видеофайл для элементов <audio> и <video>. Обобщённо такие файлы называются медийными. Также применяется для добавления изображений в контейнере <picture>
    
            Когда располагается внутри <audio> или <video>, элемент <source> (от англ. source — исходник) должен идти после медийных файлов, но до <track>. Внутри <picture> он должен идти перед <img>.
        </details> 
        <details> 
          <summary>Синтаксис </summary>
    
            <audio>
             <source src="<адрес>">
            </audio>
          
            <video>
             <source src="<адрес>">
            </video>
          
            <picture>
             <source srcset="...">
            </picture>
        </details>
        <details> 
          <summary>Атрибуты </summary>
  
          - `media` - Определяет устройство, для которого будет воспроизводиться файл.
          - `sizes` - Задаёт размеры изображений для разных макетов страницы.
          - `src` - Адрес медиа-файла.
          - `srcset` - Изображения, которые используются в разных ситуациях (для экранов планшетов, для экранов ретина и др.).
          - `type` - MIME-тип медийного источника.
        </details>
        <details> 
          <summary>Примеры </summary>
    
            <!DOCTYPE html>
            <html>
             <head>
              <meta charset="utf-8">
              <title>source</title>
             </head>
             <body>
              <video width="400" height="300" controls="controls">
               <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
               <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
               <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
               Элемент video не поддерживается вашим браузером. 
               <a href="video/duel.mp4">Скачайте видео</a>.
              </video>
             </body>
            </html>
    
        <!DOCTYPE html>
        <html>
         <head>
          <meta charset="utf-8">
          <title>source</title>
         </head>
         <body>
          <video width="400" height="300" controls="controls">
           <source src="video/duel.ogv" type='video/ogg; codecs="theora, vorbis"'>
           <source src="video/duel.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
           <source src="video/duel.webm" type='video/webm; codecs="vp8, vorbis"'>
           Элемент video не поддерживается вашим браузером. 
           <a href="video/duel.mp4">Скачайте видео</a>.
          </video>
         </body>
        </html>
          </details>

      - #### `<track></track>`	Субтитры	`none`
        <details> 
          <summary>Описание </summary>
    
            Элемент <track> (от англ. track — дорожка) позволяет авторам указать текстовую дорожку для медийных элементов <audio> и <video>. Такая дорожка обычно содержит субтитры на разных языках, комментарии, заголовки и др.



            Содержимое файла jane.ru.vtt в формате субтитров VTT приведено ниже.
  
            WEBVTT FILE
            00:00.360 --> 00:01.240
              Солдат Джейн.
  
            00:01.240 --> 00:02.240
              Спасаюсь от радиации.
  
            00:02.240 --> 00:04.000
              Арбуз - лучшее средство.
        </details>
        <details>
          <summary>Синтаксис </summary>
        
            <audio>
              <track kind | src | srclang | label | default>
            </audio>
            <video>
              <track kind | src | srclang | label | default>
            </video>
        </details>
        <details> 
          <summary>Атрибуты </summary>
  
        - `kind` - Указывает тип дорожки, возможные варианты перечислены
          <details>
            <summary>Значения атрибута kind </summary>
        
            - Значение:`subtitles`	/	Предназначение:Субтитры	/	Описание:Предназначены для дублирования звуковой дорожки фильма в виде текста на языке оригинала для глухих людей. Также могут содержать перевод на другие языки для тех, кто не знаком с языком оригинала. Текст субтитров выводится поверх видео.
            - Значение:`captions`	/	Предназначение:Заголовки	/	Описание:Дублирование диалогов, звуковых эффектов, музыкального сопровождения в виде текста для тех случаев, когда звук недоступен или для глухих пользователей. Выводится поверх видео, при этом помечается, что подходит для плохо слышащих людей.
            - Значение:`descriptions`	/	Предназначение:Описание	/	Описание:Звуковое описание происходящего в видео для тех случаев, когда изображение недоступно или для слепых людей.
            - Значение:`chapters`	/	Предназначение:Главы	/	Описание:Названия глав используемые для быстрой навигации по видео или аудио. Отображаются в виде списка.
            - Значение:`metadata`	/	Предназначение:Метаданные	/	Описание:Предназначены для использования скриптами и не отображаются в браузере.
          </details>
        - `src` - Путь к файлу с дорожкой.
        - `srclang` - Язык дорожки. См. коды языков.
        - `label` - Отображаемое название дорожки. Если этот атрибут не указан, браузер станет использовать значение, которое применяется у него по умолчанию, например «untitled1».
        - `default` - Наличие этого атрибута указывает, что данная дорожка предпочтительна и должна быть выбрана по умолчанию. Только одна дорожка может иметь атрибут default.
        </details>
        <details> 
         <summary>Примеры </summary>
        
             <!DOCTYPE html>
             <html>
              <head>
               <meta charset="utf-8">
               <title>track</title>
              </head>
              <body>
               <video width="500" height="400" controls>
                 <source src="video/jane.ogv" type='video/ogg; codecs="theora, vorbis"'>
                 <source src="video/jane.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
                 <source src="video/jane.webm" type='video/webm; codecs="vp8, vorbis"'>
                 <track kind="subtitles" src="video/jane.en.vtt" srclang="en" label="English">
                 <track kind="subtitles" src="video/jane.ua.vtt" srclang="uk" label="Українська">
                 <track kind="subtitles" src="video/jane.ru.vtt" srclang="ru" label="Русский" default>
                  Элемент video не поддерживается вашим браузером.
               </video>
              </body>
             </html>
      
        <!DOCTYPE html>
        <html>
        <head>
         <meta charset="utf-8">
         <title>track</title>
        </head>
        <body>
         <video width="500" height="400" controls>
           <source src="video/jane.ogv" type='video/ogg; codecs="theora, vorbis"'>
           <source src="video/jane.mp4" type='video/mp4; codecs="avc1.42E01E, mp4a.40.2"'>
           <source src="video/jane.webm" type='video/webm; codecs="vp8, vorbis"'>
           <track kind="subtitles" src="video/jane.en.vtt" srclang="en" label="English">
           <track kind="subtitles" src="video/jane.ua.vtt" srclang="uk" label="Українська">
           <track kind="subtitles" src="video/jane.ru.vtt" srclang="ru" label="Русский" default>
            Элемент video не поддерживается вашим браузером.
         </video>
        </body>
        </html>
        </details>
  
      - #### `<embed></embed>`	Встроенный внешний элемент	`inline-block`
        <details> 
          <summary>Описание </summary>
  
            Элемент <embed> (от англ. embed — вставить, внедрить) используется для загрузки и отображения объектов (например, видеофайлов, флэш-роликов, некоторых звуковых файлов и т. д.), которые исходно браузер не понимает. Как правило, такие объекты требуют подключения к браузеру специального модуля, который называется плагин, или запуска вспомогательной программы.
    
            Вид внедрённого объекта зависит от установленных в браузере плагинов, типа загружаемого файла, а также от атрибутов элемента <embed>.
        </details>
        <details>
          <summary>Синтаксис </summary>

            <embed></embed>
        </details>
        <details> 
          <summary>Атрибуты </summary>

        - `align` - Определяет, как объект будет выравниваться на странице и способ его обтекания текстом. 
        - `height` - Высота объекта.
        - `hidden` - Указывает, скрыть объект на странице или нет.
        - `hspace` - Горизонтальный отступ от объекта до окружающего контента. 
        - `pluginspage` - Адрес страницы в Интернете, откуда можно скачать и установить плагин к браузеру.
        - `src` - Путь к файлу.
        - `type` - MIME-тип объекта.
        - `vspace` - Вертикальный отступ от объекта до окружающего контента. 
        - `width` - Ширина объекта.
        </details>
        <details> 
          <summary>Примеры </summary>
         
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <title>EMBED</title>
              </head>
              <body> 
                <embed src="flash/mouse.swf" width="400" height="300" 
                       type="application/x-shockwave-flash"
                       pluginspage="https://get.adobe.com/flashplayer">  
              </body>
            </html>
      
        <!DOCTYPE html>
        <html>
          <head>
            <meta charset="utf-8">
            <title>EMBED</title>
          </head>
          <body> 
            <embed src="flash/mouse.swf" width="400" height="300"
                    type="application/x-shockwave-flash"
                    pluginspage="https://get.adobe.com/flashplayer">
          </body>
        </html>
        </details>
      
      - #### `<object></object>`	Контейнер для встраиваемого внешнего элемента	`inline-block`

          <details>
            <summary>Описание </summary>
  
              Элемент <object> (от англ. object — объект) сообщает браузеру, как загружать и отображать объекты, которые исходно браузер не понимает. Как правило, такие объекты требуют подключения к браузеру специального модуля, который называется плагин, или запуска вспомогательной программы.

              Дополнительно внутрь контейнера <object> можно поместить элемент <param>, который передаёт дополнительные параметры для отображения объекта.
          </details>
          <details>
            <summary>Синтаксис </summary>
  
              <object></object>
          </details>
          <details>
            <summary>Атрибуты </summary>
  
        - `align` - Определяет, как объект будет выравниваться на странице и способ его обтекания текстом. 
        - `archive` - Устанавливает путь к файлам, необходимым для работы объекта. 
        - `classid` - Адрес программы (приложения или плагина), которая работает с данным объектом, и будет запускать его. 
        - `code` - Имя объекта для его выполнения. 
        - `codebase` - Путь к папке с объектом, который указан атрибутом code или classid. 
        - `codetype` - Указывает на тип объекта, который задан атрибутом classid. 
        - `data` - Адрес файла для его отображения в окне браузера. 
        - `height` - Высота объекта.
        - `hspace` - Горизонтальный отступ от объекта до окружающего контента. 
        - `type` - MIME-тип объекта. 
        - `vspace` - Вертикальный отступ от объекта до окружающего контента. 
        - `width` - Ширина объекта.

              Также для этого элемента доступны универсальные атрибуты и события.

          </details>
          <details>
            <summary>Примеры </summary>
    
              <!DOCTYPE html>
              <html>
                <head>
                  <meta charset="utf-8">
                  <title>OBJECT</title>
                </head>
                <body> 
                 <p><object type="application/x-shockwave-flash" 
                    data="flash/mouse.swf" width="400" height="300">
                  <param name="quality" value="high">
                  <param name="wmode" value="opaque">
                 </object></p>
                </body>
              </html>
              
          <!DOCTYPE html>
          <html>
            <head>
              <meta charset="utf-8">
              <title>OBJECT</title>
            </head>
            <body> 
            <p><object type="application/x-shockwave-flash" 
                data="flash/mouse.swf" width="400" height="300">
              <param name="quality" value="high">
              <param name="wmode" value="opaque">
            </object></p>
           </body>
          </html>
        
          </details>
  
        - #### `<param>`	Параметры встраиваемого внешнего элемента	`none`

            <details> 
              <summary>Описание </summary>
          
              Элемент <param> (от англ. parameter — параметр) предназначен для передачи значений параметров Java-апплетам или объектам веб-страницы, созданным с помощью элементов <applet> или <object>. Такой подход позволяет прямо в коде HTML-документа изменять характеристики объекта без его дополнительной компиляции. Количество одновременно используемых элементов <param> может быть больше одного и для каждого из них задаётся пара «имя=значение» через атрибуты name и value.
            </details>
            <details> 
              <summary>Синтаксис </summary>
          
              <param name="<имя>" value="<значение>">
            </details>
            <details> 
              <summary>Атрибуты </summary>
          
          - `name` - Имя параметра.
          - `type` - MIME-тип объекта. 
          - `value` - Значение параметра.
          - `valuetype` - Тип значения параметра. 
            </details>
            <details> 
              <summary>Примеры </summary>
  
                <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
                  "http://www.w3.org/TR/html4/strict.dtd">
                <html>
                  <head>
                    <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                    <title>PARAM</title>
                  </head>
                  <body>  
                   <p><object classid="animation.class" width="500" height="200">
                    <param name="bgcolor" value="#000000">
                    <param name="delay" value="1000">
                    <param name="loop" value="5">
                   </object></p>
                  </body>
                </html>

            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" 
              "http://www.w3.org/TR/html4/strict.dtd">
            <html>
              <head>
                <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
                <title>PARAM</title>
              </head>
              <body>  
               <p><object classid="animation.class" width="500" height="200">
                <param name="bgcolor" value="#000000">
                <param name="delay" value="1000">
                <param name="loop" value="5">
               </object></p>
              </body>
            </html>
            </details>
          
          - #### `<iframe></iframe>`	Встроенный фрейм	`block`
              <details> 
                <summary>Описание </summary>
  
                  Элемент <iframe> (от англ. inline frame — встроенный фрейм) создаёт встроенный фрейм, который находится внутри обычного документа, он позволяет загружать в область заданных размеров любые другие независимые документы.

                  <iframe> является контейнером, содержание которого игнорируется браузерами, не поддерживающими данный элемент. Для таких браузеров можно указать альтернативный текст, который увидят пользователи. Он должен располагаться между тегами <iframe> и </iframe>.

              </details>
              <details> 
                <summary>Синтаксис </summary>
  
                  <iframe>...</iframe>
              </details>
              <details> 
                <summary>Атрибуты </summary>
  
            - `align` - Определяет, как фрейм будет выравниваться по краю, а также способ обтекания его текстом. 
            - `allowfullscreen` - Разрешает для фрейма полноэкранный режим.
            - `frameborder` - Устанавливает, отображать границу вокруг фрейма или нет. 
            - `height` - Высота фрейма.
            - `hspace` - Горизонтальный отступ от фрейма до окружающего контента. 
            - `marginheight` - Отступ сверху и снизу от содержания до границы фрейма. 
            - `marginwidth` - Отступ слева и справа от содержимого до границы фрейма. 
            - `name` - Имя фрейма.
            - `sandbox` - Позволяет задать ряд ограничений на контент загружаемый во фрейме. 
            - `scrolling` - Способ отображения полосы прокрутки во фрейме.
            - `seamless` - Определяет, что содержимое фрейма должно отображаться так, словно оно является частью документа. 
            - `src` - Путь к файлу, содержимое которого будет загружаться во фрейм.
            - `srcdoc` - Хранит содержимое фрейма непосредственно в атрибуте. 
            - `vspace` - Вертикальный отступ от фрейма до окружающего контента. 
            - `width` - Ширина фрейма.
              </details>
              <details> 
                <summary>Примеры </summary>
    
                  <!DOCTYPE HTML>
                  <html>
                   <head>
                    <meta charset="utf-8">
                    <title>IFRAME</title>
                   </head>
                   <body>  
                   <iframe src="page/banner.html" width="468" height="60" align="left">
                      Ваш браузер не поддерживает встроенные фреймы!
                   </iframe>
                   </body>
                  </html>
          
                <!DOCTYPE HTML>
                <html>
                  <head>
                    <meta charset="utf-8">
                    <title>IFRAME</title>
                  </head>
                  <body>  
                  <iframe src="page/banner.html" width="468" height="60" align="left">
                    Ваш браузер не поддерживает встроенные фреймы!
                  </iframe>
                  </body>
                  </html>
            
              </details>
  
  
  
### Ссылка
- #### `<a></a>`	Гипер ссылка		`inline`
    <details> 
      <summary>Описание </summary>
  
        Элемент <a> (от англ. anchor — якорь) является одним из важных в HTML и предназначен для создания ссылок. 
        Для этого необходимо сообщить браузеру, что является ссылкой, а также указать адрес документа, на который 
        следует сделать ссылку. В качестве значения атрибута href используется адрес документа, на который происходит 
        переход. Адрес ссылки может быть абсолютным и относительным. Абсолютные адреса работают везде и всюду 
        независимо от имени сайта или веб-страницы, где прописана ссылка. Относительные ссылки, как следует из 
        их названия, построены относительно текущего документа или корня сайта.
    </details>
    <details> 
      <summary>Синтаксис </summary>
  
        <a href="<адрес>">...</a>
    </details>
    <details> 
      <summary>Атрибуты </summary>
  
  - `coords` - Устанавливает координаты активной области. 
  - `download` - Предлагает скачать указанный по ссылке файл. 
  - `href` - Задаёт адрес документа, на который следует перейти.
  - `hreflang` - Идентифицирует язык текста по ссылке.
  - `name` - Устанавливает имя якоря внутри документа. 
  - `rel` - Отношения между ссылаемым и текущим документами.
  - `rev` - Отношения между текущим и ссылаемым документами. 
  - `shape` - Задаёт форму активной области ссылки для изображений. 
  - `target` - Имя окна или фрейма, куда браузер будет загружать документ.
  - `type` - Указывает MIME-тип документа, на который ведёт ссылка.
  
          Также для этого элемента доступны универсальные атрибуты и события.
    </details>
    <details> 
      <summary>Примеры </summary>
    
        <!DOCTYPE HTML>
        <html>
         <head>
           <meta charset="utf-8">
          <title>А</title>
         </head>
         <body>
          <p><a href="image/xxx.jpg">Посмотрите на мою фотографию!</a></p>
          <p><a href="page/tip.html">Как сделать такое же фото?</a></p> 
        </body>
        </html>
  
    <!DOCTYPE HTML>
    <html>
      <head>
        <meta charset="utf-8">
        <title>А</title>
      </head>
      <body>
        <p><a href="image/xxx.jpg">Посмотрите на мою фотографию!</a></p>
        <p><a href="page/tip.html">Как сделать такое же фото?</a></p> 
      </body>
      </html>
    
    </details>