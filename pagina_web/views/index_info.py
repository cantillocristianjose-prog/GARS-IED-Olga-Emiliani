import reflex as rx
import styles.styles as styles
from routers import Route
from styles.styles import Size,Spacing
from components.link_button import link_button
from components.info_text import info_text
from components.title import title
from styles.colors import Color 

def index_info() -> rx.Component:
    return rx.vstack(
        title("Formulacion Estrategica"),
        rx.box(
            info_text(
                "Justificación / Identificación del problema:",
                """
                Actualmente, muchos estudiantes presentan dificultades en algunas competencias evaluadas en las Pruebas Saber, lo que puede afectar su desempeño académico y sus oportunidades de acceso a la educación superior. Sin un análisis detallado de los resultados, es difícil identificar las fortalezas y las áreas que requieren mayor atención.
                
                Este proyecto se relaciona directamente con la Institución Educativa Distrital (IED) Olga Emiliani, ya que permite conocer el rendimiento de los estudiantes y generar información útil para la toma de decisiones orientadas al mejoramiento de la calidad educativa. Además, beneficia a la comunidad educativa al proporcionar datos que faciliten la implementación de estrategias de apoyo y fortalecimiento académico.

                La importancia de este proyecto radica en que permitirá a los estudiantes reconocer sus fortalezas y oportunidades de mejora en cada área evaluada, contribuyendo a una mejor preparación para futuras pruebas y a un mayor desarrollo de sus competencias académicas.

                """
            ),
            info_text(
                "Objetivos:",
                """
                Objetivo general:
                Diseñar e implementar un prototipo en RStudio que permita identificar fortalezas y oportunidades en las competencias evaluadas en los resultados de las Pruebas Saber, brindando información estratégica que contribuya al mejoramiento del desempeño académico de los estudiantes del IED Olga Emiliani.

                Objetivos Específicos:
 
                Diseñar e implementar un herramienta en RStudio que interprete los resultados académicos basados en datos de las Pruebas Saber, con el propósito de proporcionar información clara y útil a la institución educativa  IED Olga Emiliani.

                Diseñar un prototipo en RStudio para analizar las fortalezas y oportunidades de mejora en las diferentes áreas y competencias evaluadas en las pruebas saber aplicadas en la IED Olga Emiliani.

                Implementar un prototipo en RStudio que genere un reporte de fortalezas y oportunidades para mejorar en las diferentes áreas y competencias evaluadas en las pruebas saber aplicadas en la IED Olga Emiliani.

                """
            ),
            border_radius="10px",
            background_color=Color.BACKGROUND_BOX.value,
            padding=Size.DEFAULT.value,
            width="100%"
        ),

        link_button(
            "Nexus Analitica",
            "Equipo encargado de este proyecto",
            "/icons/logotipo_de_nexus.jpg",
            Route.CREDITOS.value,
            is_external=False
        ),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )