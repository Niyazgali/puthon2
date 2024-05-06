import pygame

class SceneBase: #база әдістерін анықтайды.
    def init(self):
        self.next = self
    
    def ProcessInput(self, events, pressed_keys):#пернелерді және тінтуірді басу кодын анықтайды
        print("uh-oh, you didn't override this in the child class")

    def Update(self):#жаңартып тұрады
        print("uh-oh, you didn't override this in the child class")

    def Render(self, screen): #элементердің суретін салып береді
        print("uh-oh, you didn't override this in the child class")

    def SwitchToScene(self, next_scene):#сценаны келесі сценаға ауыстырып береді
        self.next = next_scene
    
    def Terminate(self):# Ойынды аяқтап береді
        self.SwitchToScene(None)

class DrawingScene(SceneBase):
    def init(self):
        SceneBase.init(self)
        self.shapes = []  # Фигураларды сақтайды
        self.current_color = (0, 0, 0)  # түс қою
        self.current_tool = "Rectangle"  # Сурет салу үшін құрал
    
    def ProcessInput(self, events, pressed_keys):#пернені басу
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # мышканың сол жақ тінтуірін басқан кезде фигуралар шығады
                    if self.current_tool == "Rectangle":
                        pos = pygame.mouse.get_pos()#тіктөрбұрыштың сол жақ жоғарғы бұрышыныңкоординаттар алады
                        rect = pygame.Rect(pos[0], pos[1], 50, 50)  # Өлшем беру
                        self.shapes.append((rect, self.current_color))#кортежде сақтайды
                    elif self.current_tool == "Circle":
                        pos = pygame.mouse.get_pos()
                        circle = (pos[0], pos[1], 25)  # шеңбер центрі координатары және радиус
                        self.shapes.append((circle, self.current_color))
                    elif self.current_tool == "Eraser":
                        # Фигураларды басып жою
                        pos = pygame.mouse.get_pos()
                        for shape in self.shapes:
                            if isinstance(shape[0], pygame.Rect) and shape[0].collidepoint(pos):
                                self.shapes.remove(shape)#фигураның квадрат екенін анықтап, тінтуір басы квадрат ішінде болса жояды
                            elif isinstance(shape[0], tuple) and ((shape[0][0] - pos[0])**2 + (shape[0][1] - pos[1])**2) <= shape[0][2]**2:
                                self.shapes.remove(shape)#фигураның шеңбер екенін анықтап, тінтуір басы шеңбер ішінде болса жояды
                elif event.button == 3:  # Right mouse button
                    # Тінтуірдің оң жақ түймешігі басылса, түсін өзгертіңіз
                    self.current_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            elif event.type == pygame.KEYDOWN:#клавиш басуын тексереді
                if event.key == pygame.K_r:
                    self.current_tool = "Rectangle"
                elif event.key == pygame.K_c:
                    self.current_tool = "Circle"
                elif event.key == pygame.K_e:
                    self.current_tool = "Eraser"
    
    def Update(self):
        pass
    
    def Render(self, screen):#графикалық элементке түс береді
        screen.fill((255, 255, 255))  # White background
        for shape, color in self.shapes:
            if isinstance(shape, pygame.Rect):#егер фигура квадрат болса салып береді
                pygame.draw.rect(screen, color, shape)
            elif isinstance(shape, tuple):#егер фигура шеңбер болса салып береді
                pygame.draw.circle(screen, color, (shape[0], shape[1]), shape[2])
                
def run_game(width, height, fps, starting_scene):
    pygame.init()
    screen = pygame.display.set_mode((width, height))#терезе өлшемі
    clock = pygame.time.Clock()#частовой кадр жылдамдығы

    active_scene = starting_scene