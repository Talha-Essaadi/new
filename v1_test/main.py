import mlx
import time

# Create MLX instance
mlx_instance = mlx.Mlx()

# Initialize and get MLX pointer
mlx_ptr = mlx_instance.mlx_init()

# Create window (pass regular string, not bytes)
win = mlx_instance.mlx_new_window(mlx_ptr, 2000, 1500, "MLX Python Test")

# Draw a white pixel at (200, 150)
mlx_instance.mlx_pixel_put(mlx_ptr, win, 200, 150, 0xFFFFFF)

time.sleep(10)
