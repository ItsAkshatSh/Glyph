from buttons.buttons import LEFT, RIGHT, SELECT, PRESSED
import ui.pages as pages
from models.project import PROJECTS 

class UIStateMachine:
    def __init__(self):
        self.current_page = pages.HOME
        self.home_index = 0
        self.project_index = 0
        
        self._handlers = {
            pages.HOME: self._handle_home,
            pages.ABOUT: self._handle_simple_subpage,
            pages.INTERESTS: self._handle_simple_subpage,
            pages.CONTACT: self._handle_simple_subpage,
            pages.PROJECTS: self._handle_projects,
            pages.PROJECT_DETAILS: self._handle_project_detail
        }
        
    def handle_event(self, event):
        
        if event.kind != PRESSED:
            return False
        
        handler = self._handlers[self.current_page]
        return handler(event)
    
    def _handle_home(self, event):
        if event.button == LEFT:
            self.home_index = (self.home_index - 1) % len(pages.HOME_MENU)
            return True
        if event.button == RIGHT:
            self.home_index = (self.home_index + 1) % len(pages.HOME_MENU)
            return True
        if event.button == SELECT:
            _, target_page = pages.HOME_MENU[self.home_index]
            self.current_page = target_page
            return True
        return False
    
    def _handle_simple_subpage(self, event):
        if event.button == LEFT:
            self.current_page = pages.HOME
            return True
        return False
    
    def _handle_projects(self, event):
        if event.button == LEFT:
            if self.project_index == 0:
                self.current_page = pages.HOME
            else:
                self.project_index -= 1
            return True
        if event.button == RIGHT:
            self.project_index = (self.project_index + 1) % len(PROJECTS)
            return True
        if event.button == SELECT:
            self.current_page = pages.PROJECT_DETAILS
            return True
        return False
    
    def _handle_project_detail(self, event):
        if event.button in (LEFT, SELECT):
            self.current_page = pages.PROJECTS
            return True
        
    
    def get_current_nfc_url(self):
        if self.current_page == pages.PROJECT_DETAILS:
            return PROJECTS[self.project_index].github_url
        return pages.NFC_URLS[self.current_page]