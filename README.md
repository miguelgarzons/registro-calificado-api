# Proyecto Django con Arquitectura Hexagonal

Este proyecto implementa **Django** siguiendo los principios de la **Arquitectura Hexagonal (Ports & Adapters)**.
La idea principal es separar la lógica de negocio (dominio) de los detalles de infraestructura (frameworks, bases de datos, APIs externas).

---

## 📂 Estructura del proyecto

```
.
├── .devcontainer/                # Configuración para desarrollo en contenedor (VS Code Remote)
│   ├── devcontainer.json
│   └── Dockerfile
│
├── app/                          # Código fuente principal de Django
│   ├── Acta/                     # Módulo principal (puede haber más apps)
│   │   ├── application/          # Capa de aplicación (casos de uso, DTOs)
│   │   │   ├── dto.py
│   │   │   └── use_cases.py
│   │   │
│   │   ├── domain/               # Capa de dominio (reglas de negocio)
│   │   │   ├── entities.py       # Entidades de negocio puras (sin dependencias de Django)
│   │   │   ├── repositories.py   # Interfaces (ports) que definen cómo acceder a datos
│   │   │   ├── services.py       # Lógica de negocio (servicios de dominio)
│   │   │   └── value_objects.py  # Objetos de valor (tipados, invariantes)
│   │   │
│   │   ├── infrastructure/       # Capa de infraestructura (adapters)
│   │   │   ├── models.py         # Modelos Django (ORM)
│   │   │   ├── repositories.py   # Implementaciones concretas de repositorios
│   │   │   ├── serializers.py    # Serializadores de Django REST Framework
│   │   │   └── views.py          # Endpoints y vistas (adapters HTTP)
│   │   │
│   │   ├── migrations/           # Migraciones de base de datos
│   │   └── tests/                # Tests unitarios y de integración
│   │       ├── test_views.py
│   │       ├── test_models.py
│   │       └── ...
│   │
│   ├── Acuerdo/                  # Otra app de Django (ejemplo)
│   └── registro_calificado/      # Otra app de Django (ejemplo)
│
├── venv/                         # Entorno virtual local (si no se usa Docker)
│
├── .env                          # Variables de entorno (configuración sensible)
├── .gitignore
├── docker-compose.yml            # Orquestación con Docker Compose
├── Dockerfile                    # Imagen base para Django
├── entrypoint.sh                 # Script de arranque (migraciones + superusuario + servidor)
├── manage.py                     # Script de administración de Django
├── pyrefly.toml                  # Configuración de Pyrefly (tipado estático)
├── requirements.txt              # Dependencias Python
└── .pre-commit-config.yaml       # Hooks pre-commit (linting, formateo, etc.)
```

---

## 🏗️ Capas principales

* **Domain (`domain/`)**
  Contiene la lógica central de negocio: entidades, servicios y objetos de valor.
  Aquí no debería haber dependencias de frameworks.

* **Application (`application/`)**
  Define casos de uso y orquesta la interacción entre el dominio y la infraestructura.
  Usa DTOs para transferir datos entre capas.

* **Infrastructure (`infrastructure/`)**
  Implementa adaptadores concretos:

  * Modelos Django (`models.py`) para persistencia.
  * Serializadores DRF (`serializers.py`) para exponer datos.
  * Repositorios (`repositories.py`) que implementan las interfaces definidas en `domain/repositories.py`.
  * Vistas (`views.py`) que exponen endpoints HTTP.

* **Entrypoint (`entrypoint.sh`)**
  Automatiza el arranque:

  * Ejecuta migraciones.
  * Crea superusuario si no existe.
  * Inicia el servidor.

---

## 🚀 Ejecución

Este proyecto puede levantarse de dos formas:

1. **Con Docker Compose** (recomendado).
2. **Sin Docker (local)**.

Ver [Guía detallada de ejecución](#) (añadir link a la sección con pasos explicados).

---

## 🧪 Tests

Los tests se organizan por app en la carpeta `tests/`.
Se ejecutan con:

```bash
python manage.py test
```

---

## ✅ Calidad de código

* **Pyrefly** para tipado estático:

```bash
pyrefly check
```

* **Pre-commit hooks** (ejecutar antes de cada commit):

```bash
pre-commit run --all-files
```

---

## 📌 Notas finales

* La separación en capas hace que la lógica de negocio sea independiente de Django, facilitando pruebas y mantenimiento.
* Puedes sustituir `infrastructure/` por otras implementaciones (por ejemplo, otra base de datos o API externa) sin afectar `domain/`.
* Usa `.env` para credenciales y configuraciones sensibles (nunca lo subas a git).
