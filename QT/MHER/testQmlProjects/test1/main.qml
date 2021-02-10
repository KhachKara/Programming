import QtQuick 2.12
import QtQuick.Window 2.12

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")
    Rectangle {
        id: redRect
        anchors.left: parent.left
        anchors.right: parent.horizontalCenter
        anchors.top: parent.top
        anchors.bottom: parent.verticalCenter
        color: "red"
    }
    Rectangle {
        anchors.left: parent.horizontalCenter
        anchors.right: parent.right
        anchors.top: parent.verticalCenter
        anchors.bottom: parent.bottom
        color: "blue"
    }
    Text {
        text: qsTr("RedRect")
        anchors.centerIn: redRect
    }
}
