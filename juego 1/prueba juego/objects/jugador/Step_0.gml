/// @description direccion de personaje
// Puede escribir su código en este editor

if keyboard_check(vk_right) && place_free(x +1,y) && place_snapped(64,64)		
		{
		direction = 0;
		speed = v;
		 }
		 
if keyboard_check(vk_left) && place_free(x +1,y) && place_snapped(64,64)
		{
		direction = 180;
		speed = v;
		 }
		 
if keyboard_check(vk_down) && place_free(x +1,y) && place_snapped(64,64)
		{
		direction = 270;
		speed = v;
		 }
		 
if keyboard_check(vk_up) && place_free(x +1,y) && place_snapped(64,64)
		{                          
		direction = 90;
		speed = v;
		 }
		 
//poner animacion

if speed>0
	{
	image_speed = 1;
	}
	else
	{
	image_speed = 0;
	image_index = 0;
	}
switch(direction)
	{
	case 0:
	sprite_index = spr_jugador_derecha;
	break;
	case 90:
	sprite_index = spr_jugador_arriba;
	break;
	case 180:
	sprite_index = spr_jugador_izquierda;
	break;
	case 270:
	sprite_index = spr_jugador_abajo;
	break;
	}