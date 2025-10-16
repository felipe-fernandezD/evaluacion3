# evaluacion3
prueba de  Django + DRF

## 📘 Descripción
Esta RESTful API permite gestionar una lista de tareas usando **Django Rest Framework (DRF)**.
Se llevan a cabo los principios de RESTful, JSON y control de versión de la API, así como arquitectura por capas.

---

Recurso principal
Tarea con los siguientes campos:
- `id` (int, auto generado)
- `titulo` (string, requerido)
- `hecho` (boolean, por defecto `false`)
- `created_at` (datetime, automático)

---

Endpoints
Base URI: `/api/v1/tareas/`

| Método     |          URI           |               Descripción              | Código esperado |
|------------|------------------------|----------------------------------------|-----------------|
| **GET**    | `/api/v1/tareas/`      | Lista todas las tareas (paginadas)     | 200 OK |
| **POST**   | `/api/v1/tareas/`      | Crea una nueva tarea                   | 201 Created |
| **GET**    | `/api/v1/tareas/{id}/` | Obtiene el detalle de una tarea        | 200 OK / 404 Not Found |
| **PATCH**  | `/api/v1/tareas/{id}/` | Actualiza el título o estado (`hecho`) | 200 OK / 400 Bad Request |
| **DELETE** | `/api/v1/tareas/{id}/` | Elimina una tarea                      | 204 No Content |

---

Reglas REST utilizadas
- **Stateless:** Se refiere a que no guarda los estados entre peticiones en otras palabras que en cada peticion que se haga al sitio no necesita de la informacio de la peticion anterior.
- 
- **JSON:** Es un formato de texto que sirve para enviar y recibir datos ordenados a un servidor o base de datos.
- **Versionado:** Se incluye `/api/v1/` en la ruta para permitir futuras versiones.
- **Idempotencia:**  Significa que repetir la misma operación no cambia el resultado final.

---

## 🧩 Arquitectura por capas

```text
[ Cliente (curl / Postman / SPA) ] ->Envía peticiones HTTP y recibe respuestas JSON.
        |
     HTTP / JSON-> el metodo de comunicacio.
        |
[ API /api/v1 (DRF ViewSets / URLs) ]->Define los endpoints REST y gestiona los métodos GET, POST, PATCH, DELETE.
        |
[ Serializers (validación / formato JSON) ]->Validan y transforman los datos entre Python ↔ JSON
        |
[ Modelos Django (ORM) ]->Representan las tablas de la base de datos.
        |
[ Base de datos SQLite (local) ]->Guarda la información de las tareas.
