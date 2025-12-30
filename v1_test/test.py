apis = ['SYNC_IMAGE_WRITABLE', 'SYNC_WIN_COMPLETED', 'SYNC_WIN_FLUSH', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__firstlineno__', '__format__', '__ge__',
  '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
  '__setattr__', '__sizeof__', '__static_attributes__', '__str__', '__subclasshook__', '__weakref__', '_img_height', '_python_ref_gen', '_python_ref_std', 'mlx_clear_window', 'mlx_destroy_image',
  'mlx_destroy_window', 'mlx_do_key_autorepeatoff', 'mlx_do_key_autorepeaton', 'mlx_do_sync', 'mlx_expose_hook', 'mlx_func', 'mlx_get_data_addr', 'mlx_get_screen_size', 'mlx_hook', 'mlx_init',
  'mlx_key_hook', 'mlx_loop', 'mlx_loop_exit', 'mlx_loop_hook', 'mlx_mouse_get_pos', 'mlx_mouse_hide', 'mlx_mouse_hook', 'mlx_mouse_move', 'mlx_mouse_show', 'mlx_new_image', 'mlx_new_window', 'mlx_pixel_put',
 'mlx_png_file_to_image', 'mlx_put_image_to_window', 'mlx_release', 'mlx_string_put', 'mlx_sync', 'mlx_xpm_file_to_image', 'so_file']
import mlx
import time

width = 2500
height = 1500
blue = 0x000FF

m = mlx.Mlx()

mlx_ptr = m.mlx_init()

win = m.mlx_new_window(mlx_ptr, width, height, "A-Maze-ing")

img = m.mlx_new_image(mlx_ptr, width, height)

for y in range(height):
    for x in range(width):
        m.mlx_pixel_put(mlx_ptr, img, x, y, blue)

m.mlx_put_image_to_window(mlx_ptr, win, img, 0, 0)
                
time.sleep(10)





