// autor:Ondřej Andrla

import QtQuick 2.12
import QtQuick.Window 2.12
import QtQuick.Layouts 1.11
import QtQuick.Controls 2.5
//import Foo 1.0



Window {
    id: okno
    visible: true
    width: 400
    height: 550
    maximumHeight: 550
    maximumWidth: 400
    minimumHeight: 550
    minimumWidth: 400
    onVisibleChanged: if (visible) textA.forceActiveFocus()
    title: "RunySoft Calculator"
    color: "#ccff99"
property int selector: 0;

    //Seznam prvků pro menu
    ListModel {
        id: controls;
        ListElement { op: "CALCULATOR"; tog: true;}
        ListElement { op: "HELP"; tog: false;}


    }

    //Seznam prvků pro klasické operace
    ListModel {
        id: ope;

 ListElement { op: "*"; tog: false; }
 ListElement { op: "√"; tog: false; }
 ListElement { op: "/"; tog: false; }
 ListElement { op: "!"; tog: false; }
 ListElement { op: "-"; tog: false; }
 ListElement { op: "ln"; tog: false; }
 ListElement { op: "+"; tog: false; }
 ListElement { op: "^"; tog: false; }
    }



    //Seznam prvků pro číselník
    ListModel {
        id: numbers;
        ListElement { op: "7"; tog: false; }
        ListElement { op: "8"; tog: false; }
        ListElement { op: "9"; tog: false; }
        ListElement { op: "4"; tog: false; }
        ListElement { op: "5"; tog: false; }
        ListElement { op: "6"; tog: false; }
        ListElement { op: "1"; tog: false; }
        ListElement { op: "2"; tog: false; }
        ListElement { op: "3"; tog: false; }
        ListElement { op: "0"; tog: false; }
        ListElement { op: "."; tog: false; }
        ListElement { op: "clr"; tog: false; }
    }





    //Řádek pro menu, kde jsou ty prvky se seznamu pro menu

    Row{
        //Parametry toho řádku
        id: main_menu
        width: 400
        height: 80
        Repeater {
            model: controls;
            delegate: Rectangle {
                width: 200
                height: 80
                color: toggled ? Qt.darker("#ccff99") : "#ccff99"
                border.color: "#ccff99";
                border.width: 2;
                property bool toggled;
                radius:5
               // property alias text: txt.text;

                MouseArea {
                    id: mouse;
                    anchors.fill: parent;
                    onClicked: {

                            for (var i = 0; i < controls.count; i++) {
                                controls.setProperty( i, "tog", (i == index) );
                            }
                            if (controls.get(0).tog === true)
                                calc.visible = true
                            else
                                calc.visible = false
                            if (controls.get(1).tog === true)
                                help.visible = true
                            else
                                help.visible = false

                    }
                }

                Text {
                    id: txt;
                    anchors.fill: parent;
                    text: model.op
                    color: toggled ? "white" : "black"
                    font.pointSize: 12;
                    font.bold: true;

                    horizontalAlignment: Text.AlignHCenter
                    verticalAlignment: Text.AlignVCenter

                }
                toggled: model.tog;



            }

        }

    }


    Rectangle {
        //Parametry toho rectanglu
        id: calc
        width: 400
        height: 450
        anchors.top: main_menu.bottom //ukotvení horní hrany rectanglu na spodek main menu
        color: "#bbbbbb"

        Rectangle {
            id: vstup;
            height: 100;
            width: 400;
            border.color: "#bbb";
            border.width: 3;
            anchors.margins: 2

            color: "#EEE"
            ScrollView{
                anchors.fill: parent
                TextField {
                    width: 400
                    height: 100
                    text:""
                    horizontalAlignment: TextInput.AlignRight
                    verticalAlignment: TextInput.AlignVCenter
                    id: textA
                    font.pointSize: 20
                    validator: RegExpValidator{ regExp: /([0-9]*[xy]*(log)*(sin)*(cos)*(tan)*(e)*(!)*(pi)*(,)*(=)*[+*/]*(-)*(\x5e)*(sqrt)*(\x28)*(\x29)*)*/ }
                }
            }
        }


        Row{
            id: func_row
            anchors.top:vstup.bottom //zase ukotvení
            GridLayout {
                id: numbers_layout
                columns: 3
                rows: 4
                columnSpacing : 0
                rowSpacing : 0
                Repeater {
                    model: numbers;
                    delegate: Rectangle {
                        width: 80
                        height: 80
                        radius: 5
                        property bool toggled;

                        color : op === "clr" ? "orange" : "#ccff99";
                        border.color: "#bbbbbb";
                        border.width: 1;


                        // Oblast pro zachytávaní události myši
                        MouseArea {

                            anchors.fill: parent;
                            onClicked: {

                                    id: mouse;
                                    model.op === "clr" ? textA.text = "" :textA.text = textA.text + op

                                    if (textA1.text === "a"){
                                       textA3.text = textA.text;
                                       }
                                    if (textA1.text === "b"){
                                       textA4.text =  textA.text;

                            }
                        }


                        Text {
                            id: txt1;
                            anchors.fill: parent;

                            color: toggled ? "#0066FF" : "black"
                            font.pointSize: 18;
                            font.bold: true;
                            text: model.op
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter

                        }



                    }
                }
            }


            }
            GridLayout {
                columns: 2
                rows : 4
                columnSpacing : 0
                rowSpacing : 0
                Repeater {
                     model: ope;
                    delegate: Rectangle {
                        width: 80
                        height: 80
                        radius: 5

                        color : "#ccff99";

                        border.color: "#bbbbbb";
                        border.width: 1;

                        MouseArea {

                            anchors.fill: parent;
                            onClicked: {
                                textA1.text = "b";

                                textA2.text = op;

                                textA.text = "";
                            }
                        }


                        Text {
                            id: txt2;
                            anchors.fill: parent;

                            //color: toggled ? "#0066FF" : "black"
                            font.pointSize: 18;
                            font.bold: true;
                            text: model.op
                            horizontalAlignment: Text.AlignHCenter
                            verticalAlignment: Text.AlignVCenter

                        }

                    }
                }
            }

        }


        Rectangle {
             id: compute
            signal clicked();
            width: 400;
            height: 50;
            property color btnColor: "red"
            anchors.top: func_row.bottom
            //property alias text: txt.text;
            border.color: "black";
            border.width: 2;
            Text {
                id: txt3;

                font.pixelSize: 30
                anchors.centerIn: compute.Center
                anchors.horizontalCenter: compute.horizontalCenter
                anchors.verticalCenter: compute.verticalCenter
                 text:  "="
            }
            MouseArea {
                anchors.fill: parent;
            onClicked: {textA1.text = "a";var res = "";var a = textA3.text;
                if (textA2.text  === "/"){res = textA3.text / textA4.text;}
                else if(textA2.text === "*"){res = textA3.text * textA4.text;}
                else if(textA2.text === "+"){res = textA3.text + textA4.text;}
                else if(textA2.text === "-"){res = textA3.text - textA4.text;}
                else if (textA2.text  === "√"){if (a<0){res = "none"}
                    else{res = Math.pow(textA3.text,1 / textA4.text);} }
               else if(textA2.text === "ln"){res = Math.log(textA3.text) ;}
               else if(textA2.text === "!"){if (a % 1 !== 0){res = "none"}
                     else{res = 1; if (a<0){res = "none"} else if (a===0){res = 1}
                        else {while (a!==1){res = a * res; a-=1}}}}
               else if(textA2.text === "^"){res = Math.pow(textA3.text, textA4.text);}
                textA.text = res; textA3.text = res;textA4.text = "";
            }}}


        Rectangle {
            id: calc1
            width: 400
            height: 450
            anchors.top: compute.bottom
            color: "#bbbbbb"
            Rectangle {
                //Parametry toho rectanglu
                id: vstup1;
                height: 100;
                width: 400;
                border.color: "#bbb";
                border.width: 3;
                anchors.margins: 2

                color: "#EEE"
                ScrollView{
                    anchors.fill: parent
                    TextField {
                        width: 400
                        height: 100
                        text:"a"
                        horizontalAlignment: TextInput.AlignRight
                        verticalAlignment: TextInput.AlignVCenter
                        id: textA1
                        font.pointSize: 20
                        validator: RegExpValidator{ regExp: /([0-9]*[xy]*(log)*(sin)*(cos)*(tan)*(e)*(!)*(pi)*(,)*(=)*[+*/]*(-)*(\x5e)*(sqrt)*(\x28)*(\x29)*)*/ }
                    }
                }
            }

            Rectangle {
                id: calc2
                width: 400
                height: 450
                anchors.top: calc1.bottom
                color: "#bbbbbb"
                Rectangle {
                    //Parametry toho rectanglu
                    id: vstup2;
                    height: 100;
                    width: 400;
                    border.color: "#bbb";
                    border.width: 3;
                    anchors.margins: 2

                    color: "#EEE"
                    ScrollView{
                        anchors.fill: parent
                        TextField {
                            width: 400
                            height: 100
                            text:"a"
                            horizontalAlignment: TextInput.AlignRight
                            verticalAlignment: TextInput.AlignVCenter
                            id: textA2
                            font.pointSize: 20
                            validator: RegExpValidator{ regExp: /([0-9]*[xy]*(log)*(sin)*(cos)*(tan)*(e)*(!)*(pi)*(,)*(=)*[+*/]*(-)*(\x5e)*(sqrt)*(\x28)*(\x29)*)*/ }
                        }
                    }
                }
            }

            Rectangle {
                id: calc3
                width: 400
                height: 450
                anchors.top: calc2.bottom
                color: "#bbbbbb"
                Rectangle {
                    id: vstup3;
                    height: 100;
                    width: 400;
                    border.color: "#bbb";
                    border.width: 3;
                    anchors.margins: 2

                    color: "#EEE"
                    ScrollView{
                        anchors.fill: parent
                        TextField {
                            width: 400
                            height: 100
                            text:"a"
                            horizontalAlignment: TextInput.AlignRight
                            verticalAlignment: TextInput.AlignVCenter
                            id: textA3
                            font.pointSize: 20
                            validator: RegExpValidator{ regExp: /([0-9]*[xy]*(log)*(sin)*(cos)*(tan)*(e)*(!)*(pi)*(,)*(=)*[+*/]*(-)*(\x5e)*(sqrt)*(\x28)*(\x29)*)*/ }
                        }
                    }
                }
            }

            Rectangle {
                id: calc4
                width: 400
                height: 450
                anchors.top: calc3.bottom
                color: "#bbbbbb"
                Rectangle {
                    id: vstup4;
                    height: 100;
                    width: 400;
                    border.color: "#bbb";
                    border.width: 3;
                    anchors.margins: 2

                    color: "#EEE"
                    ScrollView{
                        anchors.fill: parent
                        TextField {
                            width: 400
                            height: 100
                            text:"a"
                            horizontalAlignment: TextInput.AlignRight
                            verticalAlignment: TextInput.AlignVCenter
                            id: textA4
                            font.pointSize: 20
                            validator: RegExpValidator{ regExp: /([0-9]*[xy]*(log)*(sin)*(cos)*(tan)*(e)*(!)*(pi)*(,)*(=)*[+*/]*(-)*(\x5e)*(sqrt)*(\x28)*(\x29)*)*/ }
                        }
                    }
                }
            }
}

    } //Konec okna pro kalkulačku



    Rectangle{ //Okno pro help
        id: help
                width: 400
                height: 650
                anchors.top: main_menu.bottom
                visible: false
                color: "#ccff99"


                Rectangle{
                    id:  help2;
                    height: 200;
                    width: 400;

                    Text {
                        id:  help2_text;

                        x: 10
                        y: 10

                        height: 6;
                        font.pointSize: 12
                        color: "#000000"
                        text:
        "Výraz můžete do kalkulačky zadávat klikáním na
        číslice a operátory. Nejprve klikněte na první
        číslici poté na operátor a následně
        na druhou číslici.
        Pokud kliknete na opearad '!' nebo 'ln'
        nezadávejte již druhou číslici
        ale rovnou klikněte na '='.

        Kliknutím na tlačítko '=' získáte výsledek.";
                    }
                }

                Rectangle{
                    id:  help_hot_keys;
                    height: 60;
                    width: 400;
                    anchors.top: help2.bottom

                    Text {
                        id:  help_hot_keys_text;
                        x: 10
                        y: 5

                        height: 4;
                        font.pointSize: 12
                        color: "#000000"
                        text: "Výsledek zůstává uložen v kalkulačce
        a slouží dále jako první operand." ;
                    }
                }

                Rectangle{
                    id:  help_history;
                    height: 160;
                    width: 400;
                    anchors.top: help_hot_keys.bottom

                    Text {
                        id:  help_history_text;

                        x: 10
                        y: 5

                        height: 4;
                        font.pointSize: 12
                        color: "#000000"
                        text: "Stisknutím tlačítka 'clr' vymažete
        veškeré hodnoty uložené v kalkulačce
        z předchozích výpočtů.

        Pokud jsou operandy zadány špatně,
        kalkulačka vypíše 'none' nebo 'inf'.
        V takovémto případě vynulujte paměť
        pomocí 'clr' a pokračujte ve výpočtu.
" ;
                    }
                }

    }
}
