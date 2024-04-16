import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg2_img = pg.image.load("fig/pg_bg.jpg") #練習7
    bg2_img = pg.transform.flip(bg2_img, True, False) #練習7
    kk_img = pg.image.load("fig/3.png")  #練習2
    kk_img = pg.transform.flip(kk_img, True, False) #練習2
    kk_rct = kk_img.get_rect() # 練習8
    kk_rct.center = 300, 200
    tmr = 0
    dx = 0
    dy = 0
    while True:
        x = tmr % 3200 #練習6 #練習7
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            dx = -1
            dy = -1
        elif key_lst[pg.K_DOWN]:
            dx = -1
            dy = 1
        elif key_lst[pg.K_RIGHT]:
            dx = 2
            dy = 0
        elif key_lst[pg.K_LEFT]:
            dx = -2
            dy = 0
        else:
            dx = -1
            dy = 0
        kk_rct.move_ip(dx, dy)

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg2_img, [-x+1600, 0])
        screen.blit(bg_img, [-x+3200, 0])
        screen.blit(bg2_img, [-x+4800, 0])
        screen.blit(kk_img, kk_rct) #練習4
        pg.display.update()
        tmr += 1        
        clock.tick(200) #練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()