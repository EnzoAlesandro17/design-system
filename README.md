# ArchSolutions — Design System

Base de estilos reutilizable para proyectos internos (web y Tkinter). Se arma una sola vez acá y se copia/clona en cada proyecto nuevo.

## Contenido

- `paleta-colores.png` — referencia visual original de la paleta (modo claro, modo oscuro, colores resaltantes).
- `styles.css` — tokens y componentes base para proyectos web (Flask, FastAPI, HTML plano).
- `styles.py` — mismos tokens adaptados a `ttk.Style()` para apps de escritorio en Tkinter.
- `logo/` — logo en versión clara y oscura (`.png` originales y `.svg` vectorizados).

## Paleta

**Modo claro**
| Nombre | Hex | Uso |
|---|---|---|
| Primario | `#2E5FC7` | botones, enlaces, elementos activos |
| Texto principal | `#323332` | títulos, textos importantes |
| Fondo secundario | `#F0F0F0` | secciones, tarjetas |
| Fondo principal | `#FFFFFF` | fondo general |
| Fondo sutil / hover | `#E6F0FF` | hover ligero |
| Texto secundario | `#6B7280` | textos secundarios, placeholders |
| Bordes / divisores | `#CBD1D9` | líneas, bordes |
| Superficies | `#FFFFFF` | tarjetas, modales |

**Modo oscuro**
| Nombre | Hex | Uso |
|---|---|---|
| Primario | `#3878EC` | botones, enlaces, elementos activos |
| Texto principal | `#E6E6E6` | títulos, textos importantes |
| Fondo secundario | `#1E1E1E` | secciones, tarjetas |
| Fondo principal | `#121212` | fondo general |
| Fondo sutil / hover | `#1D2D5C` | hover ligero |
| Texto secundario | `#9CA3AF` | textos secundarios, placeholders |
| Bordes / divisores | `#2A2A2A` | líneas, bordes |
| Superficies | `#242424` | tarjetas, modales |

**Resaltantes** (iguales en ambos modos)
| Nombre | Hex | Uso |
|---|---|---|
| Éxito | `#22C55E` | confirmaciones |
| Advertencia | `#F59E0B` | atención sin indicar error |
| Error | `#EF4444` | fallos, acciones destructivas |
| Información | `#8B5CF6` | contenido destacado |
| Acción secundaria | `#06B6D4` | acciones menos prioritarias |

## Uso en web (`styles.css`)

Linkear el archivo en el `<head>` del HTML:

```html
<link rel="stylesheet" href="styles.css">
```

Modo oscuro: agregar `data-theme="dark"` en el `<html>`. Sin ese atributo queda en modo claro por default.

```html
<html data-theme="dark">
```

## Uso en Tkinter (`styles.py`)

```python
import tkinter as tk
from tkinter import ttk
from styles import apply_theme

root = tk.Tk()
style = apply_theme(root, dark=False)

btn = ttk.Button(root, text="Guardar", style="Primary.TButton")
```

Si algo falla al aplicar el tema (SO sin el tema base, versión vieja de Tkinter), `apply_theme` cae sola a un tema genérico sin romper la app — no requiere manejo de errores desde afuera.

## Notas

- Sin identidad de marca definida todavía: los valores son provisorios y pensados para sistemas internos (ERP, panacar, asistente local). El día que haya marca, se cambian los tokens y el resto se actualiza solo.
- Cualquier ajuste a la paleta se hace acá primero, después se propaga a los proyectos que la usan.

## Cómo se usa este repo desde otro proyecto

Este repo es la fuente de verdad, no se clona entero en cada proyecto. Se copia solo el archivo que corresponda (`styles.css` para web, `styles.py` para Tkinter) — el que no se use, no va.

En el README del proyecto que lo consuma, alcanza con una referencia corta, sin repetir esta documentación:

```md
## Estilos

Basado en el design system interno. Ver detalle y paleta completa en:
https://github.com/EnzoAlesandro17/design-system
```
