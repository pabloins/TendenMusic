package tendenmusic.tendenmusic.controller;

import javafx.event.ActionEvent;
import javafx.fxml.FXML;

import javafx.fxml.FXMLLoader;
import javafx.fxml.Initializable;

import javafx.scene.Node;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.scene.control.Button;

import javafx.scene.image.Image;
import javafx.scene.layout.Pane;
import javafx.scene.text.Text;
import javafx.stage.Modality;
import javafx.stage.Stage;
import tendenmusic.tendenmusic.Main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.URL;
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
            Node source= (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.close();
        } else if (event.getSource() == btnGenerarReporteConFiltro) {
            panTitulo.setText("Generar Reporte con Filtro");
            loadStage("VentanaGenerarReporteFiltro.fxml");
            Node source= (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.close();
        } else if (event.getSource() == btnContacto) {
            panTitulo.setText("Contacto");
            loadStage("Main.fxml");
            Node source= (Node) event.getSource();
            Stage stage = (Stage) source.getScene().getWindow();
            stage.close();
        } else if (event.getSource() == btnPDF) {
            generarReportePdf();
        } else if (event.getSource() == btnPlantilla) {
            generarReportePlanilla();
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

    private void generarReportePdf() throws IOException {
        String dirScript = "C://Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/ScriptPythonReport.bat";
        Runtime.
                getRuntime().
                exec("cmd /c start "+dirScript);
    }

    private void generarReportePlanilla() throws IOException {
        String dirScript = "C://Users/Diego/OneDrive/Escritorio/ProyectoTendenMusic/Java/TendenMusic/src/main/java/tendenmusic/tendenmusic/Python/ScriptPythonExport.bat";
        Runtime.
                getRuntime().
                exec("cmd /c start "+dirScript);
    }
}
