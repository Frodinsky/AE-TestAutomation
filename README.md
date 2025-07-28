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

```plaintext
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

## 📁 Cómo Ejecutar


