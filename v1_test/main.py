import mlx
import time

def callaback(*args):
    print("Exiting...")
    exit(0)

m = mlx.Mlx()
help(mlx)

mlx_ptr = m.mlx_init()
win = m.mlx_new_window(mlx_ptr, 2000, 1500, "MLX Python Test")
image = m.mlx_new_image(mlx_ptr, 2000, 1500)
(data, bpp, sline, endian) = m.mlx_get_data_addr(image)


for y in range(1500):
    for x in range(2000):
        offset = y * sline + x * (bpp // 8)
        data[offset] = 255
        data[offset + 1] = 255
        data[offset + 2] = 255
        data[offset + 3] = 255

m.mlx_put_image_to_window(mlx_ptr, win, image, 0, 0)

m.mlx_hook(win, 2 , 1, callaback, m)
m.mlx_loop(mlx_ptr)