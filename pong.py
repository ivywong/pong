import pygame


class Paddle:
    """"""
    def __init__(self, game, x, y):
        self.game = game

        self.rect = pygame.Rect(0, 0, 50, 200)
        self.rect.center = (x, y)
        self.speed = 10
        
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)

        self.game.screen.fill("white", self.rect)

    def update(self):
        if self.moving_up and self.rect.top < (self.game.screen_rect.top - 50):
            self.y -= self.speed
            print("moving up")
        if self.moving_down and self.rect.bottom > (self.game.screen_rect.bottom - 50):
            self.y += self.speed
            print("moving down")
        # Update rect object from self.x
        self.rect.y = self.y

    def draw(self):
        # do something
        self.game.screen.fill("white", self.rect)

class Pong:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Ivy and Ava's Best Pong Ever")
        
        self.screen = pygame.display.set_mode((1280, 720))
        self.screen_rect = self.screen.get_rect()
        
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.screen.fill("red")
        self.paddle_left = Paddle(self, 0, self.screen_rect.centery)
        self.paddle_right = Paddle(self, (self.screen_rect.right - 25), self.screen_rect.centery)

        self.wall_top = pygame.Rect(0, 0, self.screen_rect.width, 50)
        self.wall_bottom = pygame.Rect(0, 0, self.screen_rect.width, 50)
        self.divider = pygame.Rect(0, 0, 10, self.screen_rect.height)
        self.wall_bottom.bottom = self.screen_rect.bottom
        self.divider.center = self.screen_rect.center
        self.screen.fill((141, 29, 5), self.divider)
        self.screen.fill("white", self.wall_top)
        self.screen.fill("white", self.wall_bottom)

        
        
    def run_game(self):
        while self.running:
            self._check_events()
            self.paddle_left.update()
            self.paddle_right.update()
            self._update_screen()

            pygame.display.flip()
            self.clock.tick(60)

    def _update_screen(self):
        self.paddle_left.draw()
        self.paddle_right.draw()
         

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
         if event.key == pygame.K_UP:
            self.paddle_right.moving_up = True
         elif event.key == pygame.K_DOWN:
            self.paddle_right.moving_down = True
         elif event.key == pygame.K_w:
             self.paddle_left.moving_up = True
         elif event.key == pygame.K_s:
             self.paddle_left.moving_down = True

    def _check_keyup_events(self, event):
         if event.key == pygame.K_UP:
            self.paddle_right.moving_up = False
         elif event.key == pygame.K_DOWN:
            self.paddle_right.moving_down = False
         elif event.key == pygame.K_w:
             self.paddle_left.moving_up = False
         elif event.key == pygame.K_s:
             self.paddle_left.moving_down = False        
        
if __name__ == '__main__':
    #Make a game instance, and run the game.
    pong = Pong()
    pong.run_game()