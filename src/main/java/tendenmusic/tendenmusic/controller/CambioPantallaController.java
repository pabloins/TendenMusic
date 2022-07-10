package tendenmusic.tendenmusic.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;

import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;

import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import javafx.scene.image.Image;
import javafx.scene.image.ImageView;
import javafx.scene.layout.Pane;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;
import tendenmusic.tendenmusic.Main;

import java.io.IOException;
import java.net.URL;
import java.util.HashMap;
import java.util.ResourceBundle;

public class CambioPantallaController implements Initializable {

    @FXML
    private Text panTitulo;

    @FXML
    private Pane paneGenerar;

    @FXML
    private Button btnGenerarReporte;

    @FXML
    private Button btnPDF;

    @FXML
    private Button btnContacto;

    @FXML
    private Button btnGenerarReporteConFiltro;

    @FXML
    private Pane panStatus;

    @FXML
    private Button btnPlantilla;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {

    }
    @FXML
    private void handleClicks(ActionEvent event) throws IOException {
        if(event.getSource() == btnGenerarReporte){
            panTitulo.setText("Generar Reporte");
            loadStage("VentanaGenerarReporte.fxml");
        } else if (event.getSource() == btnGenerarReporteConFiltro) {
            panTitulo.setText("Generar Reporte con Filtro");
            loadStage("VentanaGenerarReporteFiltro.fxml");
        } else if (event.getSource() == btnContacto) {
            panTitulo.setText("Contacto");
            loadStage("Main.fxml");
        } else if (event.getSource() == btnPDF) {
            
        }
    }

    private void loadStage(String fxml) throws IOException {

        FXMLLoader loader = new FXMLLoader(Main.class.getResource(fxml));
        Parent root = loader.load();

        Stage stage = new Stage();
        stage.setTitle("TendenMusic");
        Image icono = new Image(String.valueOf(Main.class.getResource("icono.png")));
        stage.getIcons().add(icono);
        stage.setScene(new Scene(root));
        stage.initModality(Modality.APPLICATION_MODAL);
        stage.show();

    }

}
