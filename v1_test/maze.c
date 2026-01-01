#include <mlx.h>


int main()
{
    void *mlx_ptr;
    void *win_ptr;
    int x, y;

    mlx_ptr = mlx_init();
    win_ptr = mlx_new_window(mlx_ptr, 2000, 1500, "MLX C Test");

    for (y = 0; y < 1500; y++)
    {
        for (x = 0; x < 2000; x++)
        {
            mlx_pixel_put(mlx_ptr, win_ptr, x, y, 0xFFFFFF);
        }
    }

    mlx_loop(mlx_ptr);
    return (0);
}