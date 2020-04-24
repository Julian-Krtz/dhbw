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
	uint8_t gruen;
	uint8_t gelb;
	uint8_t rot;
};

uint8_t changepin(uint8_t port, int pin, int newValue) {
	//return newValue << (pin) | (0xFF & ~1<<(pin));
	//return (port & ~1 << (pin+1))| (newValue << (pin+1) | 0x00);
	return (port & ~ (1 << (pin)) ) | (newValue << (pin));  
}

int potenz(int basis, int exponent) {
	if (exponent == 0)
		return 1;
	return basis * potenz(basis, exponent-1);
}

int main(void)
{
	struct ampel ampel1;
	//ampel1.gruen = 
	
	DDRC = 0xFF;
	PORTC = 0xFF;
	/*
	DDRB=0xFF;
	PORTB=0xFF;
	DDRC=0xFF;
	PORTC=0xFF; */
	while (1)
	{
		PORTC = 0xFF;
		_delay_ms(1000);
		PORTC = changepin(PORTC,3,0);
		_delay_ms(1000);

		/*PORTB=0xFF;
		PORTC <<= 1;
		//6 LEDS
		if(PORTC >> 6 == 1)
		PORTC = 1;
		_delay_ms(100);*/
	}
	
}

