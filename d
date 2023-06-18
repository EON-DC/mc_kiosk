QScrollBar:vertical {
        border: 1px solid #999999;
        border-radius: 10px;
        background:white;
        width:20px;
        margin: 0px 0px 0px 0px;
}
QScrollBar::handle:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130), stop:1 rgb(32, 47, 130));
    min-height: 0px;
}
QScrollBar::add-line:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 20px;
    subcontrol-position: bottom;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:vertical {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
    stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),  stop:1 rgb(32, 47, 130));
    height: 5px;
    subcontrol-position: top;
    subcontrol-origin: margin;
}