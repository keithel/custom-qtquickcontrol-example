import QtQuick 2.12
import QtQuick.Controls.Material 2.12
import QtQuick.Controls.Material.impl 2.12
import QtQuick.Templates 2.12 as T

T.TabBar {
    id: control

    property var orientation: ListView.Horizontal

    implicitWidth: Math.max(implicitBackgroundWidth + leftInset + rightInset, contentWidth + leftPadding + rightPadding)
    implicitHeight: Math.max(implicitBackgroundHeight + topInset + bottomInset, contentHeight + topPadding + bottomPadding)

    contentItem: ListView {
        model: control.contentModel
        currentIndex: control.currentIndex
        spacing: control.spacing
        orientation: control.orientation
        boundsBehavior: Flickable.StopAtBounds
        flickableDirection: Flickable.AutoFlickIfNeeded
        snapMode: ListView.SnapToItem
        highlightMoveDuration: 250
        highlightResizeDuration: 0
        highlightFollowsCurrentItem: true
        highlightRangeMode: ListView.ApplyRange
        preferredHighlightBegin: 48
        preferredHighlightEnd: width - 48

        highlight: Item {
            z: 2

            Rectangle {
                height: 2
                width: parent.width
                y: control.position === T.TabBar.Footer ? 0 : parent.height - height
                color: control.Material.accentColor
            }

        }

    }

    background: Item {
        Rectangle {
            anchors.fill: parent
            color: "orange"
            layer.enabled: control.Material.elevation > 0

            layer.effect: ElevationEffect {
                elevation: control.Material.elevation
                fullWidth: true
            }

        }

    }

}