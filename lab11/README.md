# hacknote
- House of force
- Unsorted bin attack

## Vulnerability
Protection
>   Arch:     amd64-64-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)



Off-by-One vulnerability in add
```
	itemlist[i].name = (char*)malloc(length);
	...
	size = read(0,itemlist[i].name,length);
	itemlist[i].name[size] = '\x00';
	...

```
The header of next chunk will be modified

Heap overflow vulnerability in change in add
```
	...
	printf("Please enter the length of item name:");
	read(0,lengthbuf,8);
	length = atoi(lengthbuf);
	printf("Please enter the new name of the item:");
	readsize = read(0,itemlist[index].name,length);
	*(itemlist[index].name + readsize) = '\x00';
	...
```



## Solution1
1.Use heap over flow to modify the size of topchunk to -1 (0xfffffffffffffffff)
2.Malloc a great size so that the top locate before the real heap
3.The next malloc will reuse the beginning of the heap,which is the bamboo box
4.Then modify the bamboo box's function pointer to magic


Script [solve.py](./solve_house_of_force.py)
