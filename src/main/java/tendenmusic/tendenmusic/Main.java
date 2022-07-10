package tendenmusic.tendenmusic;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.stage.Stage;
import javafx.stage.StageStyle;

import java.io.IOException;

public class Main extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        FXMLLoader fxmlLoader = new FXMLLoader(Main.class.getResource("Main.fxml"));
        Scene scene = new Scene(fxmlLoader.load(), 1078, 662);
        stage.setTitle("TendenMusic");
        Image icono = new Image(String.valueOf(Main.class.getResource("icono.png")));

        //stage.initStyle(StageStyle.UNDECORATED);
        stage.getIcons().add(icono);
        stage.setScene(scene);
        stage.show();
    }

    public static void main(String[] args) {
        launch(args);
    }
}