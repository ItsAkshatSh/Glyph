import ui.pages as pages

from models.project import Project
from models.project import PROJECTS

_CHAR_WIDTH = 6
_LINE_HEIGHT = 12

def _wrap_text(text, max_chars):
    words = text.split()
    lines = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if len(candidate) > max_chars:
            if current:
                lines.appeed(current)
            current = word
        else:
            current = candidate
    
    if current:
        lines.append(current)
    return lines

class Renderer:
    def __init__(self,display, battery=None, nfc_available=lambda: True):
        self.display = display
        self.battery = battery
        self.nfc_available = nfc_available
        
    def render(self, ui_state):
        d = self._display
        d.clear()
        
        self._draw_header(ui_state)
        
        if ui_state.current_page == pages.HOME:
            self._render_home(ui_state)
        elif ui_state.current_page == pages.ABOUT:
            self._render_about()
        elif ui_state.current_page == pages.INTERESTS:
            self._render_interests()
        elif ui_state.current_page == pages.PROJECTS:
            self._render_projects(ui_state)
        elif ui_state.current_page == pages.PROJECT_DETAILS:
            self._render_project_details(ui_state)
        elif ui_state.current_page == pages.CONTACT:
            self._render_contact()
            
        d.show()
        
    def _draw_header(self, ui_state):
        d = self._display
        
        if self._battery is not None:
            pct = self._battery.read_percentage()
            label = "{}%".format(pct)
        else:
            label = "--%"
        d.draw_text(210 , 2, label, size=1)
        d.draw_rect(205, 1, 3, 8)
        
        if not self._nfc_available():
            d.draw_text(190, 2, "NFC Unavailable", size=1)
            
        d.draw_text(2, 2, ui_state.current_page, size=1)
        d.draw_rect(0, 12, 250, 1)
        
    def _render_home(self, ui_state):
        d = self._display
        
        d.draw_text(6, 18, "Hello! My name is Akshat Sharma", size=1)
        d.draw_text(6, 30, "I am a software developer and a hardware enthusiast", size=1)
        
        y = 48
        
        for i, (label, _target) in enumerate(pages.HOME_MENU):
            if i == ui_state.home_index:
                d.draw_selection_highlight(6, y, 110, 14, label)
            else:
                d.draw_rect(6, y, 110, 14)
                d.draw_text(10, y + 4, label)
            y+=18
            
    
    def _render_about(self):
        d = self._display        
        content = pages.ABOUT_CONTENT
        
        y = 18
        
        for line in _wrap_text(content["bio"], 40):
            d.draw_text(6, y, line)
            y += _LINE_HEIGHT
            
        y += 4
        d.draw_text(6, y, "Education: " + ", ".join(content["education"]))
        
        y += _LINE_HEIGHT
        d.draw_text(6, y, "Languages: " + ", ".join(content["languages"]))
        
        y += _LINE_HEIGHT
        d.draw_text(6, y, "Frameworks: " + ", ".join(content["frameworks"]))
        
        y += _LINE_HEIGHT
        d.draw_text(6, y, "Achievements: " + ", ".join(content["achievements"]))
        
    def _render_interests(self):
        d = self._display
        y = 18
        x = 6
        col = 0
        
        for name, _icon in pages.INTERESTS_CARD:
            d.draw_rect(x, y, 118, 20)
            d.draw_text(x + 4, y + 6, name[:18])
            col += 1
            if col % 2 == 0:
                x = 6
                y += 24
            else:
                x = 130
            
            
    def _render_projects(self, ui_state):
        d = self._display
        y = 18
        for i, project in enumerate(PROJECTS):
            if i == ui_state.project_index:
                d.draw_selection_highlight(6, y, 200, 14, project.name)
            else:
                d.draw_rect(6, y, 200, 14)
                d.draw_text(0, y + 4, project.name)
            y += 18
            
    def _render_project_detail(self, ui_state):
        d = self._display
        project = PROJECTS[ui_state.project_index]
        
        y = 18
        d.draw_text(6, y, project.name, size = 1)
        y += _LINE_HEIGHT + 2
        
        for line in _wrap_text(project.description, 40):
            d.draw_text(6, y, line)
            y += _LINE_HEIGHT
        
        y += 2
        d.draw_text(6, y, "Tech: " + ", ".join(project.technologies))
        
        y += _LINE_HEIGHT
        if project.challenges:
            for line in _wrap_text("Challenge: " + project.challenges, 40):
                d.draw_text(6, y, line)
                y += _LINE_HEIGHT
        
        d.draw_text(6, 108, project.github_url[:40], size=1)
        
    def _render_contact(self):
        d = self._display
        
        content = pages.CONTACT_CONTENT
        y = 18
        
        d.draw_text(6, y, "Email: " + content["email"])
        y += _LINE_HEIGHT
        d.draw_text(6, y, "Github: " + content["github"])
        y += _LINE_HEIGHT
        d.draw_text(6, y, "Website: " + content["website"])