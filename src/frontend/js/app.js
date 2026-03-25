// основная логика фронта
import api from './api.js';

async function extractText() {
    let pointsField = document.getElementById("pointsInput");
    let pointsValue = parseInt(pointsField.value, 10) || 5;

    let westField = document.getElementById("westInput");
    let westValue = parseFloat(westField.value) || 20.22;

    let northField = document.getElementById("northInput");
    let northValue = parseFloat(northField.value) || 20.22;

    let radField = document.getElementById("radInput");
    let radValue = parseFloat(radField.value) || 50;

    console.log("Генерация точек:", {
        center: [northValue, westValue],
        radius: radValue,
        count: pointsValue
    });

    try {
        const result = await api.generatePoints(northValue, westValue, radValue, pointsValue);
        
        console.log("Точки сгенерированы:", result);

        if (window.markers) {
            window.markers.forEach(marker => map.removeLayer(marker));
        }

        window.generatedPoints = result.points;
        window.markers = [];

        result.points.forEach(point => {
            const marker = L.marker([point.lat, point.lon]).addTo(map);
            marker.bindPopup(`<b>Точка ${point.id}</b><br>lat: ${point.lat}<br>lon: ${point.lon}`);
            window.markers.push(marker);
        });

        if (result.points.length > 0) {
            map.setView([result.points[0].lat, result.points[0].lon], 10);
        } else {
            map.setView([northValue, westValue], 10);
        }

        alert(`Сгенерировано ${result.points.length} точек`);
        
    } catch (error) {
        console.error("Ошибка при генерации точек:", error);
        alert("Ошибка при генерации точек: " + error.message);
    }
}

window.extractText = extractText;