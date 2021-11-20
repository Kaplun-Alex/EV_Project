const shadow = "0 16px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19)"
const sbg="2px"
const bbg="4px"

const aboutMes = "<h3>I repaired complex medical equipment. I had to use Raspberry \
                on one of the devices. Read Learning Python, Programming Python\
                5th Edition by Mark Lutz, 4 volumes. Wrote software for the device.\
                Soon there was a need to optimize the work of the security system \
                database and provide data to local users, look to Github. Python \
                began to tighten me! Finished the course Beetroot Academy,\
                in parallel, I have developed a robot device in the field of\
                biochemistry (full development cycle), this robot was a \
                graduation project, look to Youtube. In fact BA gave me Python engineer dev\
                skills. Thereafter Django 3.0 book, Dronov. After that Frontend JS, \
                DevOps AWS, S3 deploy, Herocu-django deploy projects to expand skills.\
                You are looking at the result now. Also several projects on request. Now my direction\
                is full stack samurai path, device control over sockets, web, eth. In search of interesting\
                technology projects. From myself I can give a lot to the team and\
                multiply my engineering skills in dev. See you…</h3>"
const eduMes =   "<h2>Beetroot Academy</h2>\
                08.02.2021 — 12.02.2021   A+<br><br>\
                <h2>University of the state fiscal service Ukraine</h2>\
                2010 – 2013<br>\
                Bachelor's degree, Finance and Credit,   B<br><br>\
                <h2>State University of Telecommunications</h2>\
                2004 — 2008<br>\
                Master's degree, Protection of information in information systems and networks.   A+<br>"
const expMes =    "<h2>StarLightMedia - Junior Python developer</h2>\
                01.03.2021 — to date<br>\
                Create python database multiservices/application<br><br>\
                <h2>StarLightMedia  -  CSO(security systems engineer)</h2>\
                2017 — to date<br>\
                Security cluster administration and support. Implementation of safety systems.\
                Document flow<br><br>\
                <h2>Intteks – CTO (Chief Engineer)</h2>\
                2007 — 2017<br>\
                Full cycle of implementation of technical security systems.\
                Service Center Management. Development of security systems<br><br>"
const skilMes =   "<h2>Lang/Libraries/Modules/Frameworks:</h2>\
                Python, JS, CSS(flaxbox, grid), Bootstrap5, HTML, Django, MySql, SQLite, mongoDB(cloud), Redis, OS, SYS, Argparse, Tkinter, PyQt, Socket, Decimal, Random, Struct, Array,\
                Doctest, Pytest, Unittest,  PyUSB, HIDUSB, Threading,\
                Multiprocessing, Embedd Python Ex, Keyboard, mako, Jinja2, Logging, Numpy, Matplotlib,\
                Beautiful Soup, Unittest.<br><br>\
                <h2>Additional:</h2>\
                Win, Linux(Ubuntu), heroku,  AWS, GIT, Github, Tortoise SVN, PyCharm, Visual Studio Code, Slack, Codespaces beta, \
                Technical background. "
const contMes = " <h2>PHONE:</h2><br>\
                <h3>+38-067-381-80-46  (Telegram, Viber)</h3><br>\
                <h2>E-MAIL:</h2><br>\
                <h3>Kaplunalex1985@gmail.com</h3><br>\
                <h2>KYIV REGION</h2>"
const backMes = "<h2>Electrical and Electronics Engineer:</h2><br>\
                Analog electronics, digital electronics, consumer electronics, embedded systems\
                solid-state physics, radio engineering, telecommunications, control systems,\
                signal processing, systems engineering, computer engineering, instrumentation\
                engineering, electric power control, robotics.<br><br>\
                <h2>DIY Engineer:</h2><br>\
                Personal electric transport, audio amplifiers, Raspberry pi embedded programming,\
                cnc machining assembly processing, welding(TIG, MIG, MMA), Solidworks design,\
                EasyEDA design and manufacturing, assembly of metal structures and mechanisms."
const lnMes = "<h2> Python, JS, ENG(intermediate), UA and others...</h2>"
const sertMes = "<img src='http://127.0.0.1:8000/static/ev_shop/img/SERT.jpg' class='img-fluid mx-auto d-block'/>"

function borderWidth (point){
    [abBut, edBut, exBut, skBut, csBut, bkBut, lnBut, cnBut].map(a => {
    a.style.borderWidth = sbg
})
point.style.borderWidth=bbg
}

const headSection = document.getElementById('header')
const footerSection = document.getElementById('footer')
const mainInfo = document.getElementById('main_info')
const themeBut = document.getElementById('suntheme')

let colorScheme = false
const sunleBut = document.getElementById('sun')
    sunleBut.onclick=function(){
        if (!colorScheme) {
            console.log("blk")
            themeBut.className="icon-moon"
            headSection.style.backgroundColor="green"
            footerSection.style.backgroundColor="green"
            colorScheme = !colorScheme
        } 
        else {
            console.log("noblk")
            headSection.style.backgroundColor="black"
            footerSection.style.backgroundColor="black"
            themeBut.className="icon-sun"
            colorScheme = !colorScheme
        }
    }

const abBut = document.getElementById('ab_but')
    abBut.onmouseover=function(){abBut.style.boxShadow=shadow}
    abBut.onmouseleave=function(){abBut.style.boxShadow="none"}
    abBut.onclick=function() {
        mainInfo.innerHTML=aboutMes
        borderWidth(abBut)
    }

const edBut = document.getElementById('ed_but')
    edBut.onmouseover=function(){edBut.style.boxShadow=shadow}
    edBut.onmouseleave=function(){edBut.style.boxShadow="none"}
    edBut.onclick=function() {
        mainInfo.innerHTML=eduMes
        borderWidth(edBut)
    }

const exBut = document.getElementById('ex_but')
    exBut.onmouseover=function(){exBut.style.boxShadow=shadow}
    exBut.onmouseleave=function(){exBut.style.boxShadow="none"}
    exBut.onclick=function() {
        mainInfo.innerHTML=expMes
        borderWidth(exBut)
    }

const skBut = document.getElementById('sk_but')
    skBut.onmouseover=function(){skBut.style.boxShadow=shadow}
    skBut.onmouseleave=function(){skBut.style.boxShadow="none"}
    skBut.onclick=function() {
        mainInfo.innerHTML=skilMes
        borderWidth(skBut)
    }

const csBut = document.getElementById('cs_but')
    csBut.onmouseover=function(){csBut.style.boxShadow=shadow}
    csBut.onmouseleave=function(){csBut.style.boxShadow="none"}
    csBut.onclick=function() {
        mainInfo.innerHTML=sertMes
        borderWidth(csBut)
    }

const bkBut = document.getElementById('bk_but')
    bkBut.onmouseover=function(){bkBut.style.boxShadow=shadow}
    bkBut.onmouseleave=function(){bkBut.style.boxShadow="none"}
    bkBut.onclick=function() {
        mainInfo.innerHTML=backMes
        borderWidth(bkBut)
    }

const lnBut = document.getElementById('ln_but')
    lnBut.onmouseover=function(){lnBut.style.boxShadow=shadow}
    lnBut.onmouseleave=function(){lnBut.style.boxShadow="none"}
    lnBut.onclick=function() {
        mainInfo.innerHTML=lnMes
        borderWidth(lnBut)
    }

const cnBut = document.getElementById('cn_but')
    cnBut.onmouseover=function(){cnBut.style.boxShadow=shadow}
    cnBut.onmouseleave=function(){cnBut.style.boxShadow="none"}
    cnBut.onclick=function() {
        mainInfo.innerHTML=contMes
        borderWidth(cnBut)
    }