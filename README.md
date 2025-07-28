# 🧪 AE Test Automation – Selenium & Python

Automatización de pruebas end-to-end (E2E) usando **Python**, **Selenium** y **Pytest**, sobre la web [Automation Exercise](https://automationexercise.com).  
Este proyecto forma parte de mi portafolio para demostrar habilidades en automatización moderna, diseño escalable (Page Object Model), y buenas prácticas con fixtures y modularización.

> 🎯 Enfocado en roles de QA Automation / SDET

---

## 📌 Tabla de Contenidos

- [🔍 Descripción](#-descripción)
- [🚀 Características](#-características)
- [🛠️ Tecnologías Usadas](#-tecnologías-usadas)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [▶️ Cómo Ejecutar](#-cómo-ejecutar)
- [✅ Test Cases Implementados](#-test-cases-implementados)
- [🧠 Decisiones Técnicas](#-decisiones-técnicas)
- [🗺️ Roadmap / Próximos Pasos](#-roadmap--próximos-pasos)
- [📸 Capturas de Pantalla](#-capturas-de-pantalla)
- [📬 Contacto](#-contacto)

---

## 🔍 Descripción

Este repositorio automatiza distintos flujos de prueba sobre el sitio web [https://automationexercise.com](https://automationexercise.com), una plataforma pública para practicar automatización de pruebas.

Se utilizan patrones de diseño como **Page Object Model (POM)** y **fixtures de Pytest** para crear una arquitectura mantenible y reutilizable.

---

## 🚀 Características

- Automatización E2E de flujos de usuario reales
- Uso de Selenium WebDriver con Pytest
- Arquitectura basada en Page Object Model (POM)
- Modularización por componentes, helpers y páginas
- Uso de fixtures reutilizables con `conftest.py`
- Compatible para ejecutar en local y en CI (futuro)

---

## 🛠️ Tecnologías Usadas

- Python 3.x  
- Selenium WebDriver  
- Pytest  
- POM (Page Object Model)  
- Pytest fixtures (`conftest.py`)  
- Modularización por componentes

---

## 📁 Estructura del Proyecto

AE-TestAutomation/
│
├── components/             # Elementos reutilizables como header, modales, etc.
├── helpers/                # Flujos de usuario (ej: login, navegación)
├── pages/                  # Page Objects de cada vista
├── tests/                  # Casos de prueba automatizados
├── conftest.py             # Fixtures globales para Pytest
├── base_page.py            # Clase base con funciones comunes
├── pytest.ini              # Configuración de pytest
└── README.md

---


## ▶️ Cómo Ejecutar

1. Clonar el repositorio
git clone https://github.com/Frodinsky/AE-TestAutomation.git
cd AE-TestAutomation

2. Crear entorno virtual e instalar dependencias
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Ejecutar pruebas
pytest

---

## ✅ Test Cases Implementados

 Test Case 1 – Verificar la página de inicio

 Test Case 2 – Registro de nuevo usuario

 Test Case 3 – Inicio de sesión del usuario

Próximamente:
 Test Case 4 – Eliminar cuenta de usuario

 Test Case 5 – Compra de producto

 Test Case 6 – Contacto desde formulario

 Test Case 7 – Validación visual de productos

 Test Case 8 – Navegación por categorías

 Test Case 9 – Búsqueda y filtros

 Test Case 10 – Verificación de carrito persistente

---

## 🧠 Decisiones Técnicas

Arquitectura basada en Page Object Model (POM): Cada vista está representada por una clase que encapsula sus elementos y acciones.

Uso de fixtures en Pytest: Mediante conftest.py se definen datos y configuración reutilizable para todos los tests.

Separación de responsabilidades: helpers/ maneja flujos reutilizables, components/ para secciones comunes (como el header).

Base Page común: base_page.py contiene funciones compartidas como navegación, clics, etc.

Enfoque en escalabilidad: Esta estructura permite agregar nuevos tests o funcionalidades sin romper otros casos existentes.

---

## 🗺️ Roadmap / Próximos Pasos

 Añadir al menos 7 test cases adicionales

 Integrar generación de reportes HTML automáticos

 Agregar capturas o grabaciones de ejecución

 Implementar GitHub Actions para CI

 Agregar pruebas negativas y validaciones de errores
 
---

## 📸 Capturas de Pantalla

<!--   ![Ejecución de pruebas](docs/screenshots/test-running.png) -->
 
---

## 📬 Contacto

💼 [LinkedIn](https://www.linkedin.com/in/rodolfo-lara-qa-automation/)
