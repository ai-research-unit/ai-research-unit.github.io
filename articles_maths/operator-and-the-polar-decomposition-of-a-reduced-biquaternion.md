# __Operator and the Polar Decomposition of a Reduced Biquaternion__

## Introduction

The **multiplication operator** of a reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is

$$
M_{\breve Q}:\mathbb{B}_{\mathrm{r}}\longrightarrow\mathbb{B}_{\mathrm{r}},\qquad M_{\breve Q}(\breve X)=\breve Q\breve X.
$$

The algebra $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ is commutative, so the left and the right multiplications coincide,

$$
L_{\breve Q}=R_{\breve Q}=M_{\breve Q}.
$$

There is one one-sided operator, not two. The **two-sided operator** is the sandwich

$$
\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q},
$$

where the bar is the coefficient conjugation, $i\mapsto-i$ and $j\mapsto j$.

The polar decomposition writes

$$
\breve Q=\breve r\,u
=\rho\bigl(\cosh\phi+j\sinh\phi\bigr)\exp(i\alpha)\exp(ij\beta),
\qquad \breve r=\rho e^{\phi j}\in P,\quad u=e^{i\alpha}e^{ij\beta}\in T^2,
$$

with $\rho>0$, $\phi\in\mathbb{R}$ and $(\alpha,\beta)\in\mathbb{R}^2/2\pi\mathbb{Z}^2$. The operator inherits the word,

$$
M_{\breve Q}=\rho\,M_{e^{\phi j}}\,M_{e^{i\alpha}}\,M_{e^{ij\beta}},
$$

and in the eigenbasis $(\Pi_+,\Pi_-)$ of the idempotents $\Pi_\pm=\tfrac12(1\pm j)$ it is diagonal:

$$
M_{\breve Q}=\operatorname{diag}(\lambda_+,\lambda_-),
\qquad
\lambda_\pm=Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}
=\rho e^{\pm\phi}e^{i(\alpha\pm\beta)}.
$$

The one-sided operator carries all four parameters: the scale $\rho$, the boost $\phi$, and the two phases $\alpha,\beta$. The two-sided operator is

$$
\Theta_{\breve Q}=M_{\breve Q\bar{\breve Q}}=M_{\breve r^2},
\qquad
\breve r^2=\rho^2 e^{2\phi j},
$$

so in the eigenbasis it is

$$
\Theta_{\breve Q}=\operatorname{diag}\bigl(\rho^2e^{2\phi},\,\rho^2e^{-2\phi}\bigr)
=\operatorname{diag}\bigl(\lvert Q_+\rvert^2,\lvert Q_-\rvert^2\bigr).
$$

The scale squares, the boost doubles, and both phases cancel.

The results are four. The map $\breve Q\mapsto M_{\breve Q}$ is a faithful representation of $\mathbb{B}_{\mathrm{r}}$ on itself. The spectrum is $\{Q_+,Q_-\}$, and the eigenbasis is the fixed idempotent basis. The one-sided operator carries the full boost $\phi$ and the full phases $\alpha,\beta$: its eigenvalues are $e^{\pm\phi}e^{i(\alpha\pm\beta)}$, with no half-angle. The two-sided operator is again a one-sided operator, the multiplication by the modulus squared $\breve r^2$; it is the inner automorphism multiplied by the modulus squared, the inner automorphism is trivial because the algebra is commutative, and the operator doubles the boost while cancelling the phases.

The contrast with the biquaternion is the contrast between a commutative and a non-commutative algebra. In $\mathbb{B}$ the one-sided operator is the spinor action with the half-angle, and the sandwich is the vector action with the full angle. In $\mathbb{B}_{\mathrm{r}}$ the one-sided operator is the regular representation with the full parameters, and the sandwich is the modulus squared. The half-angle is not a feature of the polar decomposition alone.

| Question | Answer |
|---|---|
| Algebra | $\mathbb{B}_{\mathrm{r}}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$ |
| Element | $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ |
| One-sided operator | $M_{\breve Q}(\breve X)=\breve Q\breve X$, with $L=R=M$ |
| Two-sided operator | $\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q}=\breve r^2\breve X$ |
| Spectrum of $M_{\breve Q}$ | $\{\lambda_+,\lambda_-\}=\{Q_+,Q_-\}$ |
| Eigenbasis | $(\Pi_+,\Pi_-)$, fixed and independent of $\breve Q$ |
| Polar word | $\breve Q=\rho e^{\phi j}e^{i\alpha}e^{ij\beta}$ |
| One-sided exponents | $\phi$, $\alpha+\beta$, $\alpha-\beta$ |
| Two-sided exponents | $2\phi$, $0$, $0$ |
| Half-angle | none |
| Nilpotents | none |

## Conventions

The algebra is $\mathbb{B}_{\mathrm{r}}=\mathbb{C}[j]/(j^2-1)$, with basis $1,i,j,ij$ over $\mathbb{R}$ and basis $1,j$ over $\mathbb{C}$, and with

$$
i^2=-1,\qquad j^2=+1,\qquad ij=ji.
$$

A general element is

$$
\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown},
\qquad Q_{\blacktriangle},Q_{\blacktriangledown}\in\mathbb{C}.
$$

The idempotents are

$$
\Pi_+=\frac{1+j}{2},\qquad \Pi_-=\frac{1-j}{2},
\qquad
\Pi_+^2=\Pi_+,\quad \Pi_-^2=\Pi_-,\quad \Pi_+\Pi_-=0,\quad \Pi_++\Pi_-=1.
$$

The idempotent coordinates are

$$
Q_+=Q_{\blacktriangle}+Q_{\blacktriangledown},\qquad Q_-=Q_{\blacktriangle}-Q_{\blacktriangledown},
\qquad
\breve Q=Q_+\Pi_++Q_-\Pi_-.
$$

The eigenvalues are written $\lambda_\pm=Q_\pm$, as in *Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion*. The bar is the coefficient conjugation

$$
\overline{Q_{\blacktriangle}+jQ_{\blacktriangledown}}
=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}.
$$

The modulus and the unit factor are those of *Modulus–Unit Polar Decomposition of Reduced Biquaternions*:

$$
\breve Q=\breve r\,u,
\qquad
\breve r\in P=\{\,x+jy:x>\lvert y\rvert\,\},
\qquad
u\in T^2=\{\,u:u\bar u=1\,\},
$$

and in exponential coordinates

$$
\breve r=\rho e^{\phi j}=\rho(\cosh\phi+j\sinh\phi),
\qquad
u=e^{i\alpha}e^{ij\beta}.
$$

The **reduced norm** is

$$
\langle\breve Q\rangle_{\mathrm{ts}}
=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2=Q_+Q_-,
$$

complex-valued and multiplicative. The modulus is the coefficient norm

$$
\breve Q\bar{\breve Q}=\lvert Q_+\rvert^2\Pi_++\lvert Q_-\rvert^2\Pi_-=\breve r^2,
$$

which is the positive-cone element used by the polar decomposition.

The operator is written $M_{\breve Q}$ because there is only one side; the letters $L$ and $R$ are reserved for the biquaternion comparison. The two-sided operator is $\Theta_{\breve Q}$. The complex bilinear form is

$$
G=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

## The Multiplication Operator

### Definition and Laws

**Definition.** For $\breve Q\in\mathbb{B}_{\mathrm{r}}$ the multiplication operator is $M_{\breve Q}(\breve X)=\breve Q\breve X$.

**Proposition (the representation).** The map $M:\breve Q\mapsto M_{\breve Q}$ is $\mathbb{C}$-linear and multiplicative,

$$
M_{\breve Q+\breve P}=M_{\breve Q}+M_{\breve P},
\qquad
M_{\breve Q\breve P}=M_{\breve Q}\circ M_{\breve P},
\qquad
M_1=\operatorname{id},
$$

and faithful: $M_{\breve Q}(1)=\breve Q$, so $M_{\breve Q}=0$ exactly when $\breve Q=0$. The image is the commutative algebra of complex matrices

$$
\left\{\begin{pmatrix}A&B\\B&A\end{pmatrix}:A,B\in\mathbb{C}\right\},
$$

which is isomorphic to $\mathbb{B}_{\mathrm{r}}$.

*Proof.* The laws are the associativity and the distributivity of the algebra. Faithfulness is evaluation at $1$. The matrix is computed on the basis: $\breve Q\cdot1=A+jB$ and $\breve Q\cdot j=B+jA$, hence the two columns $(A,B)$ and $(B,A)$.

**Corollary (invertibility).** $M_{\breve Q}$ is invertible exactly when $\breve Q$ is a unit, that is, exactly when both $Q_+$ and $Q_-$ are nonzero, equivalently when the reduced norm $Q_+Q_-$ is nonzero. The inverse is $M_{\breve Q^{-1}}$.

**Proposition (commutation).** For all $\breve Q,\breve P$,

$$
M_{\breve Q}M_{\breve P}=M_{\breve P}M_{\breve Q}=M_{\breve Q\breve P}.
$$

The operator algebra is commutative; it is the regular representation of $\mathbb{B}_{\mathrm{r}}$.

**Proposition (the complex bilinear form).** With $G=\operatorname{diag}(1,-1)$,

$$
M_{\breve Q}^{T}GM_{\breve Q}=\langle\breve Q\rangle_{\mathrm{ts}}\,G.
$$

*Proof.* Direct computation:

$$
\begin{pmatrix}A&B\\B&A\end{pmatrix}
\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\begin{pmatrix}A&B\\B&A\end{pmatrix}
=
\begin{pmatrix}A^2-B^2&0\\0&B^2-A^2\end{pmatrix}
=(A^2-B^2)G.
$$

Thus $M_{\breve Q}$ is conformal for the complex bilinear form $G$, with conformal factor the reduced norm $Q_+Q_-$. The form is complex bilinear, not Hermitian; the coefficient conjugation gives the modulus $\breve r^2$, not this form.

### The Two Matrices

In the basis $(1,j)$ the matrix is

$$
M_{\breve Q}=\begin{pmatrix}A&B\\B&A\end{pmatrix},
\qquad A=Q_{\blacktriangle},\quad B=Q_{\blacktriangledown}.
$$

In the eigenbasis $(\Pi_+,\Pi_-)$ it is

$$
M_{\breve Q}=\operatorname{diag}(Q_+,Q_-).
$$

The change of basis is

$$
P=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^{-1}=2P,
\qquad
P^{-1}M_{\breve Q}P=\operatorname{diag}(Q_+,Q_-).
$$

The characteristic polynomial is

$$
p_{\breve Q}(X)=X^2-2AX+(A^2-B^2)=(X-Q_+)(X-Q_-),
$$

with trace $2A$ and determinant $Q_+Q_-$. The discriminant is $4B^2$, so the eigenvalues are distinct exactly when $Q_{\blacktriangledown}=B\neq0$.

### The Spectrum and the Eigenbasis

**Theorem.** The spectrum of $M_{\breve Q}$ is $\{Q_+,Q_-\}$. The eigenspaces are the two minimal ideals

$$
S_+=\mathbb{C}\Pi_+,\qquad S_-=\mathbb{C}\Pi_-,
\qquad
\mathbb{B}_{\mathrm{r}}=S_+\oplus S_-.
$$

*Proof.* In the eigenbasis the matrix is diagonal with entries $Q_\pm$, and $\Pi_\pm$ are the corresponding idempotents: $\breve Q\Pi_\pm=Q_\pm\Pi_\pm$.

The eigenbasis is **fixed**: it is the standard idempotent pair, independent of $\breve Q$. This is the commutative simplification. In the biquaternion the eigenbasis is attached to $\tilde Q$, built from the nilpotents and depending on the element; here the idempotents are the only nontrivial ones, the Peirce corners are zero, and there are no nilpotents.

The eigenvalues are the two complex idempotent coordinates. Their sum is $2A$ and their product is the reduced norm. When $Q_{\blacktriangledown}=0$ the element is the complex scalar $A$, the two eigenvalues coincide, and $M_{\breve Q}=A\operatorname{id}$.

### Kernel and Image

**Proposition.** Let $\breve Q\in\mathbb{B}_{\mathrm{r}}$.

**(a)** If $Q_+Q_-\neq0$, then $M_{\breve Q}$ is bijective.

**(b)** If $Q_+=0$ and $Q_-\neq0$, then $M_{\breve Q}=Q_-\Pi_-$ has rank one, image $S_-$ and kernel $S_+$.

**(c)** If $Q_-=0$ and $Q_+\neq0$, then $M_{\breve Q}=Q_+\Pi_+$ has rank one, image $S_+$ and kernel $S_-$.

**(d)** If $\breve Q=0$, then $M_{\breve Q}=0$.

*Proof.* (a) is the invertibility corollary. For (b), $Q_+=0$ gives $\breve Q=Q_-\Pi_-$; multiplication by $\Pi_-$ is the projection onto $S_-$ along $S_+$. The case (c) is symmetric. (d) is immediate.

The image is the principal ideal $\breve Q\mathbb{B}_{\mathrm{r}}$; the kernel is the annihilator

$$
\operatorname{Ann}(\breve Q)=\{\breve X:\breve Q\breve X=0\}.
$$

The complex rank is $2$, $1$ or $0$.

## The Polar Word, One-Sided

### The Factorisation of the Operator

The polar word $\breve Q=\rho e^{\phi j}e^{i\alpha}e^{ij\beta}$ gives

$$
M_{\breve Q}=\rho\,M_{e^{\phi j}}\,M_{e^{i\alpha}}\,M_{e^{ij\beta}}.
$$

The factors commute. In the eigenbasis,

$$
M_{e^{\phi j}}=\operatorname{diag}(e^{\phi},e^{-\phi}),
\qquad
M_{e^{i\alpha}}=e^{i\alpha}\operatorname{id},
\qquad
M_{e^{ij\beta}}=\operatorname{diag}(e^{i\beta},e^{-i\beta}),
$$

so

$$
M_{\breve Q}=\operatorname{diag}\bigl(\rho e^{\phi}e^{i(\alpha+\beta)},\,
\rho e^{-\phi}e^{i(\alpha-\beta)}\bigr)
=\operatorname{diag}(Q_+,Q_-).
$$

The four factors have distinct roles. The scale $\rho$ acts as $\rho$, not $\rho^2$. The boost $\phi$ acts as $e^{\pm\phi}$. The central phase $e^{i\alpha}$ acts as the same scalar $e^{i\alpha}$ on both ideals. The phase $e^{ij\beta}$ acts as $e^{\pm i\beta}$, with opposite signs on the two ideals.

### The Exponents and the Absence of a Half-Angle

On $S_+$ the exponent is

$$
\phi+i\alpha+i\beta=\phi+i(\alpha+\beta),
$$

and on $S_-$ it is

$$
-\phi+i\alpha-i\beta=-\phi+i(\alpha-\beta).
$$

The eigenvalues are the exponentials of these expressions. The boost exponent is $\phi$, the full hyperbolic angle. The phase exponents are $\alpha+\beta$ and $\alpha-\beta$, the full phases. There is no half of $\phi$, $\alpha$ or $\beta$.

A half-angle would require a square root of $\breve Q$, or a module on which $j$ acts by $\pm\tfrac12$. Neither is part of the polar decomposition. On the minimal ideals,

$$
j\Pi_+=\Pi_+,\qquad j\Pi_-=-\Pi_-,
$$

so $j$ acts by $\pm1$, and $\exp(\phi j)$ acts by $e^{\pm\phi}$. If $\breve Q=\breve S^2$, then $M_{\breve Q}=(M_{\breve S})^{2}$, and the eigenvalues of $M_{\breve S}$ are square roots of those of $M_{\breve Q}$; but $\breve S$ is not the polar factor, and the polar decomposition does not take this square root.

The map $\breve Q\mapsto M_{\breve Q}$ is faithful, so there is no sign ambiguity: $\breve Q$ and $-\breve Q$ give different operators. The group of units is

$$
\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times},
$$

whose universal cover is $\mathbb{C}^2$, an infinite cover, not a double cover. The phases are periodic with period $2\pi$, but that is the period of the exponential, not a spin half-angle. No double cover is used.

### The Spinor Reading

The minimal left ideals $S_\pm=\mathbb{C}\Pi_\pm$ are one-dimensional over $\mathbb{C}$. A spinor is a single complex coordinate on one ideal:

$$
\xi_+=\alpha\Pi_+,\qquad \xi_-=\beta\Pi_-,
\qquad \alpha,\beta\in\mathbb{C}.
$$

The operator acts by

$$
M_{\breve Q}\xi_+=Q_+\xi_+,\qquad M_{\breve Q}\xi_-=Q_-\xi_-,
$$

and never mixes the two ideals. The word spinor is algebraic: an element of a minimal left ideal. The weights of $S_\pm$ are the full exponents $\pm\phi+i(\alpha\pm\beta)$; there is no half-angle. The two ideals are the two Peirce components, not the two Lorentz chiralities.

### The Matrix Picture

In the basis $(1,j)$ the four factors are

$$
M_{e^{\phi j}}=\begin{pmatrix}\cosh\phi&\sinh\phi\\\sinh\phi&\cosh\phi\end{pmatrix},
\qquad
M_{e^{i\alpha}}=\begin{pmatrix}e^{i\alpha}&0\\0&e^{i\alpha}\end{pmatrix},
\qquad
M_{e^{ij\beta}}=\begin{pmatrix}\cos\beta&i\sin\beta\\i\sin\beta&\cos\beta\end{pmatrix}.
$$

The product is

$$
M_{\breve Q}=\begin{pmatrix}A&B\\B&A\end{pmatrix},
\qquad
A=\rho e^{i\alpha}\bigl(\cosh\phi\cos\beta+i\sinh\phi\sin\beta\bigr),
$$

$$
B=\rho e^{i\alpha}\bigl(i\cosh\phi\sin\beta+\sinh\phi\cos\beta\bigr).
$$

The determinant is the reduced norm,

$$
\det M_{\breve Q}=A^2-B^2=Q_+Q_-=\rho^2e^{2i\alpha},
$$

and the two-sided operator has determinant

$$
\det\Theta_{\breve Q}=\rho^4=\lvert\det M_{\breve Q}\rvert^2.
$$

The phases $\alpha$ and $\beta$ are visible to the one-sided operator and invisible to the two-sided one.

## The Two-Sided Operator

### The Collapse to the Modulus Squared

**Theorem.** For every $\breve Q$,

$$
\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q}=\breve Q\bar{\breve Q}\,\breve X=\breve r^2\breve X.
$$

*Proof.* The algebra is commutative and $\breve Q\bar{\breve Q}=\breve r^2$ is central. Hence $\breve Q\breve X\bar{\breve Q}=\breve Q\bar{\breve Q}\,\breve X$.

In the eigenbasis,

$$
\breve r^2=\lvert Q_+\rvert^2\Pi_++\lvert Q_-\rvert^2\Pi_-,
\qquad
\Theta_{\breve Q}=\operatorname{diag}\bigl(\lvert Q_+\rvert^2,\lvert Q_-\rvert^2\bigr).
$$

The two-sided operator is again a one-sided operator, the multiplication by the cone element $\breve r^2$. It is multiplicative,

$$
\Theta_{\breve Q}\circ\Theta_{\breve P}=\Theta_{\breve Q\breve P},
$$

but it is not faithful: $\Theta_{\breve Q}=\Theta_{\breve P}$ exactly when $\breve Q\bar{\breve Q}=\breve P\bar{\breve P}$.

On the units the operator is the inner automorphism multiplied by the modulus squared. For a unit, $\bar{\breve Q}=\breve r^2\breve Q^{-1}$, so

$$
\Theta_{\breve Q}=\breve r^2\,\operatorname{Ad}_{\breve Q}.
$$

The inner automorphism $\operatorname{Ad}_{\breve Q}$ of a commutative algebra is the identity, hence

$$
\Theta_{\breve Q}=\breve r^2\operatorname{id}.
$$

This is the structural reason for the collapse: the sandwich is a conjugation, and there is nothing to conjugate.

### The Polar Reading

Write $\breve Q=\rho e^{\phi j}u$ with $u=e^{i\alpha}e^{ij\beta}\in T^2$. Then

$$
\Theta_{\breve Q}=\breve r^2\operatorname{id}=\rho^2e^{2\phi j}\operatorname{id}.
$$

The scale is squared, $\rho\mapsto\rho^2$. The boost is doubled, $\phi\mapsto2\phi$. Both phases cancel, $\alpha\mapsto0$ and $\beta\mapsto0$, because $u\bar u=1$.

The sandwich is blind to the unit torus. Every element on the same torus coset $\breve rT^2$ has the same two-sided operator. The fibre of $\Theta$ over $\breve r^2$ is the torus $\breve rT^2$.

### The Image and the Kernel

On the group of units $\mathbb{B}_{\mathrm{r}}^{\times}$ the map $\breve Q\mapsto\Theta_{\breve Q}$ has image the positive cone

$$
P=\{\,x+jy:x>\lvert y\rvert\,\},
$$

and kernel the unit torus

$$
T^2=\{\,u:u\bar u=1\,\}.
$$

The image is two-dimensional and the kernel is two-dimensional; the domain is four-dimensional, and the quotient is the cone. On the unit torus itself the sandwich is the identity:

$$
\Theta_u=\operatorname{id}\qquad(u\in T^2).
$$

The image is not a Lorentz group. It is the positive cone of the split-complex plane, the set of modulus squares. The two-sided operator has lost both phases, which are the compact part of the unit group.

### The Two-Sided Family

Every two-sided operator of the form $L_{\breve A}R_{\breve B}$ is a one-sided operator:

$$
L_{\breve A}R_{\breve B}=M_{\breve A\breve B}.
$$

The family is the algebra itself, and the sandwich is the case $\breve B=\bar{\breve A}$. The commutator vanishes,

$$
[L_{\breve A},R_{\breve B}]=0,
$$

and every derivation is zero:

$$
\operatorname{ad}_{\breve Q}(\breve X)=\breve Q\breve X-\breve X\breve Q=0.
$$

Consequently the inner automorphism $\operatorname{Ad}_{\breve Q}=L_{\breve Q}R_{\breve Q^{-1}}$ is the identity for every unit $\breve Q$. The only nontrivial action is left multiplication, the regular representation. The two-sided operator is not a new object in a commutative algebra; it is a one-sided operator with the product of the two parameters.

## The Two Involutions and the Two Sandwiches

The algebra carries two natural involutions, and each gives a two-sided operator.

### The Coefficient Conjugation

The **coefficient conjugation** is the bar,

$$
\overline{Q_{\blacktriangle}+jQ_{\blacktriangledown}}
=\bar Q_{\blacktriangle}+j\bar Q_{\blacktriangledown}.
$$

It fixes $j$ and negates $i$. It is the involution of the polar decomposition. Its sandwich is

$$
\Theta^{\mathrm{c}}_{\breve Q}(\breve X)
=\breve Q\breve X\bar{\breve Q}
=\breve r^2\breve X,
$$

with

$$
\breve r^2=\rho^2e^{2\phi j}
=\rho^2(\cosh 2\phi+j\sinh 2\phi).
$$

The scale squares, the boost doubles, and the two phases cancel. In coordinates,

$$
\Theta^{\mathrm{c}}_{\breve Q}
=\operatorname{diag}\bigl(\rho^2e^{2\phi},\rho^2e^{-2\phi}\bigr).
$$

### The Elementary Conjugation

The **elementary conjugation** is

$$
\eta(Q_{\blacktriangle}+jQ_{\blacktriangledown})
=Q_{\blacktriangle}-jQ_{\blacktriangledown}.
$$

It fixes $i$ and negates $j$. Its sandwich is

$$
\Theta^{\mathrm{e}}_{\breve Q}(\breve X)
=\breve Q\breve X\eta(\breve Q)
=\breve Q\eta(\breve Q)\breve X.
$$

Now

$$
\breve Q\eta(\breve Q)
=Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2
=Q_+Q_-
=\rho^2e^{2i\alpha},
$$

a complex scalar. Hence

$$
\Theta^{\mathrm{e}}_{\breve Q}
=Q_+Q_-\,\operatorname{id}
=\rho^2e^{2i\alpha}\operatorname{id}.
$$

This sandwich is scalar over $\mathbb{C}$. It doubles the phase $\alpha$, cancels the phase $\beta$, and cancels the boost $\phi$.

### The Two Collapses

The two sandwiches are the two extreme collapses of the four parameters.

| Sandwich | Scale | Boost | Phase $\alpha$ | Phase $\beta$ |
|---|---|---|---|---|
| $\Theta^{\mathrm{c}}$, polar | $\rho^2$ | $2\phi$ | $0$ | $0$ |
| $\Theta^{\mathrm{e}}$, elementary | $\rho^2$ | $0$ | $2\alpha$ | $0$ |

The polar sandwich keeps the modulus and loses the torus. The elementary sandwich keeps the scale and one phase, and loses the boost and the other phase. The polar decomposition uses the bar; the elementary sandwich is the reduced-norm analogue of the split-complex scalar sandwich.

In the split-complex algebra there is only one conjugation, so there is only one sandwich. In the reduced biquaternion the two involutions separate the two real forms: the bar fixes the split-complex plane $\mathbb{R}\{1,j\}$ and $\eta$ fixes the complex plane $\mathbb{C}\{1,i\}$.

## The Null Cone and the Degenerate Cases

The zero divisors are the elements with $Q_+Q_-=0$, that is, the two complex lines $Q_{\blacktriangle}=\pm Q_{\blacktriangledown}$. They are the null cone of the reduced norm.

**Proposition.** Let $\breve Q\neq0$ be a zero divisor.

**(a)** $M_{\breve Q}$ has complex rank one. If $Q_+=0$, the image is $S_-$ and the kernel is $S_+$; if $Q_-=0$, the roles are exchanged.

**(b)** There is no polar decomposition of $\breve Q$: the modulus $\breve r$ is not in the cone $P$.

**(c)** $\Theta^{\mathrm{c}}_{\breve Q}=0$.

*Proof.* (a) is the kernel and image proposition. (b) is the definition of the modulus. (c) is $\breve r^2=0$.

The scalar case $Q_{\blacktriangledown}=0$ is the other degeneration. Then $\breve Q=A$ is a nonzero complex scalar, $M_{\breve Q}=A\operatorname{id}$, the two eigenvalues coincide, and the polar parameters are $\phi=0$ and $\beta=0$, with $\rho=\lvert A\rvert$ and $\alpha=\arg A$.

There are no nilpotents. The algebra is $\mathbb{B}_{\mathrm{r}}\cong\mathbb{C}\times\mathbb{C}$, which is reduced: every element is semisimple, the minimal polynomial is squarefree, and $M_{\breve Q}$ is diagonalizable for every $\breve Q$. There is no Jordan block and no nilpotent regime. The nilpotent construction of the biquaternion, with the two elements $\vec\Upsilon_\pm$ of square zero, has no analogue here: the Peirce corners of the fixed idempotents are zero.

## Comparison with the Biquaternion and Split-Complex Cases

| Item | Biquaternion $\mathbb{B}$ | Split-complex $\mathbb{D}$ | Reduced $\mathbb{B}_{\mathrm{r}}$ |
|---|---|---|---|
| Commutative | no | yes | yes |
| One-sided operators | $L_{\tilde Q}\neq R_{\tilde Q}$ | $L_Q=R_Q=M_Q$ | $L=R=M$ |
| Spectrum of the one-sided operator | $\lambda_\pm=Q_t\pm iB$, each twice | $\lambda_\pm=q\pm q'$ | $\lambda_\pm=Q_\pm$ |
| Eigenbasis | eigenbasis attached to $\tilde Q$ | fixed $(\Pi_+,\Pi_-)$ | fixed $(\Pi_+,\Pi_-)$ |
| One-sided exponents | $\theta/2$, $\psi/2$ | $\phi$ | $\phi$, $\alpha+\beta$, $\alpha-\beta$ |
| Two-sided operator | $\tilde Q\tilde X\tilde Q^{*}$, non-scalar | $\langle Q\rangle_{*}X$, scalar | $\breve r^2X$, cone element |
| Two-sided exponents | $\theta$, $\psi$ | $0$ | $2\phi$, $0$, $0$ |
| Image on the units | $CO^{+}(1,3)$ | $\mathbb{R}^{\times}I$ | $P$ |
| Kernel on the units | $U(1)$ | $\{N=1\}$ | $T^2$ |
| Nilpotents | yes, when $B\neq0$ | none | none |
| Half-angle | yes | no | no |

The table records the same reversal as in the split-complex case. In the biquaternion the one-sided operator is the spinor action, which carries half the angle, and the sandwich is the vector action, which carries the full angle. In the reduced biquaternion the one-sided operator is the regular representation, which carries the full parameters, and the sandwich is the modulus squared, which doubles the boost and kills the phases.

The reason is the commutativity. The biquaternion is the tensor product $S\otimes S^{*}$ of a spinor space and its dual; the left multiplication acts on one factor, the right multiplication on the other, and the sandwich acts on the pair. The reduced biquaternion is commutative; its regular representation is the direct sum of the two characters $S_\pm$, and the sandwich is, up to the modulus squared, the inner automorphism, which is trivial. The half-angle belongs to the non-commutative spinor factor, not to the polar word alone.

## Summary

The multiplication operator $M_{\breve Q}(\breve X)=\breve Q\breve X$ is a faithful representation of $\mathbb{B}_{\mathrm{r}}$ on itself. In the fixed eigenbasis $(\Pi_+,\Pi_-)$ it is diagonal with eigenvalues $Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$.

The polar word $\breve Q=\rho e^{\phi j}e^{i\alpha}e^{ij\beta}$ reads

$$
M_{\breve Q}=\operatorname{diag}\bigl(\rho e^{\phi}e^{i(\alpha+\beta)},\rho e^{-\phi}e^{i(\alpha-\beta)}\bigr).
$$

The scale acts as $\rho$, the boost as $e^{\pm\phi}$, and the phases as $e^{i(\alpha\pm\beta)}$. All exponents are full; there is no half-angle.

The two-sided operator is

$$
\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q}=\breve r^2\breve X,
$$

with

$$
\Theta_{\breve Q}=\operatorname{diag}\bigl(\rho^2e^{2\phi},\rho^2e^{-2\phi}\bigr).
$$

The scale squares, the boost doubles, and both phases cancel. The operator is the inner automorphism multiplied by the modulus squared; the inner automorphism of a commutative algebra is the identity. On the units the image is the positive cone $P$ and the kernel is the unit torus $T^2$.

The zero divisors give rank one. There are no nilpotents and no Jordan blocks: the algebra is reduced. The half-angle, the spin double cover and the eigenbasis attached to the biquaternion element have no analogue.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}_{\mathrm{r}}$ | the reduced biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}$ |
| $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ | a reduced biquaternion |
| $Q_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | the idempotent coordinates, the eigenvalues |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents |
| $\bar{\breve Q}$ | the coefficient conjugation, $i\mapsto-i$, $j\mapsto j$ |
| $\eta(\breve Q)=Q_{\blacktriangle}-jQ_{\blacktriangledown}$ | the elementary conjugation, $j\mapsto-j$, $i\mapsto i$ |
| $\langle\breve Q\rangle_{\mathrm{ts}}=Q_+Q_-$ | the reduced norm |
| $\breve r=\rho e^{\phi j}$ | the modulus, an element of the cone $P$ |
| $\rho>0$, $\phi\in\mathbb{R}$ | the radius and the boost |
| $\alpha,\beta$ | the two phases, modulo $2\pi$ |
| $u=e^{i\alpha}e^{ij\beta}$ | the unit factor, an element of the torus $T^2$ |
| $M_{\breve Q}(\breve X)=\breve Q\breve X$ | the multiplication operator |
| $\Theta_{\breve Q}(\breve X)=\breve Q\breve X\bar{\breve Q}$ | the two-sided operator |
| $\Theta^{\mathrm{c}},\Theta^{\mathrm{e}}$ | the sandwiches of the coefficient and elementary conjugations |
| $G=\operatorname{diag}(1,-1)$ | the complex bilinear form of the reduced norm |
| $S_\pm=\mathbb{C}\Pi_\pm$ | the two minimal ideals, the spinor spaces |
| $\mathbb{B}_{\mathrm{r}}^{\times}\cong\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ | the group of units |

## Further Reading

- [Modulus–Unit Polar Decomposition of Reduced Biquaternions](modulus-unit-polar-decomposition-of-reduced-biquaternions.html), for the modulus in the cone, the unit torus and the existence theorem.
- [Exponential Polar Decomposition of Reduced Biquaternions](exponential-polar-decomposition-of-reduced-biquaternions.html), for the exponential word, the logarithm and the principal domain.
- [Eigenvalue Decomposition and Eigenbasis of a Reduced Biquaternion](eigenvalue-decomposition-and-eigenbasis-of-a-reduced-biquaternion.html), for the spectrum, the idempotents and the Peirce decomposition.
- [Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-a-reduced-biquaternion.html), for the dictionary between the polar parameters and the spectral data.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the minimal ideals and the Peirce corners.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the unit criterion and the zero divisors.
- [Reduced Biquaternion Spectral Theory](reduced-biquaternion-spectral-theory.html), for the spectrum of the left multiplication.
- [One-Sided Operator and the Polar Decomposition](one-sided-operator-and-the-polar-decomposition.html), for the non-commutative companion where the one-sided operator is the spinor action.
- [Two-Sided Operator and the Polar Decomposition](two-sided-operator-and-the-polar-decomposition.html), for the non-commutative companion where the sandwich is the vector action.
- [Operator and the Polar Decomposition of a Split-Complex Number](operator-and-the-polar-decomposition-of-a-split-complex-number.html), for the commutative real companion with one hyperbolic angle.
