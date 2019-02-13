
#Robin's hitcon training write-up
Source: https://github.com/scwuaptx/HITCON-Training/
## Outline

+ Basic Knowledge(Skip)
+ Stack Overflow
	+ Buffer Overflow
	+ Return to Text/Shellcode
		+ lab 3 - ret2shellcode 
	+ Protection
		+ ASLR/DEP/PIE/StackGuard
	+ Lazy binding
	+ Return to Library
		+ lab 4 - ret2lib 
+ Return Oriented Programming
	+ ROP
		+ lab 5 - simple rop 
	+ Using ROP bypass ASLR
		+ ret2plt
	+ Stack migration
		+ lab 6 - migration
+ Format String Attack
	+ Format String 
	+ Read from arbitrary memory
		+ lab 7 - crack
	+ Write to arbitrary memory
		+ lab 8 - craxme
	+ Advanced Trick
		+ EBP chain 
		+ lab 9 - playfmt 
+ x64 Binary Exploitation
	+ x64 assembly
	+ ROP
	+ Format string Attack

+ Heap exploitation
	+ Glibc memory allocator overview
	+ Vulnerablility on heap
		+ Use after free
			+ lab 10 - hacknote
		+ Heap overflow 
			+ house of force 
				+ lab 11 - 1 - bamboobox1
			+ unlink
				+ lab 11 - 2 - bamboobox2
+ Advanced heap exploitation
	+ Fastbin attack
		+ lab 12 - babysecretgarden 
	+ Shrink the chunk
	+ Extend the chunk
		+ lab 13 -  heapcreator
	+ Unsortbin attack
		+ lab 14 - magicheap
+ C++ Exploitation
	+ Name Mangling 
	+ Vtable fucntion table
	+ Vector & String
	+ New & delete
	+ Copy constructor & assignment operator
		+ lab 15 - zoo 
