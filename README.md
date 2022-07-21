# FM_FC
Searching for fundamental matrix and full controlling.

Рассмотрим линейную систему, реализующую программное управление: <img src="https://latex.codecogs.com/svg.image?\dot{x}=P(t)&plus;Q(t)u&plus;f(t)" title="\dot{x}=P(t)+Q(t)u+f(t)" />,
<img src="https://latex.codecogs.com/svg.image?x&space;=&space;x(t)&space;\in&space;R^n&space;" title="x = x(t) \in R^n " /> - вектор фазовых переменных, <img src="https://latex.codecogs.com/svg.image?u=u(t)&space;\in&space;R^m&space;" title="u=u(t) \in R^m " /> - вектор управления,
<img src="https://latex.codecogs.com/svg.image?f(t)&space;\in&space;R^n&space;" title="f(t) \in R^n " />, и координаты точки для t = t0 и t = T.

Требуется найти полное управление на [t0;T], по следующему алгоритму:
1) Проверка системы на ПУ.  Для этого составляем матрицу Калмана и если ранг матрицы Калмана равен n - строим ПУ.
2) Строим ФМ однородной системы. В представленном коде ФМ строится методом интерполяционных полиномов. 
3) Нормируем полученную ФМ.
Находим вспомогательные коэффициенты:
4) <img src="https://latex.codecogs.com/svg.image?B(t)&space;=&space;Y^{-1}Q(t)&space;" title="B(t) = Y^{-1}Q(t) " />
5) <img src="https://latex.codecogs.com/svg.image?A&space;=&space;\int_{t_0}^{T}B(t)B^T(t)dt&space;" title="A = \int_{t_0}^{T}B(t)B^T(t)dt " />
6) <img src="https://latex.codecogs.com/svg.image?\nu&space;=&space;Y^{-1}(T)x_1-x_0-\int_{0}^{T}Y^{-1}(\tau)f(\tau)d\tau&space;" title="\nu = Y^(-1)(T)x_1-x_0-\int_{0}^{T}Y^(-1)(\tau)f(\tau)d\tau " />
7) Найти решение С системы уравнений: <img src="https://latex.codecogs.com/svg.image?AC&space;=&space;\nu" title="AC = \nu" /> 
Тогда найденное ПУ представимо в следующем виде: <img src="https://latex.codecogs.com/svg.image?u(t)&space;=&space;B^TC" title="u(t) = B^TC" />
