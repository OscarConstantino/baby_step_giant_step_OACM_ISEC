# baby_step_giant_step_OACM_ISEC
Baby Step - Giant Step implementation

This discrete log problem algorithm helps to solve `𝑘` in the expression `𝑎 ≡ 𝑔𝑘 mod 𝑝`.

The program will ask for the next parameters:

```
𝑝: prime number
𝑎: integer number
𝑔: an integer number, primitive root module of 𝑝 
```

The parameters will be asked after the program has started, here is an example:

![Screenshot 2024-09-15 at 20 09 30](https://github.com/user-attachments/assets/5e512d72-3f0e-4c07-8cd0-b74fd3dd7a02)

The program has three different modes:

```
1: Calculate k using [𝑎 · 𝑔^−𝑟 mod 𝑝] for baby step and (𝑔^𝐵)^𝑞 mod 𝑝 for the giant step
2: Calculate k using Fermat's Little Theorem. Calculating baby steps as 𝑔^𝑟 mod 𝑝 and a * (c^j mod 𝑝) mod 𝑝
3: Verifies if 𝑝 is a prime number
```
The program should display the list of the baby and giant steps iterations and the results of 𝑘 = j · b + r, here is an image:

![Screenshot 2024-09-15 at 20 36 05](https://github.com/user-attachments/assets/3ed7b18b-7e5e-465b-8469-6dceee9e553f)
