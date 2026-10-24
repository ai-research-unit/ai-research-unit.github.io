# __Operator and the Polar Decomposition of a Split-Complex Number__

## Introduction

The **multiplication operator** of a split-complex number $Q=q+jq'$ is

$$
M_Q:\mathbb{D}\longrightarrow\mathbb{D},\qquad M_Q(X)=QX.
$$

The algebra $\mathbb{D}=\mathbb{R}[j]$, $j^2=1$, is commutative, so the left and the right multiplications coincide,

$$
L_Q=R_Q=M_Q.
$$

There is one one-sided operator, not two. The **two-sided operator** is the sandwich

$$
\Theta_Q:\mathbb{D}\longrightarrow\mathbb{D},\qquad \Theta_Q(X)=QX\bar Q,
\qquad \bar Q=q-jq'.
$$

The polar decomposition writes

$$
Q=r\,\epsilon\exp(\phi j),
\qquad r=\sqrt{\lvert N\rvert}>0,\quad \epsilon\in\{\pm1,\pm j\},\quad \phi\in\mathbb{R},
\qquad N=Q\bar Q=q^2-q'^2.
$$

The operator inherits the word,

$$
M_Q=r\,M_\epsilon\,\exp(\phi M_j),
\qquad
M_j=\begin{pmatrix}0&1\\1&0\end{pmatrix},
$$

and in the eigenbasis $(\Pi_+,\Pi_-)$ of the idempotents $\Pi_\pm=\tfrac12(1\pm j)$ it is diagonal:

$$
M_Q=\operatorname{diag}(\lambda_+,\lambda_-),
\qquad
\lambda_\pm=q\pm q'=r\,\epsilon_\pm e^{\pm\phi},
$$

where $\epsilon=\epsilon_+\Pi_++\epsilon_-\Pi_-$ with $\epsilon_\pm=\pm1$. The four pairs $(\epsilon_+,\epsilon_-)\in\{\pm1\}^2$ are the four components of the group of units.

Four results are proved. The map $Q\mapsto M_Q$ is a faithful representation of $\mathbb{D}$ on itself: the operator is the algebra read on its regular module. The spectrum is $\{\lambda_+,\lambda_-\}$, and the eigenbasis is the fixed idempotent basis, independent of $Q$. The one-sided operator carries the full hyperbolic angle $\phi$: its eigenvalues are $e^{\pm\phi}$, not $e^{\pm\phi/2}$. The two-sided operator is the scalar $N(Q)$: it is the inner automorphism multiplied by the norm, the inner automorphism is trivial because the algebra is commutative, and the operator sees only the modulus squared and the sign of the norm.

The last point is the structural difference from the biquaternion. In $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ the algebra is non-commutative, $L_{\tilde Q}$ and $R_{\tilde Q}$ differ, the one-sided operator is the spinor action with the half-angle, and the sandwich is the vector action with the full angle. In $\mathbb{D}$ the algebra is commutative, the two sides coincide, the one-sided operator is the regular representation, and the sandwich is a scalar. The half-angle is not a feature of the polar decomposition alone; it is a feature of the non-commutative spinor structure.

| Question | Answer |
|---|---|
| Algebra | $\mathbb{D}=\mathbb{R}[j]$, $j^2=1$ |
| Element | $Q=q+jq'$ |
| One-sided operator | $M_Q(X)=QX$, with $L_Q=R_Q=M_Q$ |
| Two-sided operator | $\Theta_Q(X)=QX\bar Q=N(Q)X$ |
| Spectrum of $M_Q$ | $\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$ |
| Eigenbasis | $(\Pi_+,\Pi_-)$, fixed and independent of $Q$ |
| Polar word | $Q=r\epsilon\exp(\phi j)$ |
| One-sided exponent | $\phi$, the full hyperbolic angle |
| Two-sided exponent | $0$; the boost cancels, the scale squares |
| Half-angle | none |
| Nilpotents | none |

## Conventions

The algebra is $\mathbb{D}=\mathbb{R}[j]$, with $j^2=+1$, general element $Q=q+jq'$ and conjugate $\bar Q=q-jq'$. The norm is

$$
N=Q\bar Q=q^2-q'^2.
$$

The idempotents are

$$
\Pi_+=\frac{1+j}{2},\qquad \Pi_-=\frac{1-j}{2},
\qquad
\Pi_+^2=\Pi_+,\quad \Pi_-^2=\Pi_-,\quad \Pi_+\Pi_-=0,\quad \Pi_++\Pi_-=1.
$$

The idempotent coordinates are $\lambda_\pm=q\pm q'$, and

$$
Q=\lambda_+\Pi_++\lambda_-\Pi_-.
$$

The eigenvalues are written $\lambda_\pm$ when their values are exhibited and $Q_\pm$ when they are read as idempotent coordinates, as in *Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number*. The modulus and the component sign are those of *Modulus–Unit Polar Decomposition of Split-Complex Numbers*:

$$
r=\sqrt{\lvert N\rvert},\qquad u=\frac{Q}{r}=\epsilon\exp(\phi j),\qquad \epsilon\in\{\pm1,\pm j\},\quad \phi\in\mathbb{R}.
$$

The operator is written $M_Q$ because there is only one side; the letters $L$ and $R$ are reserved for the biquaternion comparison. The two-sided operator is written $\Theta_Q$. The split form is

$$
g=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.
$$

## The Multiplication Operator

### Definition and Laws

**Definition.** For $Q\in\mathbb{D}$ the multiplication operator is $M_Q(X)=QX$.

**Proposition (the representation).** The map $M:Q\mapsto M_Q$ is $\mathbb{R}$-linear and multiplicative,

$$
M_{Q+P}=M_Q+M_P,\qquad M_{QP}=M_Q\circ M_P,\qquad M_1=\operatorname{id},
$$

and faithful: $M_Q(1)=Q$, so $M_Q=0$ exactly when $Q=0$, and $M_Q=M_P$ exactly when $Q=P$. The image is the algebra of real matrices

$$
\left\{\begin{pmatrix}q&q'\\q'&q\end{pmatrix}:q,q'\in\mathbb{R}\right\},
$$

which is isomorphic to $\mathbb{D}$.

*Proof.* The laws are the associativity and the distributivity of the algebra. Faithfulness is evaluation at $1$. The matrix is computed on the basis: $Q\cdot1=q+jq'$ and $Q\cdot j=q'+jq$, hence the two columns $(q,q')$ and $(q',q)$.

**Corollary (invertibility).** $M_Q$ is invertible exactly when $Q$ is a unit, that is, exactly when $N\neq0$. The inverse is $M_{Q^{-1}}$, with

$$
Q^{-1}=\frac{\bar Q}{N}.
$$

**Proposition (commutation).** For all $Q,P$,

$$
M_QM_P=M_PM_Q=M_{QP}.
$$

The operator algebra is commutative; it is the regular representation of $\mathbb{D}$.

**Proposition (the split form).** With $g=\operatorname{diag}(1,-1)$,

$$
M_Q^{T}gM_Q=N(Q)\,g.
$$

*Proof.* Direct computation:

$$
\begin{pmatrix}q&q'\\q'&q\end{pmatrix}
\begin{pmatrix}1&0\\0&-1\end{pmatrix}
\begin{pmatrix}q&q'\\q'&q\end{pmatrix}
=
\begin{pmatrix}q^2-q'^2&0\\0&q'^2-q^2\end{pmatrix}
=(q^2-q'^2)g.
$$

Thus $M_Q$ is a conformal operator for the split form, with conformal factor $N(Q)$. For $N=1$ it is, up to the component sign, a boost of rapidity $\phi$; for $N=-1$ it is, up to the component sign, a boost times the reflection $j$.

### The Two Matrices

In the basis $(1,j)$ the matrix is

$$
M_Q=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}.
$$

In the eigenbasis $(\Pi_+,\Pi_-)$ it is

$$
M_Q=\operatorname{diag}(\lambda_+,\lambda_-),
\qquad
\lambda_\pm=q\pm q'.
$$

The change of basis is

$$
P=\frac12\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
P^{-1}=2P,
\qquad
P^{-1}M_QP=\operatorname{diag}(\lambda_+,\lambda_-).
$$

The characteristic polynomial is

$$
p_Q(X)=X^2-2qX+N=(X-\lambda_+)(X-\lambda_-),
$$

with trace $2q$ and determinant $N$. The discriminant is $4q'^2$, so the eigenvalues are distinct exactly when $q'\neq0$.

### The Spectrum and the Eigenbasis

**Theorem.** The spectrum of $M_Q$ is $\{\lambda_+,\lambda_-\}=\{q+q',q-q'\}$. The eigenspaces are the two minimal ideals

$$
S_+=\mathbb{R}\Pi_+,\qquad S_-=\mathbb{R}\Pi_-,
\qquad
\mathbb{D}=S_+\oplus S_-.
$$

*Proof.* In the eigenbasis the matrix is diagonal with entries $\lambda_\pm$, and $\Pi_\pm$ are the corresponding idempotents: $Q\Pi_\pm=\lambda_\pm\Pi_\pm$.

The eigenbasis is **fixed**: it is the standard idempotent pair, and it does not depend on $Q$. This is the commutative simplification. In the biquaternion the eigenbasis is the $Q$-adapted Peirce basis, built from the nilpotents and depending on $Q$; here the two idempotents are the only nontrivial idempotents, and the Peirce corners are zero.

The eigenvalues are the two idempotent coordinates. Their sum is $2q$ and their product is $N$. The spectrum is real and, when $q'\neq0$, simple. When $q'=0$ the element is the scalar $q$, the two eigenvalues coincide, and $M_Q=q\operatorname{id}$.

### Kernel and Image

**Proposition.** Let $Q\in\mathbb{D}$.

**(a)** If $N\neq0$, then $M_Q$ is bijective.

**(b)** If $N=0$ and $Q\neq0$, then $Q$ is a nonzero multiple of $\Pi_+$ or of $\Pi_-$, the operator has rank one, its kernel is the other minimal ideal, and its image is the line spanned by $Q$.

**(c)** If $Q=0$, then $M_Q=0$.

*Proof.* (a) is the invertibility corollary. For (b), a nonzero null element satisfies $Q_+Q_-=0$, so exactly one idempotent coordinate is nonzero. If $Q=\lambda_+\Pi_+$ with $\lambda_+\neq0$, then $M_Q=\lambda_+\Pi_+$: the image is $S_+$ and the kernel is $S_-$. The other case is symmetric. (c) is immediate.

The image is the principal ideal $Q\mathbb{D}$; the kernel is the annihilator

$$
\operatorname{Ann}(Q)=\{X:QX=0\}.
$$

In the null case both are one of the two minimal ideals. In the unit case the kernel is the zero ideal and the image is the whole algebra. There is no intermediate rank over $\mathbb{R}$: the rank is $2$, $1$ or $0$.

## The Polar Word, One-Sided

### The Factorisation of the Operator

The polar word $Q=r\epsilon\exp(\phi j)$ gives

$$
M_Q=r\,M_\epsilon\,\exp(\phi M_j).
$$

In the eigenbasis, $M_j=\operatorname{diag}(1,-1)$ and $M_\epsilon=\operatorname{diag}(\epsilon_+,\epsilon_-)$, so

$$
M_Q=\operatorname{diag}\bigl(r\epsilon_+e^{\phi},\,r\epsilon_-e^{-\phi}\bigr)
=\operatorname{diag}(\lambda_+,\lambda_-).
$$

The three factors have distinct roles. The scale $r$ acts as $r$, not as $r^2$. The component sign $\epsilon$ is a discrete diagonal sign. The boost $\phi$ acts as $e^{\pm\phi}$. All three are visible to the one-sided operator.

### The Exponents and the Absence of a Half-Angle

The exponent of the operator is

$$
\ln r+\phi M_j
$$

on the identity component, with the discrete sign $\epsilon$ on the four components. In the eigenbasis the exponents are $\ln r\pm\phi$, and the eigenvalues are $r e^{\pm\phi}$ up to sign.

The hyperbolic angle is $\phi$, the full angle. It is not $\phi/2$. The eigenvalues of the boost are $e^{\pm\phi}$, not $e^{\pm\phi/2}$.

The contrast with the biquaternion is a contrast of generators. There the rotor is $\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$, and the spinor weights are $e^{\pm i\theta/2}$; the factor $\tfrac12$ is written in the polar word itself. Here the boost is $\exp(\phi j)$, and the weights are $e^{\pm\phi}$; the polar word carries no $\tfrac12$.

A half-angle would require one of two things: a square root of $Q$, or a module on which $j$ acts by $\pm\tfrac12$. Neither is part of the polar decomposition. If $Q=S^2$, then $M_Q=(M_S)^{2}$, and the eigenvalues of $M_S$ are the square roots of those of $M_Q$; but $S$ is not the polar factor, and the polar decomposition does not take this square root. On the minimal ideals, $j$ acts by $\pm1$, not by $\pm\tfrac12$; a spin lift would need a module on which $j$ acts by $\pm\tfrac12$.

The map $Q\mapsto M_Q$ is faithful, so there is no sign ambiguity: $Q$ and $-Q$ give different operators. The group of units is

$$
\mathbb{D}^{\times}\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2.
$$

Its identity component is $\mathbb{R}^2$, simply connected; the exponential is an isomorphism onto the future cone. The discrete sign $\epsilon$ is a component label, not a lift of a continuous angle. No double cover is used.

### The Spinor Reading

The minimal left ideals $S_\pm=\mathbb{R}\Pi_\pm$ are one-dimensional. A spinor is a single real coordinate on one ideal:

$$
\xi_+=\alpha\Pi_+,\qquad \xi_-=\beta\Pi_-,
\qquad \alpha,\beta\in\mathbb{R}.
$$

The operator acts by

$$
M_Q\xi_+=\lambda_+\xi_+,\qquad M_Q\xi_-=\lambda_-\xi_-,
$$

and never mixes the two ideals. The two spinor spaces are the two null lines of the split form. The word spinor is algebraic: an element of a minimal left ideal. The weight of $S_\pm$ under the boost is $\pm\phi$, not $\pm\phi/2$. The Lorentz spinor of $SO^{+}(1,1)$, of weight $\pm\phi/2$, is a different module; it is not an element of $\mathbb{D}$.

The two ideals are also the two Peirce components. They are not the two Lorentz chiralities; the algebra is two-dimensional, and its two invariant lines are the null lines of the vector representation. The distinction is the same as in the biquaternion, where the Peirce chiralities are not the Lorentz chiralities.

### The Matrix Picture

The explicit matrices are

$$
Q=r\epsilon\exp(\phi j):
\qquad
M_Q=r\epsilon\begin{pmatrix}\cosh\phi&\sinh\phi\\\sinh\phi&\cosh\phi\end{pmatrix}
\quad(\epsilon=\pm1),
$$

$$
Q=r\epsilon j\exp(\phi j):
\qquad
M_Q=r\epsilon\begin{pmatrix}\sinh\phi&\cosh\phi\\\cosh\phi&\sinh\phi\end{pmatrix}
\quad(\epsilon=\pm j).
$$

The first is, up to the component sign, a boost of rapidity $\phi$; the second is, up to the component sign, a boost times the reflection $j$. The determinant is $N=\pm r^2$, with the sign $+$ on the timelike components and $-$ on the spacelike components. The split-form identity $M_Q^{T}gM_Q=Ng$ holds in both cases.

## The Two-Sided Operator

### The Collapse to a Scalar

**Theorem.** For every $Q$,

$$
\Theta_Q(X)=QX\bar Q=N(Q)\,X.
$$

*Proof.* The algebra is commutative and $Q\bar Q=N(Q)$ is central. Hence $QX\bar Q=Q\bar Q\,X=N(Q)X$.

In the eigenbasis,

$$
\Theta_Q=\operatorname{diag}(N,N)=\lambda_+\lambda_-\,\operatorname{id}.
$$

The two-sided operator is a scalar operator. It is multiplicative,

$$
\Theta_Q\circ\Theta_P=\Theta_{QP},
$$

but it is not faithful: $\Theta_Q=\Theta_P$ exactly when $N(Q)=N(P)$.

On the units the operator is the inner automorphism multiplied by the norm. For a unit, $\bar Q=NQ^{-1}$, so

$$
\Theta_Q=N\,\operatorname{Ad}_Q=N\,\operatorname{id}
$$

because the algebra is commutative. On the norm-one slice $\bar Q=Q^{-1}$ and $\Theta_Q=\operatorname{id}$.

The inner automorphism $\operatorname{Ad}_Q$ of a commutative algebra is the identity. This is the structural reason for the collapse: the sandwich is a conjugation, and there is nothing to conjugate.

### The Polar Reading

Write $Q=r\epsilon\exp(\phi j)$. Then

$$
\Theta_Q=N(Q)\operatorname{id}=\operatorname{sign}(N)\,r^2\operatorname{id}.
$$

The scale is squared, $r\mapsto r^2$. The boost cancels, $\phi\mapsto0$, because $e^{\phi j}$ and its conjugate $e^{-\phi j}$ multiply to $1$. The sign of the norm survives: the timelike components give $+r^2$, the spacelike components give $-r^2$. The finer sign $\epsilon=\pm1$ within a pair of components is lost.

The sandwich is blind to the continuous unit factor. Every element on the same hyperbola $N=\text{constant}$ has the same two-sided operator. The fibre of $\Theta$ over $N$ is the hyperbola, not a point.

### The Image and the Kernel

On the group of units $\mathbb{D}^{\times}=\{N\neq0\}$ the map $Q\mapsto\Theta_Q$ has image

$$
\mathbb{R}^{\times}I=\{\lambda\operatorname{id}:\lambda\neq0\},
$$

and kernel

$$
\{Q:N(Q)=1\},
$$

the timelike unit hyperbola, with two connected components. On the unit set $\{\lvert N\rvert=1\}$ the image is $\{\pm I\}$ and the kernel is again $\{N=1\}$.

The image is not a Lorentz group. It is the group of nonzero scalar operators, of real dimension one. The kernel is one-dimensional, and the quotient has dimension one. The two-sided operator has lost the boost, which is the continuous angular content of the group of units.

## The Two-Sided Family

Every two-sided operator of the form $L_A R_B$ is a one-sided operator in a commutative algebra:

$$
L_AR_B=M_{AB}.
$$

The family is the algebra itself, and the sandwich is the case $B=\bar A$. The commutator vanishes,

$$
[L_A,R_B]=0,
$$

and every derivation is zero:

$$
\operatorname{ad}_Q(X)=QX-XQ=0.
$$

Consequently the inner automorphism $\operatorname{Ad}_Q=L_QR_{Q^{-1}}$ is the identity for every unit $Q$. There is no nontrivial conjugation action of the unit group on the algebra. The only nontrivial action is left multiplication, that is, the regular representation.

This is the reason why the two-sided operator cannot carry the boost. In the biquaternion the sandwich is, up to the scale, an inner automorphism, and the non-commutativity makes it a Lorentz transformation. Here the sandwich is an inner automorphism of a commutative algebra, and it is the identity.

## The Null Cone and the Degenerate Cases

The null cone is $N=0$, that is, the pair of lines $q=\pm q'$, equivalently $S_+\cup S_-$ away from the origin. It is the zero-divisor set.

**Proposition.** Let $Q\neq0$ be null.

**(a)** $M_Q$ has rank one. If $Q=\lambda_+\Pi_+$ with $\lambda_+\neq0$, then the image is $S_+$ and the kernel is $S_-$; if $Q=\lambda_-\Pi_-$ with $\lambda_-\neq0$, the roles are exchanged.

**(b)** There is no polar decomposition of $Q$: the modulus $r=\sqrt{\lvert N\rvert}$ vanishes.

**(c)** $\Theta_Q=0$.

*Proof.* (a) is the kernel and image proposition. (b) is the definition of the modulus. (c) is $N=0$.

The scalar case $q'=0$ is the other degeneration. Then $Q=q$ is central, $M_Q=q\operatorname{id}$, the two eigenvalues coincide, and the boost is zero. The operator is a scalar multiple of the identity, and its two-sided operator is $q^2\operatorname{id}$.

There are no nilpotents. The algebra is $\mathbb{D}\cong\mathbb{R}\times\mathbb{R}$, which is reduced: every element is semisimple, the minimal polynomial is squarefree, and $M_Q$ is diagonalizable over $\mathbb{R}$ for every $Q$. There is no Jordan block and no nilpotent regime. The nilpotent construction of the biquaternion, with the two elements $\vec\Upsilon_\pm$ of square zero, has no analogue here: the Peirce corners of the fixed idempotents are zero.

## Comparison with the Biquaternion Case

| Item | Biquaternion $\mathbb{B}$ | Split-complex $\mathbb{D}$ |
|---|---|---|
| Commutative | no | yes |
| One-sided operators | $L_{\tilde Q}\neq R_{\tilde Q}$ | $L_Q=R_Q=M_Q$ |
| Spectrum of the one-sided operator | $\lambda_\pm=Q_t\pm iB$, each twice | $\lambda_\pm=q\pm q'$ |
| Eigenbasis | $Q$-adapted Peirce basis, depends on $Q$ | fixed $(\Pi_+,\Pi_-)$ |
| One-sided exponent | $\theta/2$, $\psi/2$ | $\phi$ |
| Two-sided operator | $\tilde Q\tilde X\tilde Q^{*}$, non-scalar | $N(Q)X$, scalar |
| Two-sided exponent | $\theta$, $\psi$ | $0$ |
| Image on the units | $CO^{+}(1,3)$ | $\mathbb{R}^{\times}I$ |
| Kernel on the units | $U(1)$ | $\{N=1\}$ |
| Nilpotents | yes, when $B\neq0$ | none |
| Half-angle | yes | no |

The table records a reversal. In the biquaternion the one-sided operator is the spinor action: it carries half the angle, and the two-sided sandwich is the vector action, which carries the full angle. In the split-complex algebra the one-sided operator is the regular representation: it carries the full angle, and the two-sided sandwich is a scalar, which carries none.

The reason is the commutativity. The biquaternion is the tensor product $S\otimes S^{*}$ of a spinor space and its dual; the left multiplication acts on one factor, the right multiplication on the other, and the sandwich acts on the pair. The split-complex algebra is two-dimensional and commutative; its regular representation is the two-dimensional vector representation, and the sandwich is the inner automorphism, which is trivial. The half-angle belongs to the spinor factor, not to the polar word alone.

The split-complex article is therefore the commutative degenerate case of the biquaternion story, not a parallel spin story. The polar decomposition still has four components and a hyperbolic angle, but the operator does not produce a half-angle, a double cover, or a nilpotent Peirce basis.

## Summary

The multiplication operator $M_Q(X)=QX$ is a faithful representation of $\mathbb{D}$ on itself. In the fixed eigenbasis $(\Pi_+,\Pi_-)$ it is diagonal with eigenvalues $\lambda_\pm=q\pm q'$, and these are the idempotent coordinates of $Q$.

The polar word $Q=r\epsilon\exp(\phi j)$ reads $M_Q=\operatorname{diag}(r\epsilon_+e^{\phi},r\epsilon_-e^{-\phi})$. The scale acts as $r$, the boost as $e^{\pm\phi}$, and the sign as a discrete diagonal sign. The hyperbolic angle is full, not half.

The two-sided operator is $QX\bar Q=N(Q)X$. It is the inner automorphism multiplied by the norm; the inner automorphism of a commutative algebra is the identity, so the operator is the scalar $N(Q)$. The scale squares, the boost cancels, and only the sign of the norm survives. On the units the image is $\mathbb{R}^{\times}I$ and the kernel is $\{N=1\}$.

The null cone gives rank one. There are no nilpotents and no Jordan blocks: the algebra is reduced. The half-angle, the spin double cover and the $Q$-adapted Peirce basis of the biquaternion have no analogue.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | the split-complex algebra $\mathbb{R}[j]$, $j^2=1$ |
| $Q=q+jq'$ | a split-complex number |
| $\bar Q=q-jq'$ | the conjugate |
| $N=Q\bar Q=q^2-q'^2$ | the norm |
| $\Pi_\pm=\tfrac12(1\pm j)$ | the two idempotents |
| $\lambda_\pm=q\pm q'$ | the two eigenvalues, the idempotent coordinates |
| $r=\sqrt{\lvert N\rvert}$ | the modulus |
| $\epsilon\in\{\pm1,\pm j\}$ | the component sign |
| $\phi\in\mathbb{R}$ | the hyperbolic angle |
| $M_Q(X)=QX$ | the multiplication operator |
| $\Theta_Q(X)=QX\bar Q$ | the two-sided operator |
| $g=\operatorname{diag}(1,-1)$ | the split form |
| $S_\pm=\mathbb{R}\Pi_\pm$ | the two minimal ideals, the spinor spaces |
| $\mathbb{D}^{\times}\cong(\mathbb{Z}/2\mathbb{Z})^2\times\mathbb{R}^2$ | the group of units |

## Further Reading

- [Modulus–Unit Polar Decomposition of Split-Complex Numbers](modulus-unit-polar-decomposition-of-split-complex-numbers.html), for the modulus, the unit factor and the four components.
- [Exponential Polar Decomposition of Split-Complex Numbers](exponential-polar-decomposition-of-split-complex-numbers.html), for the exponential word, the component sign and the logarithm.
- [Eigenvalue Decomposition and Eigenbasis of a Split-Complex Number](eigenvalue-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the spectrum, the idempotents and the Peirce decomposition.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the dictionary between the polar parameters and the spectral data.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the minimal ideals and the Peirce corners.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the unit criterion and the null cone.
- [One-Sided Operator and the Polar Decomposition](one-sided-operator-and-the-polar-decomposition.html), for the non-commutative companion where the one-sided operator is the spinor action.
- [Two-Sided Operator and the Polar Decomposition](two-sided-operator-and-the-polar-decomposition.html), for the non-commutative companion where the sandwich is the vector action.
- [Operator and the Polar Decomposition of a Reduced Biquaternion](operator-and-the-polar-decomposition-of-a-reduced-biquaternion.html), for the commutative complex companion with two phases.
