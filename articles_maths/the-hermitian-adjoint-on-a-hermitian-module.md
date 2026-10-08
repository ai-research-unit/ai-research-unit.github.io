# __The Hermitian Adjoint on a Hermitian Module__

## Introduction

A Hermitian module over a Hermitian algebra is a module carrying a form for which the action is self-adjoint, $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$; the axiom says that the adjoint of the action of $x$ is the action of the involution, $\rho(x)^{*} = \rho(x^{\dagger})$. This article develops the adjoint operation on the module: the Hermitian adjoint of an operator on the module, the involution that the adjoint induces on the elements of the module, and the self-adjoint operators and self-adjoint elements of the module.

The module adjoint has the same shape as the algebra adjoint and one extra layer. The shape is that the adjoint of an operator is again an operator on the module, with $T^{**} = T$, $(TS)^{*} = S^{*}T^{*}$ and the positivity of $T^{*}T$; the extra layer is that the module carries an involution of its own, induced from the algebra by a cyclic vector, and the induced involution is the module's Tomita operator. With a cyclic and separating vector $\xi$ the map $S_M(x\cdot\xi) = x^{\dagger}\cdot\xi$ is an antilinear involution of the module; its polar decomposition produces a modular operator and a modular conjugation of the module, and the module adjoint of an operator intertwining the action is the same operation as the algebra adjoint transported by the module's modular data.

This article fixes the adjoint of a module operator and its calculus, the induced involution and the module Tomita operator, and the self-adjoint operators and elements of the module, with the relation to the algebra through the action.

The Hermitian algebra, its involution and its module forms are *Hilbert Algebras* and *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*; the adjoint of the action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*; the adjoints of the multiplications are *The Adjoint of the Left and the Right Multiplication* and *The Adjoint of the Left Multiplication on a Hermitian Algebra*; the positivity is *Self-Adjoint Elements and the Positive Cone*; the modular objects are *The Modular Operator and Tomita-Takesaki Theory*. Those are cited. The algebra is $A$ with involution $\dagger$ and form $\langle\cdot,\cdot\rangle$, the module is $M$ with form $(\cdot,\cdot)$, and the action is written $x\cdot s$ for $x\in A$, $s\in M$.

## The Adjoint of a Module Operator

**Definition.** An operator on the module is a linear map $T$ with dense domain in $M$; its **Hermitian adjoint** $T^{*}$ is defined by

$$
(T s,t) = (s,T^{*}t) \qquad \text{for all } s\in\mathrm{dom}\,T,\ t\in\mathrm{dom}\,T^{*} .
$$

**Proposition (the calculus).** For densely defined closed operators the adjoint satisfies $T^{**} = T$; for bounded operators $S,T$ it satisfies $(S+T)^{*} = S^{*}+T^{*}$, $(\alpha T)^{*} = \bar\alpha T^{*}$ and $(ST)^{*} = T^{*}S^{*}$; and $T^{*}T$ is positive, $(T^{*}Ts,s) = \|Ts\|^{2}\geq0$.

**Proof.** The defining identity with the two sides exchanged gives $T^{**}\supseteq T$ and equality for closed $T$; the sum and scalar rules are immediate from the definition; the product rule is the defining identity applied twice; the positivity is the definition of the adjoint with $t = s$.

**Theorem (the adjoint of the action).** For every $x\in A$,

$$
\rho(x)^{*} = \rho(x^{\dagger}) ,
$$

so the action of $A$ on $M$ is a $\ast$-representation with the involution of the algebra and the Hermitian adjoint of the module.

**Proof.** The module axiom is exactly $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$; comparing with the definition of the adjoint gives $\rho(x)^{*} = \rho(x^{\dagger})$.

**Proposition (the adjoint of a composite of actions).** For $x, y\in A$ and bounded module operators $S,T$,

$$
\bigl(\rho(x)S\,\rho(y)\bigr)^{*} = \rho(y^{\dagger})S^{*}\rho(x^{\dagger}) ,
$$

so adjacency reverses the order and turns each action into the action of the involution.

**Proof.** Apply the calculus of the first proposition and the theorem.

**Remark (the two adjoints on the module).** The module carries two adjoint operations that must not be confused: the **operator adjoint** $T\mapsto T^{*}$, acting on the operators of the module, and the **element involution** $s\mapsto s^{\dagger}$, defined below on the elements of the module. The first is the Hermitian adjoint for the module form; the second is induced by the algebra involution through a cyclic vector. They agree on the action operators, by the theorem, and they differ on general elements of the module, as the next section shows.

## The Induced Involution

**Definition.** Let $\xi\in M$ be cyclic and separating for the action: the set $A\cdot\xi$ is dense in $M$, and $x\cdot\xi = 0$ forces $x = 0$. The **induced involution** (or **module Tomita operator**) is the antilinear map

$$
S_M : A\cdot\xi\longrightarrow M , \qquad S_M(x\cdot\xi) = x^{\dagger}\cdot\xi ,
$$

and the involution of an element $s = x\cdot\xi$ is $s^{\dagger} = x^{\dagger}\cdot\xi$.

**Proposition (the induced involution is well defined and involutive).** With $\xi$ separating, $S_M$ is well defined, antilinear, and $S_M^{2} = \mathrm{id}$; the involution of the module satisfies

$$
(x\cdot s)^{\dagger} = s^{\dagger}\cdot x^{\dagger} , \qquad (s^{\dagger})^{\dagger} = s ,
$$

so the module is a module over the involution as well, and the two structures are compatible.

**Proof.** If $x\cdot\xi = y\cdot\xi$ then $(x-y)\cdot\xi = 0$ and $x = y$ by separatingness, so $S_M$ is well defined; antilinearity and involutivity are those of the algebra involution; the first displayed identity is $(xy)\cdot\xi\mapsto (xy)^{\dagger}\cdot\xi = y^{\dagger}\cdot x^{\dagger}\cdot\xi$; the second is $S_M^{2} = \mathrm{id}$.

**Theorem (polar decomposition of the module involution).** The closure of $S_M$ has a polar decomposition

$$
\bar S_M = J_M\,\Delta_M^{1/2} ,
$$

with $J_M$ an antiunitary involution and $\Delta_M = \bar S_M^{*}\bar S_M\geq0$ the **modular operator of the module**; the identities $\Delta_M = \bar S_M^{*}\bar S_M$, $J_M\Delta_MJ_M = \Delta_M^{-1}$ and $J_M\Delta_M^{it}J_M = \Delta_M^{-it}$ hold as in the algebra case.

**Proof.** The same polar-decomposition argument as for the algebra involution, applied to the closed antilinear involution $\bar S_M$ of $M$.

**Proposition (the action is compatible with the modular data).** The action of $A$ satisfies

$$
S_M\,\rho(x)\,S_M = \rho(x^{\dagger}) \quad\text{on } A\cdot\xi, \qquad \Delta_M^{it}\,\rho(x)\,\Delta_M^{-it} = \rho(\sigma_t(x)) ,
$$

where $\sigma_t$ is the modular automorphism of the algebra; so the modular structures of the module and of the algebra are intertwined by the action.

**Proof.** On $A\cdot\xi$, $S_M\rho(x)S_M(y\cdot\xi) = S_M(x\cdot y\cdot\xi) = (xy)^{\dagger}\cdot\xi = y^{\dagger}\cdot x^{\dagger}\cdot\xi = \rho(x^{\dagger})(y\cdot\xi)$; the second identity is the modular flow of the algebra acting on the coefficients, as in *The Modular Operator and Tomita-Takesaki Theory*.

## Self-Adjoint Operators and Elements

**Definition.** A module operator is **self-adjoint** when $T^{*} = T$, **positive** when $(Ts,s)\geq0$ for every $s$ in the domain of the form pairing, and **unitary** when $T^{*}T = TT^{*} = \mathrm{id}$; an element $s$ is **self-adjoint** when $s^{\dagger} = s$.

**Proposition (the self-adjoint elements form a real form).** The set of self-adjoint elements of $M$ is a real vector space, and every element is uniquely $s = s_1 + i s_2$ with $s_1, s_2$ self-adjoint; the involution is the conjugation with respect to this real form.

**Proof.** The involution is antilinear and involutive, so $s_1 = \tfrac12(s+s^{\dagger})$ and $s_2 = \tfrac{1}{2i}(s-s^{\dagger})$ are self-adjoint; expanding, $s_1+is_2 = s$. For uniqueness, if $s_1+is_2 = s_1'+is_2'$ with all four self-adjoint then $s_1-s_1' = i(s_2'-s_2)$ is at once self-adjoint and anti-self-adjoint, hence zero, and then $s_2 = s_2'$.

**Proposition (self-adjointness of the actions).** The action $\rho(x)$ is self-adjoint exactly when $x = x^{\dagger}$, positive when $x$ lies in the positive cone of the algebra, and unitary when $x$ is unitary; so the self-adjoint, positive and unitary operators of the module of the action kind are exactly those of the algebra.

**Proof.** $\rho(x)^{*} = \rho(x^{\dagger})$ by the theorem, and the action is faithful by the separatingness of $\xi$; the positivity is $(x\cdot s,s) = (s,x^{\dagger}\cdot s)$ with $x = x^{\dagger}$ and the positivity of the algebra cone.

**Proposition (the module adjoint of an intertwiner).** If $T\in B(M)$ intertwines the action, $T\rho(x) = \rho(x)T$ for every $x$, then $T^{*}$ intertwines the action as well; so the adjoint of an intertwiner is an intertwiner, and the self-adjoint intertwiners are the self-adjoint elements of the commutant of the action.

**Proof.** Taking adjoints in $T\rho(x) = \rho(x)T$ gives $\rho(x^{\dagger})T^{*} = T^{*}\rho(x^{\dagger})$ by the theorem, hence $T^{*}\rho(y) = \rho(y)T^{*}$ for every $y$, since the involution is of order two.

## Worked Cases

### The Regular Module

For $M = A$ with the form $(s,t) = \langle s,t\rangle$ and $\xi = 1$, the action is the left multiplication, the induced involution is the involution of the algebra, and the module adjoint of $\rho(x)$ is $\rho(x^{\dagger})$, recovering the adjoint of *The Adjoint of the Left Multiplication on a Hermitian Algebra*.

### The Vector Module

For $M = \mathbb{C}^{n}$ with the standard form over $A = M_n(\mathbb{C})$ acting by matrices, $\rho(a)^{*} = \rho(a^{*})$ with $a^{*}$ the conjugate transpose, the induced involution is the entrywise conjugation, and the self-adjoint operators are the Hermitian matrices.

### The Module of a State

For the cyclic module $M = A\cdot\xi$ of a state, $\xi$ is cyclic and separating exactly when the state is faithful, the module Tomita operator is the restriction of the algebra Tomita operator, and $\Delta_M$ is the restriction of $\Delta$; the case of a non-faithful state is excluded by the separatingness of the module's cyclic vector.

## Summary

On a Hermitian module, the **adjoint** of an operator is defined by $(Ts,t) = (s,T^{*}t)$ and obeys the calculus $T^{**} = T$, $(ST)^{*} = T^{*}S^{*}$, $T^{*}T\geq0$; the adjoint of the **action** is the action of the involution, $\rho(x)^{*} = \rho(x^{\dagger})$, which is the self-adjointness of the module form $(x\cdot s,t) = (s,x^{\dagger}\cdot t)$. A **cyclic and separating** vector induces an **involution of the module**, $s^{\dagger} = S_M s$ for $s = x\cdot\xi$ with $S_M(x\cdot\xi) = x^{\dagger}\cdot\xi$; the induced involution is well defined and involutive, satisfies $(x\cdot s)^{\dagger} = s^{\dagger}\cdot x^{\dagger}$, and its polar decomposition produces the **modular operator** and the **modular conjugation** of the module, intertwined with the modular data of the algebra by the action. The **self-adjoint elements** of the module form a real form and give the decomposition $s = s_1+is_2$; the **self-adjoint, positive and unitary** operators of the action kind are exactly those of the algebra, and the adjoint of an **intertwiner** is an intertwiner, so the self-adjoint intertwiners form the self-adjoint part of the commutant of the action. The module axioms are *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint*, the adjoint of the action is *The Adjoint of the One-Sided Action with Hermitian Adjoint*, the algebra case is *The Adjoint of the Left Multiplication on a Hermitian Algebra*, and the modular objects are *The Modular Operator and Tomita-Takesaki Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(Ts,t) = (s,T^{*}t)$ | Hermitian adjoint on the module |
| $\rho(x)^{*} = \rho(x^{\dagger})$ | Adjoint of the action |
| $S_M(x\cdot\xi) = x^{\dagger}\cdot\xi$ | The induced (module Tomita) operator |
| $s^{\dagger} = S_Ms$, $(x\cdot s)^{\dagger} = s^{\dagger}\cdot x^{\dagger}$ | The induced involution |
| $\bar S_M = J_M\Delta_M^{1/2}$ | Polar decomposition of the module involution |
| $s = s_1+is_2$ | Decomposition into self-adjoint elements |
| $T$ self-adjoint, positive, unitary | $T^{*} = T$, $(Ts,s)\geq0$, $T^{*}T = TT^{*} = 1$ |
| $T\rho(x) = \rho(x)T \Rightarrow T^{*}\rho(x) = \rho(x)T^{*}$ | Adjoint of an intertwiner |

## Further Reading

- Jacques Dixmier, *Von Neumann Algebras* (North-Holland, 1981), for Hermitian modules over a Hermitian algebra and the induced involution.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the adjoint of a densely defined module operator and its calculus.
- Serban Stratila and László Zsidó, *Lectures on von Neumann Algebras* (Abacus Press, 1979), for cyclic and separating vectors and the induced Tomita operator.
- Masamichi Takesaki, *Tomita's Theory of Modular Hilbert Algebras and its Applications*, Lecture Notes in Mathematics 128 (Springer, 1970), for the modular data of a module.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for Hermitian forms on modules and the self-adjointness axiom.
