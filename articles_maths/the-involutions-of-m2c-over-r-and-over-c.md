# __The Involutions of $M_2(\mathbb{C})$ over $\mathbb{R}$ and over $\mathbb{C}$__

## Introduction

**An involution of $M_2(\mathbb{C})$ is one of six maps up to conjugacy, and each fixes one of the spaces the rest of the series uses.**

The article classifies the involutions of order two, both the complex-linear and the conjugate-linear ones, computes the fixed space of each in explicit matrices, and identifies the fixed spaces with $\operatorname{Sym}_2$, $\operatorname{Herm}_2$, the line of scalars, the diagonal algebra and the quaternion algebra. It assumes *The Matrix Algebra $M_2(\mathbb{C})$* for the product and the transpose, and *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$* for the two real forms. It defers the two halves themselves to *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$* and *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

The biquaternion article to read alongside is *The Element: The Coordinates and the Conjugations*, where the three conjugations of $\mathbb{B}$ play the role of the three complex-linear involutions below. The dictionary is exact: the reversion, the conjugation and the reversion-conjugation of $\mathbb{B}$ are the transpose, the symplectic involution and conjugation by a reflection.

## The Three Kinds of Involution

**Definition.** An **involution** is a bijective $\mathbb{R}$-linear map $\theta$ of $M_2(\mathbb{C})$ with $\theta^{2}=\mathrm{id}$ that is either an automorphism or an antiautomorphism, and that is either $\mathbb{C}$-linear or conjugate-linear.

**Proposition.** There are four kinds, and all four occur.

**Proof.** The map is multiplicative or antimultiplicative, and it respects or reverses the scalars. Each of the four combinations has an example: the identity for linear automorphism, the transpose for linear antiautomorphism, the conjugation of entries for conjugate-linear automorphism, and the conjugate transpose for conjugate-linear antiautomorphism. Each of those four maps has square the identity.

**The fixed space is a real subspace.** For a conjugate-linear involution the fixed set is not a complex subspace; it is only real, of dimension $4$, since the eigenspaces of a real-linear involution with eigenvalues $\pm1$ partition the eight real dimensions, and $+1$ has dimension equal to that of $-1$ when exactly half the eigenvalues are $+1$.

**Every conjugate-linear involution fixes a four-real-dimensional space.** That number is the dimension of $M_2(\mathbb{R})$ and of $\operatorname{Herm}_2$ and of $\mathbb{H}$, which are the spaces that appear.

## The Two Real Forms

**Proposition.** The conjugation of entries $\sigma(A)=\bar A$ is a conjugate-linear involution of the algebra, and its fixed space is $M_2(\mathbb{R})$, of real dimension $4$.

**Proof.** Conjugation is additive, multiplicative and reverses scalars, and it has square the identity; a matrix is fixed exactly when all its entries are real.

**Proposition.** With $J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$ the map $\sigma_{J}(A)=J\bar AJ^{-1}$ is a conjugate-linear involution of the algebra, and its fixed space is the quaternion algebra

$$
\mathbb{H}=\left\{\begin{pmatrix}\alpha&\beta\\ -\bar\beta&\bar\alpha\end{pmatrix}\right\},
$$

of real dimension $4$.

**Proof.** $\sigma_J$ is the composition of the automorphism $A\mapsto JAJ^{-1}$ with the entrywise conjugation, so it is a conjugate-linear automorphism, and $\sigma_J^{2}=\mathrm{id}$ because $\bar J=J$ and $J^{2}=-I$ cancels between the two steps. The fixed condition $A=J\bar AJ^{-1}$ is equivalent to $\bar A=J^{-1}AJ=-JAJ$, which reads $\bar a=d$, $\bar b=-c$.

**The two forms are the ones of the base-field article.** That $M_2(\mathbb{R})$ and $\mathbb{H}$ are the two real forms of $M_2(\mathbb{C})$, and that no third exists, is *The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$*.

**The biquaternion reading.** The conjugation $\sigma$ restricted to $\mathbb{B}$ is the conjugation of the corpus that fixes the four Peirce coordinates and negates the mixed corners; on the matrix side it is the entrywise conjugation, whose fixed algebra is the real matrices.

## The Transpose and the Symmetric Space

**Proposition.** The transpose $\tau(A)=A^{\mathsf T}$ is a $\mathbb{C}$-linear antiautomorphism of order two, and its fixed space is $\operatorname{Sym}_2$, of complex dimension $3$ and real dimension $6$.

**Proof.** $\tau(AB)=B^{\mathsf T}A^{\mathsf T}=\tau(B)\tau(A)$ and $\tau^{2}=\mathrm{id}$; a matrix is fixed exactly when $a_{12}=a_{21}$.

**The transpose is the reversion of the corpus.** In the biquaternion language the transpose is the reversion, which fixes the real scalars, the root of one and the imaginary units and negates the mixed corner coordinates; on the matrix side those are exactly the conditions $a_{12}=a_{21}$ in the Peirce basis. The correspondence is spelled out in *The Peirce Basis of the Biquaternion Algebra*.

**The $-1$ eigenspace is the antisymmetric line.** The antisymmetric matrices form the one-dimensional space $\mathbb{C}J$, and the transpose acts on it as $-1$.

**Corollary.** $M_2(\mathbb{C})=\operatorname{Sym}_2\oplus\Lambda^{2}\mathbb{C}^{2}$ is the eigenspace decomposition of the transpose, and the two summands have complex dimensions $3$ and $1$.

## The Conjugate Transpose and the Hermitian Space

**Proposition.** The conjugate transpose $\theta(A)=A^{*}=\bar A^{\mathsf T}$ is a conjugate-linear antiautomorphism of order two, and its fixed space is $\operatorname{Herm}_2$, of real dimension $4$.

**Proof.** $\theta(AB)=B^{*}A^{*}$ and $\theta^{2}=\mathrm{id}$; a matrix is fixed exactly when $\bar a_{ji}=a_{ij}$, that is when it is Hermitian.

**The anti-Hermitian space is the other eigenspace.** The matrices with $A^{*}=-A$ form the space $i\operatorname{Herm}_2$ of real dimension $4$, and

$$
M_2(\mathbb{C})=\operatorname{Herm}_2\oplus i\operatorname{Herm}_2
$$

is the real eigenspace decomposition of $\theta$.

**The trace is real on the fixed space.** For $A$ Hermitian the diagonal entries $a_{ii}$ are real, so $\operatorname{tr}A\in\mathbb{R}$; for $A$ anti-Hermitian the trace is purely imaginary. The two halves are therefore distinguished by the trace as well as by the involution, and that is the start of *The Two Halves over $\mathbb{C}$: Hermitian and Anti-Hermitian at $n=2$*.

## The Symplectic Involution and the Line of Scalars

**Proposition.** With $J$ as above the map $\tau_{J}(A)=JA^{\mathsf T}J^{-1}$ is a $\mathbb{C}$-linear antiautomorphism of order two whose fixed space is the line of scalars $\mathbb{C}I$.

**Proof.** It is the composition of the transpose with the automorphism $A\mapsto JAJ^{-1}$, hence an antiautomorphism, and its square is the identity because $J^{\mathsf T}=-J$ and $J^{-1}=-J$. Writing $A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ one computes $JA^{\mathsf T}J^{-1}=\begin{pmatrix}d&-b\\ -c&a\end{pmatrix}$, so the fixed condition is $b=c=0$ and $a=d$.

**The name.** $\tau_J$ is the **symplectic involution**: it is the involution attached to the alternating form $J$, and its $-1$ eigenspace is the three-dimensional space of traceless matrices, which is the symplectic Lie algebra $\mathfrak{sp}_2=\mathfrak{sl}_2$.

**Corollary.** $\tau_J$ acts as $+1$ on $\mathbb{C}I$ and as $-1$ on $\mathfrak{sl}_2(\mathbb{C})$.

**The two antiautomorphic involutions are the two sorts of form.** $\tau$ is attached to the symmetric form $I$ and $\tau_{J}$ to the alternating form $J$; these are the two types of involution of the first kind, orthogonal and symplectic, and at order two both exist because a nondegenerate alternating form needs an even dimension.

## The Linear Automorphism of Order Two

**Proposition.** Let $D=\operatorname{diag}(1,-1)$. The map $\rho(A)=DAD^{-1}$ is a $\mathbb{C}$-linear automorphism of order two, and its fixed space is the algebra of diagonal matrices, of complex dimension $2$.

**Proof.** Conjugation by an invertible matrix is an automorphism, and $D^{2}=I$ gives $\rho^{2}=\mathrm{id}$; the condition $DAD^{-1}=A$ reads $a_{12}=-a_{12}$ and $a_{21}=-a_{21}$.

**Every $\mathbb{C}$-linear automorphism of order two is of this form.** By Skolem–Noether an automorphism is $A\mapsto gAg^{-1}$, and $g^{2}$ must be central for the square to be the identity; so $g$ is a scalar multiple of an involution, and a non-scalar involution of order two is a reflection, all of which are conjugate to $D$.

**The fixed algebra is $\mathbb{C}\times\mathbb{C}$.** Diagonal matrices multiply entrywise, so the fixed algebra is the product of two copies of $\mathbb{C}$; its two minimal idempotents are $E_{11}$ and $E_{22}$.

**This is one point of the frame group, not a datum.** A reflection $R$ with $R^{2}=I$ and $R$ not scalar is a choice inside the conjugacy class of $D$; the biquaternion frame of *The Frame, the Simple Nilpotent and the Frame Group of $M_2(\mathbb{C})$* does not depend on it, and no article of the corpus assumes such an $R$ as part of the definition.

## The Classification

**Theorem.** Up to conjugacy there are exactly six nontrivial involutions:

$$
\tau(A)=A^{\mathsf T},\qquad
\tau_{J}(A)=JA^{\mathsf T}J^{-1},\qquad
\rho(A)=DAD^{-1},\qquad
\sigma(A)=\bar A,\qquad
\sigma_{J}(A)=J\bar AJ^{-1},\qquad
\theta(A)=A^{*},\qquad
\theta_{J}(A)=JA^{*}J^{-1}.
$$

**Proof.** A $\mathbb{C}$-linear antiautomorphism of $M_2(\mathbb{C})$ is $A\mapsto SA^{\mathsf T}S^{-1}$ for some invertible $S$, by the Skolem–Noether argument applied to the opposite algebra, and the square is the identity exactly when $S^{\mathsf T}=\pm S$; conjugating $S$ by $T$ replaces it by $T^{\mathsf T}ST$. A symmetric invertible matrix is congruent to $I$ and an anti-Hermitian one to $J$, so the two cases give $\tau$ and $\tau_{J}$. A $\mathbb{C}$-linear automorphism of order two is a conjugation by an involution, and all non-scalar involutions are conjugate to $D$. A conjugate-linear involution is $\sigma$ composed with one of the linear ones, giving $\sigma$, $\sigma_J$, and the two conjugate transposes $\sigma\circ\tau=\theta$ and $\sigma\circ\tau_{J}=\theta_{J}$.

**The fixed spaces are the six spaces of the series.**

| Involution | Kind | Fixed space | Real dimension |
|---|---|---|---|
| $\tau$, transpose | linear antiautomorphism | $\operatorname{Sym}_2$ | $6$ |
| $\tau_J$, symplectic | linear antiautomorphism | $\mathbb{C}I$ | $2$ |
| $\rho$, reflection | linear automorphism | diagonal algebra | $4$ |
| $\sigma$, entrywise conjugation | antilinear automorphism | $M_2(\mathbb{R})$ | $4$ |
| $\sigma_J$, quaternionic | antilinear automorphism | $\mathbb{H}$ | $4$ |
| $\theta_J$, symplectic | antilinear antiautomorphism | $\alpha$, $\beta$ form | $4$ |

**The last row is the fourth conjugate-linear fixed space.** The map $\theta_{J}$ fixes the matrices $\begin{pmatrix}\alpha+i\beta&i\gamma\\ i\delta&\alpha-i\beta\end{pmatrix}$ with real $\alpha,\beta,\gamma,\delta$, of real dimension $4$.

**The pairs are the two halves.** The three linear involutions cut $M_2(\mathbb{C})$ into $\operatorname{Sym}_2\oplus\Lambda^{2}$, into $\mathbb{C}I\oplus\mathfrak{sl}_2$, and into the diagonal algebra plus its complement; the two conjugate-linear ones cut the real algebra into $M_2(\mathbb{R})$ or $\mathbb{H}$ and their complements. These cuts are the decompositions of *The Fine Decomposition against the Diagonal at $n=2$*.

## Summary

An involution of $M_2(\mathbb{C})$ is an automorphism or an antiautomorphism of order two, linear or conjugate-linear. Up to conjugacy there are six nontrivial ones: the transpose, the symplectic involution $JA^{\mathsf T}J^{-1}$, the conjugation by a reflection, the entrywise conjugation, the quaternionic conjugation $J\bar AJ^{-1}$, and the conjugate transpose with its symplectic companion. The fixed spaces are $\operatorname{Sym}_2$ of complex dimension $3$, the line $\mathbb{C}I$, the diagonal algebra of complex dimension $2$, and the two real forms $M_2(\mathbb{R})$ and $\mathbb{H}$ of real dimension $4$; the conjugate transpose fixes $\operatorname{Herm}_2$, also of real dimension $4$.

| Involution | Kind | Fixed space | $\dim_{\mathbb{R}}$ |
|---|---|---|---|
| $\tau$ | linear antiautomorphism | $\operatorname{Sym}_2$ | $6$ |
| $\tau_J$ | linear antiautomorphism | $\mathbb{C}I$ | $2$ |
| $\rho$ | linear automorphism | diagonal | $4$ |
| $\sigma$ | antilinear automorphism | $M_2(\mathbb{R})$ | $4$ |
| $\sigma_J$ | antilinear automorphism | $\mathbb{H}$ | $4$ |
| $\theta$ | antilinear antiautomorphism | $\operatorname{Herm}_2$ | $4$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau$ | the transpose $A\mapsto A^{\mathsf T}$ |
| $\tau_J$ | the symplectic involution $JA^{\mathsf T}J^{-1}$ |
| $\rho$ | the conjugation by $D=\operatorname{diag}(1,-1)$ |
| $\sigma$ | the entrywise conjugation $A\mapsto\bar A$ |
| $\sigma_J$ | the quaternionic conjugation $J\bar AJ^{-1}$ |
| $\theta$ | the conjugate transpose $A^{*}$ |
| $J$ | $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, the alternating form |
| $\operatorname{Sym}_2$ | the fixed space of $\tau$ |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (AMS, 1998), for the classification of the involutions of a central simple algebra into orthogonal and symplectic types.
- Israel Nathan Herstein, *Noncommutative Rings* (Carus Mathematical Monographs, 1968), for the Skolem–Noether theorem in the form used here.
- [The Two Base Fields: $M_2(\mathbb{R})$ inside $M_2(\mathbb{C})$](the-two-base-fields-m2r-inside-m2c.html), for the two real forms.
- [The Element: The Coordinates and the Conjugations](the-element-the-coordinates-and-the-conjugations-in-the-biquaternion-algebra.html), for the three conjugations of the biquaternion algebra.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the reversion in the Peirce coordinates.
