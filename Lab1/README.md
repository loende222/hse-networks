# Реализация небольшой сети офиса

### Структура работы
В папке `src` лежат конфиги отдельных устройств и `Lab1.uml`.
В папке `img` лежат скриншоты приложенные ниже.
Далее содержится описание работы и демонстрация работоспособности сети.

## Настройка

Топология сети:

![Топология](img/topology.jpg)

### Настройка клиентов

Настройка `VPC1`:

![VPC1](img/VPC1_setting.jpg)

Настройка `VPC2`:

![VPC1](img/VPC2_setting.jpg)

### Настройка коммутаторов уровня доступ

Настройка `S1`

Состояние перед настройкой:

![S1_before_setting](img/S1_before_setting.jpg)

Конфигурация:

![S1_setting](img/S1_setting.jpg)

Состояние после настройки:

![S1_after_setting](img/S1_after_setting.jpg)

Настройка `S2` (почти аналогично)

Состояние перед настройкой:

![S2_before_setting](img/S2_before_setting.jpg)

Конфигурация:

![S2_setting](img/S2_setting.jpg)

Состояние после настройки:

![S2_after_setting](img/S2_after_setting.jpg)

### Настройка коммутатора уровня распределения

Настройка `S3`

Состояние перед настройкой

![S3_before_setting](img/S3_before_setting.jpg)

Конфигурация:

![S3_setting](img/S3_setting.jpg)

Состояние после настройки:

![S3_after_setting](img/S3_after_setting.jpg)

### Настройка маршрутизатора

Настройка `R`

Состояние перед настройкой:

![R_before_setting](img/R_before_setting.jpg)

Конфигурация:

![R_setting](img/R_setting.jpg)

Состояние после настройки:

![R_after_setting](img/R_after_setting.jpg)

## Проверка работоспособности

Пинги с `VPC1`:

![VPC1_pings](img/VPC1_pings.jpg)

Пинги с `VPC2`:

![VPC2_pings](img/VPC2_pings.jpg)

## Проверка STP

Spanning-tree `S1`:

![S1_spanning_tree_pt1](img/S1_spanning_tree_pt1.jpg)
![S1_spanning_tree_pt2](img/S1_spanning_tree_pt2.jpg)
![S1_spanning_tree_pt3](img/S1_spanning_tree_pt3.jpg)

Spanning-tree `S2`:

![S2_spanning_tree_pt1](img/S2_spanning_tree_pt1.jpg)
![S2_spanning_tree_pt2](img/S2_spanning_tree_pt2.jpg)
![S2_spanning_tree_pt3](img/S2_spanning_tree_pt3.jpg)

## Проверка отказоустойчивости

Отключаем интерфейс между `S3` и `S1`:

![shutdown](img/shutdown.jpg)

Пинги какое-то время не работают, но затем сеть восстанавливается:

![VPC1_pings_shutdown](img/VPC1_pings_shutdown.jpg)
![VPC2_pings_shutdown](img/VPC2_pings_shutdown.jpg)
