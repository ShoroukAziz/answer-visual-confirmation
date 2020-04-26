# Answer Visual Confirmation
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<a title="Rate on AnkiWeb" href="https://ankiweb.net/shared/info/1208806023"><img src="https://glutanimate.com/logos/ankiweb-rate.svg"></a> <a title="Buy me a coffee :)" href="https://ko-fi.com/B0B51L5RI"><img src="https://img.shields.io/badge/ko--fi-contribute-%23579ebd.svg"></a>



This is a very simple Anki Addon that provides a visual confirmation of your Answer in the reviewer by displaying either a thumbs up or a thumbs down picture depending on your answer to the card. it's function is  similar to the [Visual Feedback for Reviews](https://ankiweb.net/shared/info/1749604199) addon but it allows using animated gifs for more fun and it works with Anki 2.1 <br>
<b>
<p   align="center" >
<img style="width:500px" src="https://github.com/my-Anki/answer-visual-confirmation/blob/master/screenshots/screenrecord.gif?raw=true"  >  
</p>

>For discussions head to  [Reddit](https://www.reddit.com/r/Anki/comments/g64qe0/addon_release_visual_confirmation_for_anki_21/)
</b>
## Configuration and Customization
From the menu bar > tools > add-ons
choose "Answer Visual Confirmation" then > Configuration

<p   align="center" >
<img style="width:500px" src="https://github.com/my-Anki/answer-visual-confirmation/blob/master/screenshots/screenrecord2.gif?raw=true"  >  
</p>

the default configuration are: <br>
```
{
    "duration":1400,
    "theme":"animated",
    "mode" : "random" ,
    "gradual_interval" : 100
}
```
<br>

| option        | definition    |
| :-------------: |:-------------|
| `duration`    | How long ,in ms, do you want the feedback to appear on the screen |
| `theme`      | `animated` :to display gifs <br>  `still` : to display pngs    |
| `mode`       |  `random` : will display different pictures randomly. <br>  `gradual` :  will display a different picture every defined number of reviews (gradual_interval)      | 
| `gradual_interval`       | the number of reviews after which the displayed images for (easy, good, hard and again will be changed).      |

#### Making it your own
If you don't like either of the default pics, you can (and you definitely should) add your own images  :<br>

#### The images folder

<img align="right"  style="width:200px" src="https://github.com/my-Anki/answer-visual-confirmation/blob/master/screenshots/screenshot.PNG?raw=true"  >  

Inside the addon's main folder there's an `images` folder <br>
that contains two other sub folders `gif` and `png` each folder for each image's extension.<br>
Inside each of the subfolders there're 4 folders. One for each difficulty level `again` , `hard` , `good` and `easy`


#### More on the `mode` option
there are two modes you can use this addon with :
* <b>Random</b>:<br>
In this mode after each review a random image will be selected from your images folder based in your answer. <br>
For example, If you answered again and your theme is `animated`
a random picture from the again folder (in the gif folder) will be selected. and so on.

* <b>Gradual</b>:<br>
In this mode the pictures won't change randomly but after a number of reviews you define.<br>
for example: <br>
let's say for your first 100 reviews you want funny cat gifs
and for your second 100 reviews you want the Simpsons gifs.
and for your third 100 reviews you want dr Cox gifs
what you would do is : <br>
* set the `theme` to `animated`
* set the `mode` to `gradual`
* set the `gradual_interval` to `100`
* now in the `gif` folder:
  - → in the `easy` folder you'll add three pictures:
    - `0.png` an image for a happy cat
    - `1.png` an image for a happy Homer Simpson
    - `2.png` an image for a happy Dr Cox
  - → in the `again` folder you'll add another three pictures:
    - `0.png` an image for an angry cat
    - `1.png` an image for a disappointed Homer Simpson
    - `2.png` an image for Dr Cox saying "Wrong"!

and so on with the other folders you get the idea


## Download
Download it from [AnkiWeb](https://ankiweb.net/shared/info/1208806023).

## License
Answer Visual Confirmation is released under MIT License Copyright (c) 2020 [Shorouk Abdelaziz](https://shorouk.xyz)

## Credits
* Animated pictures from [clipart.email](https://www.clipart.email/) and [giphy](https://giphy.com/)
* Still pictures from [Flaticon](https://www.flaticon.com/) by [Freepik](https://www.flaticon.com/authors/freepik)
