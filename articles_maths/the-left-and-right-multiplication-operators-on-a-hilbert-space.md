# __The Left and Right Multiplication Operators on a Hilbert Space__

## Introduction

A Hilbert space carries bounded operators, and those operators act on one another by composition: for $A\in B(H)$ the left multiplication $L_A$ sends $T$ to $AT$, and the right multiplication $R_B$ sends $T$ to $TB$. In order that these be operators of a Hilbert space in their own right, the space on which they act must be given a Hilbert structure, and the natural one is the Hilbert–Schmidt inner product $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$ on $S_2(H)$. With that structure the multiplications are bounded, their adjoints are the multiplications by the adjoints, and the whole theory is carried by the rank-one operators: every Hilbert–Schmidt operator is a sum of rank-one operators, and on a rank-one operator the two multiplications act by shifting the vectors of the two sides.

This article fixes the two one-sided multiplications, computes their adjoints with respect to the Hilbert–Schmidt form, develops the rank-one decomposition that makes the computation transparent, and identifies the algebra they generate together with its commutant. The algebra $B(H)$ and the Hilbert–Schmidt class are *Bounded Operators on a Hilbert Space* and *Compact Operators*; the multiplication operators of an abstract algebra are *The Left and Right Multiplication Operators on a Banach Algebra* (Part II) and their Hilbert-algebra form is *The Adjoint of the Left Multiplication on a Hilbert Algebra*. The signed versions with a grade involution are *The Signed Left Multiplication on a Hilbert Space* and *The Adjoint of the Left Multiplication on a Hilbert Space* below.

Throughout, $H$ is a Hilbert space over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ with inner product $\langle\cdot,\cdot\rangle$ linear in the first argument, $S_2(H)$ is the Hilbert–Schmidt class with the inner product $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$, and for $\xi,\eta\in H$ the **rank-one operator** is

$$
\xi\otimes\bar\eta:H\longrightarrow H,\qquad (\xi\otimes\bar\eta)(x)=\langle x,\eta\rangle\,\xi .
$$

The left and right multiplications are $L_A(T)=AT$ and $R_B(T)=TB$ on $S_2(H)$, and the adjoint with respect to $\langle\cdot,\cdot\rangle_{\mathrm{HS}}$ is written $L_A^*$, $R_B^*$.

## The One-Sided Multiplications

**Definition.** For $A,B\in B(H)$ the **left multiplication** and the **right multiplication** are

$$
L_A:S_2(H)\longrightarrow S_2(H),\quad L_A(T)=AT,
\qquad
R_B:S_2(H)\longrightarrow S_2(H),\quad R_B(T)=TB .
$$

**Proposition (boundedness and norms).** $L_A$ and $R_B$ are bounded linear operators on $S_2(H)$ with

$$
\|L_A\|=\|A\|,\qquad \|R_B\|=\|B\|,
$$

and the maps $A\mapsto L_A$ and $B\mapsto R_B$ are linear isometries of $B(H)$ into $B(S_2(H))$ that preserve products and the identity:

$$
L_AL_C=L_{AC},\quad R_BR_D=R_{BD},\quad L_I=R_I=I .
$$

*Proof.* For a rank-one $\xi\otimes\bar\eta$ one has $\|\xi\otimes\bar\eta\|_{\mathrm{HS}}=\|\xi\|\|\eta\|$ and $L_A(\xi\otimes\bar\eta)=A\xi\otimes\bar\eta$, $R_B(\xi\otimes\bar\eta)=\xi\otimes\bar{B^*\eta}$; hence $\|L_A(\xi\otimes\bar\eta)\|_{\mathrm{HS}}=\|A\xi\|\|\eta\|\le\|A\|\|\xi\|\|\eta\|=\|A\|\|\xi\otimes\bar\eta\|_{\mathrm{HS}}$. Since the rank-one operators span a dense subspace of $S_2(H)$, $L_A$ extends with norm at most $\|A\|$, and the value $\|A\|$ is attained by choosing $\eta$ and $\xi$ of norm one with $\|A\xi\|=\|A\|$. Products and the identity follow from associativity, and faithfulness from the density of the rank-one operators.

**Proposition (the commutant relation).** The two one-sided families commute:

$$
L_AR_B=R_BL_A\qquad(A,B\in B(H)),
$$

and this is the algebra statement $A(TB)=(AT)B$ read as an identity of operators on $S_2(H)$.

*Proof.* Both sides send $T$ to $ATB$, by associativity of the composition of the operators of $H$.

## Adjoints with Respect to the Hilbert–Schmidt Form

**Theorem (the adjoint of a one-sided multiplication).** For all $A,B\in B(H)$,

$$
L_A^*=L_{A^*},\qquad R_B^*=R_{B^*} .
$$

So the adjoint of a left multiplication is again a left multiplication, the adjoint of a right multiplication is again a right multiplication, and each one-sided family is closed under the adjunction.

*Proof.* Using $\langle L_AT,S\rangle_{\mathrm{HS}}=\operatorname{tr}(ATS^*) = \operatorname{tr}(T S^*A)=\operatorname{tr}(T(A^*S)^*)=\langle T,L_{A^*}S\rangle_{\mathrm{HS}}$, the first identity follows from the uniqueness of the Hilbert adjoint; the second is $\operatorname{tr}(TBS^*)=\operatorname{tr}(T(SB^*)^*)$.

**Corollary (self-adjointness, normality and unitarity of the multiplications).** For $A\in B(H)$:

1. $L_A$ is self-adjoint exactly when $A$ is self-adjoint, and skew-adjoint exactly when $A$ is skew-adjoint;
2. $L_A$ is normal exactly when $A$ is normal;
3. $L_A$ is unitary exactly when $A$ is unitary, and then $L_A^{-1}=L_{A^*}$;
4. $L_A$ is positive exactly when $A$ is positive.

The same four statements hold for $R_B$ with $B$ in place of $A$.

*Proof.* Each is the identity of the theorem read through the isometric representation: $L_A^*=L_{A^*}$ gives $L_A=L_A^*$ iff $A=A^*$ by faithfulness, $L_AL_A^*=L_{AA^*}$ against $L_A^*L_A=L_{A^*A}$ gives normality, unitarity adds $L_{AA^*}=L_{A^*A}=I$, and positivity is $\langle L_AT,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ATT^*)=\operatorname{tr}(T^*AT)\ge0$ exactly when $A$ is positive.

## The Rank-One Decomposition

**Definition.** The **rank-one decomposition** of $S_2(H)$ is the expression of an operator as a norm-convergent sum of rank-one operators $T=\sum_n\xi_n\otimes\bar\eta_n$; the coefficient vectors are the singular vectors of $T$ and the sum is the singular-value expansion.

**Proposition (the multiplications on rank-one operators).** For $\xi,\eta,x\in H$,

$$
L_A(\xi\otimes\bar\eta)=A\xi\otimes\bar\eta,\qquad R_B(\xi\otimes\bar\eta)=\xi\otimes\bar{B^*\eta},\qquad
\xi\otimes\bar\eta = \text{the operator } x\mapsto\langle x,\eta\rangle\xi .
$$

Consequently the left multiplication acts on the first index and the right multiplication acts on the second, and $L_A$ and $R_B$ leave the set of rank-one operators invariant.

*Proof.* $L_A(\xi\otimes\bar\eta)(x)=A(\langle x,\eta\rangle\xi)=\langle x,\eta\rangle A\xi$, which is $A\xi\otimes\bar\eta$; $R_B(\xi\otimes\bar\eta)(x)=B(\langle x,\eta\rangle\xi)=\langle x,\eta\rangle B\xi$, and one computes $\langle x,\eta\rangle B\xi=\langle x,B^*\eta\rangle\xi$, so the second factor receives $B^*$.

**Theorem (the span and the inner product).** The rank-one operators span a dense subspace of $S_2(H)$, and the Hilbert–Schmidt inner product of two of them is

$$
\langle \xi\otimes\bar\eta,\ \xi'\otimes\bar\eta'\rangle_{\mathrm{HS}}=\langle \xi,\xi'\rangle\,\langle\eta',\eta\rangle .
$$

Hence every $T\in S_2(H)$ has a norm-convergent expansion $T=\sum_n s_n\,\xi_n\otimes\bar\eta_n$ with orthonormal families $(\xi_n)$, $(\eta_n)$ and singular values $s_n$, and the multiplications act termwise on the expansion.

*Proof.* The pairings follow from $(\xi\otimes\bar\eta)(\xi'\otimes\bar\eta')^*=\xi\otimes\bar\eta\circ\eta'\otimes\bar\xi'$, whose trace is $\langle\xi,\xi'\rangle\langle\eta',\eta\rangle$; the expansion is the singular-value decomposition of the compact operator $T$ recalled from *Compact Operators*, and the density of the span is the density of the finite-rank operators in $S_2$.

## The Generated Algebra and Its Commutant

**Definition.** The **multiplication algebra** of $H$ is the algebra generated in $B(S_2(H))$ by the left and right multiplications:

$$
\mathcal{M}(H)=\Bigl\{\sum_i L_{A_i}R_{B_i}:A_i,B_i\in B(H),\ \text{finite sums}\Bigr\},
\qquad \sum_iL_{A_i}R_{B_i}(T)=\sum_iA_iTB_i.
$$

**Proposition (the algebras generated by the two sides).** The algebra generated by the left multiplications alone is $\{L_A:A\in B(H)\}\cong B(H)$, the algebra generated by the right multiplications alone is $\{R_B:B\in B(H)\}\cong B(H)$, and

$$
\mathcal{M}(H)=\{L_A:A\in B(H)\}'=\{R_B:B\in B(H)\}',
$$

so the multiplication algebra is the commutant of each one-sided family. In finite dimension $H=\mathbb{K}^n$ the multiplication algebra is all of $B(M_n(\mathbb{K}))$.

*Proof.* A multiplication $\sum_iL_{A_i}R_{B_i}$ commutes with every $L_C$, and conversely an operator on $S_2(H)$ commuting with every left multiplication is a right multiplication in the following sense: it is determined by its value on a single rank-one operator and is the sum of finitely many two-sided multiplications. In finite dimension $n$ one has $\dim B(M_n)=n^4=\dim(M_n\otimes M_n^{\mathrm{op}})$, and the identification is an isomorphism, so the multiplication algebra is everything.

**Example (finite dimension).** For $H=\mathbb{K}^n$ identify $S_2(H)$ with $M_n(\mathbb{K})$ and the Hilbert–Schmidt form with $\langle S,T\rangle=\operatorname{tr}(ST^*)$. Then $L_A$ is the operator $T\mapsto AT$ and $R_B$ is $T\mapsto TB$, the left multiplications are the matrices $A\otimes I$ under the identification $M_n\cong\mathbb{K}^n\otimes\mathbb{K}^n$, the right multiplications are $I\otimes B^{\mathrm t}$, and the multiplications satisfy $L_A^*=L_{A^*}$, $R_B^*=R_{B^*}$ with the conjugate transpose.

**Example (diagonal operators).** For $H=\ell^2$ and $A=B=D_a$ diagonal with $a\in\ell^\infty$, the operator $L_{D_a}R_{D_a}$ acts on the matrix units $e_m\otimes\bar e_n$ by $e_m\otimes\bar e_n\mapsto a_ma_n\,e_m\otimes\bar e_n$, so the two-sided multiplication by a single diagonal element is diagonal in the matrix-unit basis with the product symbol; the same computation with $a\in c_0$ restricts to the compact operators and exhibits the multiplication algebra of the compact ideal.

## Summary

On the Hilbert–Schmidt space $S_2(H)$ of a Hilbert space the bounded operators of $H$ act by the left multiplication $L_A(T)=AT$ and the right multiplication $R_B(T)=TB$, both bounded with $\|L_A\|=\|A\|$ and $\|R_B\|=\|B\|$, and the two representations $A\mapsto L_A$, $B\mapsto R_B$ are isometric and multiplicative. The adjoints are $L_A^*=L_{A^*}$ and $R_B^*=R_{B^*}$, so each one-sided family is self-adjoint, and self-adjointness, normality, unitarity and positivity of a multiplication are exactly the corresponding properties of the element. The two families commute, and they act on the rank-one operators $\xi\otimes\bar\eta$ by shifting the two vectors, $L_A(\xi\otimes\bar\eta)=A\xi\otimes\bar\eta$ and $R_B(\xi\otimes\bar\eta)=\xi\otimes\bar{B^*\eta}$; since the rank-one operators span $S_2(H)$ densely, this decomposes every Hilbert–Schmidt operator into a singular-value expansion and reduces every computation to the rank-one case. The algebra generated by both families is the multiplication algebra $\mathcal{M}(H)$, the commutant of each one-sided family, equal to all of $B(S_2(H))$ in finite dimension.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_2(H)$ | Hilbert–Schmidt class with $\langle S,T\rangle_{\mathrm{HS}}=\operatorname{tr}(ST^*)$ |
| $L_A(T)=AT$ | left multiplication by $A$ |
| $R_B(T)=TB$ | right multiplication by $B$ |
| $\|L_A\|=\|A\|$, $\|R_B\|=\|B\|$ | isometric representations |
| $L_A^*=L_{A^*}$, $R_B^*=R_{B^*}$ | adjoints for the Hilbert–Schmidt form |
| $L_AR_B=R_BL_A$ | the two sides commute |
| $\xi\otimes\bar\eta$ | rank-one operator, $x\mapsto\langle x,\eta\rangle\xi$ |
| $L_A(\xi\otimes\bar\eta)=A\xi\otimes\bar\eta$ | action on the first index |
| $R_B(\xi\otimes\bar\eta)=\xi\otimes\bar{B^*\eta}$ | action on the second index |
| $\mathcal{M}(H)$ | multiplication algebra, the commutant of each one-sided family |

## Further Reading

- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part II* (Interscience, 1963), for the multiplication operators and the Hilbert–Schmidt structure on $B(H)$.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the left and right multiplications and the commutant relations.
- Barry Simon, *Trace Ideals and Their Applications*, Mathematical Surveys and Monographs 120 (American Mathematical Society, 2nd ed. 2005), for the rank-one decomposition and the Hilbert–Schmidt inner product.
- Frigyes Riesz and Béla Sz.-Nagy, *Functional Analysis* (Dover, 1990), for the multiplication operators of a Hilbert space and the elementary operators.
- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 2nd ed. 1982), for the two-sided multiplications and their commutants.
