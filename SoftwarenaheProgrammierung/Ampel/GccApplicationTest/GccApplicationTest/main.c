/*
 * GccApplicationTest.c
 *
 * Created: 24.04.2020 15:54:49
 * Author : julim
 */ 
#define F_CPU 16000000UL
#include <avr/io.h>
#include <avr/delay.h>

struct ampel  
{
	int gruen;
	int gelb;
	int rot;
	uint8_t* port;
};

uint8_t changepin(uint8_t* port, int pin, int newValue) {
	return (*port & ~ (1 << (pin)) ) | (newValue << (pin));  
}

int potenz(int basis, int exponent) {
	if (exponent == 0)
		return 1;
	return basis * potenz(basis, exponent-1);
}

void goGreen(struct ampel a) {
	PORTC = changepin(a.port,a.rot, 1);
	PORTC = changepin(a.port,a.gelb, 1);
	PORTC = changepin(a.port,a.gruen, 0);		
	_delay_ms(2000);
	PORTC = changepin(a.port,a.rot, 0);
	PORTC = changepin(a.port,a.gelb, 0);
	PORTC = changepin(a.port,a.gruen, 1);
}

void goRed(struct ampel a) {
	PORTC = changepin(a.port,a.rot, 0);
	PORTC = changepin(a.port,a.gelb, 1);
	PORTC = changepin(a.port,a.gruen, 0);
	_delay_ms(2000);
	PORTC = changepin(a.port,a.rot, 1);
	PORTC = changepin(a.port,a.gelb, 0);
	PORTC = changepin(a.port,a.gruen, 0);
}

int main(void)
{
	struct ampel ampel1;
	ampel1.gruen = 0;
	ampel1.gelb = 1;
	ampel1.rot = 2;
	ampel1.port = &PORTC;
	
	DDRC = 0xFF;
	PORTC = 0x00;
	/*
	DDRB=0xFF;
	PORTB=0xFF;
	DDRC=0xFF;
	PORTC=0xFF; */
	while (1)
	{
		goGreen(ampel1);
		_delay_ms(2000);
		goRed(ampel1);
		_delay_ms(2000);

		/*PORTB=0xFF;
		PORTC <<= 1;
		//6 LEDS
		if(PORTC >> 6 == 1)
		PORTC = 1;
		_delay_ms(100);*/
	}
	
}

