"""
styles.py — Paleta de colores y estilos ttk para apps de escritorio.

Uso:
    from styles import apply_theme

    root = tk.Tk()
    apply_theme(root, dark=False)

Si algo falla al aplicar el tema (tema base no disponible en el SO,
version vieja de Tkinter, etc.), cae solo al tema 'clam' generico
sin romper la app.
"""

from tkinter import ttk


# ==========================================================================
# TOKENS — colores
# ==========================================================================

COLORS_LIGHT = {
    "primary": "#2E5FC7",
    "text_primary": "#323332",
    "bg_secondary": "#F0F0F0",
    "bg_primary": "#FFFFFF",
    "primary_soft": "#E6F0FF",
    "text_secondary": "#6B7280",
    "border": "#CBD1D9",
    "surface": "#FFFFFF",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "info": "#8B5CF6",
    "action_secondary": "#06B6D4",
}

COLORS_DARK = {
    "primary": "#3878EC",
    "text_primary": "#E6E6E6",
    "bg_secondary": "#1E1E1E",
    "bg_primary": "#121212",
    "primary_soft": "#1D2D5C",
    "text_secondary": "#9CA3AF",
    "border": "#2A2A2A",
    "surface": "#242424",
    "success": "#22C55E",
    "warning": "#F59E0B",
    "error": "#EF4444",
    "info": "#8B5CF6",
    "action_secondary": "#06B6D4",
}

# ==========================================================================
# TOKENS — tipografia y espaciado
# ==========================================================================

FONT_FAMILY = "Segoe UI"  # fallback: Tkinter usa la del sistema si no existe

FONT_SIZE_TITLE = 16
FONT_SIZE_SUBTITLE = 12
FONT_SIZE_BODY = 10
FONT_SIZE_SMALL = 9

SPACE_1 = 4
SPACE_2 = 8
SPACE_3 = 16


# ==========================================================================
# APLICAR TEMA
# ==========================================================================

def apply_theme(root, dark: bool = False) -> ttk.Style:
    """
    Configura ttk.Style() con la paleta definida.
    Devuelve el objeto Style para que la UI pueda usar los nombres
    de estilo (ej: widget["style"] = "Primary.TButton").

    Si el tema base falla (poco comun, pero pasa segun SO/version),
    cae a 'clam' y despues a lo que Tkinter traiga por defecto.
    """
    colors = COLORS_DARK if dark else COLORS_LIGHT
    style = ttk.Style(root)

    for theme in ("clam", "default"):
        try:
            style.theme_use(theme)
            break
        except Exception:
            continue
    # si ninguno de los dos existe, sigue con el tema que ya estaba activo

    try:
        _configure_styles(style, colors)
    except Exception:
        # si algo de la paleta falla (color invalido, widget no soportado),
        # la app sigue funcionando con el tema base sin estilos custom
        pass

    root.configure(bg=colors["bg_primary"])
    return style


def _configure_styles(style: ttk.Style, colors: dict) -> None:
    base_font = (FONT_FAMILY, FONT_SIZE_BODY)
    bold_font = (FONT_FAMILY, FONT_SIZE_BODY, "bold")

    style.configure(
        "TFrame",
        background=colors["bg_primary"],
    )

    style.configure(
        "Card.TFrame",
        background=colors["surface"],
        relief="solid",
        borderwidth=1,
    )

    style.configure(
        "TLabel",
        background=colors["bg_primary"],
        foreground=colors["text_primary"],
        font=base_font,
    )

    style.configure(
        "Secondary.TLabel",
        background=colors["bg_primary"],
        foreground=colors["text_secondary"],
        font=(FONT_FAMILY, FONT_SIZE_SMALL),
    )

    style.configure(
        "Title.TLabel",
        background=colors["bg_primary"],
        foreground=colors["text_primary"],
        font=(FONT_FAMILY, FONT_SIZE_TITLE, "bold"),
    )

    style.configure(
        "Primary.TButton",
        background=colors["primary"],
        foreground="#FFFFFF",
        font=bold_font,
        padding=(SPACE_3, SPACE_2),
        borderwidth=0,
    )
    style.map(
        "Primary.TButton",
        background=[("active", colors["primary_soft"]), ("disabled", colors["border"])],
        foreground=[("disabled", colors["text_secondary"])],
    )

    style.configure(
        "Secondary.TButton",
        background=colors["bg_secondary"],
        foreground=colors["text_primary"],
        font=bold_font,
        padding=(SPACE_3, SPACE_2),
        borderwidth=1,
    )
    style.map(
        "Secondary.TButton",
        background=[("active", colors["primary_soft"])],
    )

    style.configure(
        "TEntry",
        fieldbackground=colors["bg_primary"],
        foreground=colors["text_primary"],
        bordercolor=colors["border"],
        padding=SPACE_1,
    )

    style.configure(
        "Error.TEntry",
        fieldbackground=colors["bg_primary"],
        foreground=colors["text_primary"],
        bordercolor=colors["error"],
    )

    style.configure(
        "Treeview",
        background=colors["bg_primary"],
        fieldbackground=colors["bg_primary"],
        foreground=colors["text_primary"],
        bordercolor=colors["border"],
        font=base_font,
    )
    style.configure(
        "Treeview.Heading",
        background=colors["bg_secondary"],
        foreground=colors["text_secondary"],
        font=(FONT_FAMILY, FONT_SIZE_SMALL, "bold"),
    )
    style.map(
        "Treeview",
        background=[("selected", colors["primary_soft"])],
        foreground=[("selected", colors["text_primary"])],
    )
