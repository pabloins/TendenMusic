module tendenmusic.tendenmusic {
    requires javafx.controls;
    requires javafx.fxml;

    requires org.kordamp.bootstrapfx.core;

    opens tendenmusic.tendenmusic to javafx.fxml;
    exports tendenmusic.tendenmusic;
    exports tendenmusic.tendenmusic.controllers;
    opens tendenmusic.tendenmusic.controllers to javafx.fxml;
}