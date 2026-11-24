# __The Anti-Hermitian Derivations of $M_2(\mathbb{C})$ as $\mathfrak{su}(2)$__

## Introduction

**Two conditions pick out the generators: anti-Hermitian and traceless. They hold exactly for the three matrices $i\sigma_1,i\sigma_2,i\sigma_3$, which form $\mathfrak{su}(2)$. Each gives the derivation $[A,\cdot]$ of the matrix algebra, the array of which is $-2[a^\times]$ in the Pauli basis, and the exponential of which is the conjugation by the rotor $e^{A}\in\mathrm{SU}(2)$. Read on the vector part, the conjugation is the rotation of angle $-2\theta$ about the axis of the generator.**

The article is the matrix frame of *The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$*. The operator is the same and the numbers are the same; the difference is that here the generator is a $2\times2$ matrix, so the three of them can be written out in full, together with their three distinct rotor actions.

The three generators are not three copies of one thing. One of them generates a real rotation, one generates a mixing with the imaginary unit, and one generates a pair of opposite phases. The three cases are the three families of $\mathfrak{su}(n)$: the real antisymmetric part, the off-diagonal symmetric part multiplied by $i$, and the diagonal traceless part. At $n=2$ each family has one member, so the three generators realize the three cases one apiece; at $n=4$ they have six, six and three.

The article assumes the Lie group results of *The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$*, the Lie correspondence of *The Lie Correspondence and the Adjoint Representation*, and the determinant formula $\det e^{F}=e^{\operatorname{tr}F}$.

## The Two Conditions on the Matrix

### Anti-Hermitian and Traceless

**Proposition (the generators).** The matrices $A\in M_2(\mathbb{C})$ with $A^{*}=-A$ and $\operatorname{tr}A=0$ are exactly the complex linear combinations of $i\sigma_1,i\sigma_2,i\sigma_3$. They form a real vector space of dimension three, closed under the bracket, isomorphic to $\mathfrak{su}(2)$.

**Proof.** A general element is $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$ with $a,d$ purely imaginary and $c=-\bar b$. So the real parameters are $\operatorname{Im}a$, $\operatorname{Im}d$, $\operatorname{Re}b$, $\operatorname{Im}b$: four. The trace condition is $\operatorname{Im}a+\operatorname{Im}d=0$, one real equation, leaving three. The three $i\sigma_k$ are anti-Hermitian and traceless, and they are independent, so they are a basis. The bracket of two anti-Hermitian matrices is anti-Hermitian and traceless, so the space closes.

**Remark (the three families, one member each).** Write $A$ as a real antisymmetric part plus $i$ times a real symmetric part,

$$
A=\underbrace{\tfrac12(A-\bar A)}_{\text{real antisymmetric}}+i\,\underbrace{\tfrac1{2i}(A+\bar A)}_{\text{real symmetric}} .
$$

The first summand has dimension one at order two and is spanned by $i\sigma_2$, which is real and antisymmetric. The second has dimension two, since the symmetric real matrices of trace zero form a line, plus the off-diagonal direction. The line is $i\sigma_3$ and the off-diagonal direction is $i\sigma_1$. The count is $1+2=3$, and the same split at order $n$ gives $\tfrac12n(n-1)+\tfrac12n(n+1)-1$, which at $n=4$ is $6+9=15$.

**Remark (what the split is worth).** The first summand is a subalgebra: the real antisymmetric matrices of order $n$ close under the bracket, and they form $\mathfrak{so}(n)$. The second summand is not a subalgebra at any order above two. So the fifteen of $\mathfrak{su}(4)$ split as $6+9$ with the six closed and the nine not, and the three of $\mathfrak{su}(2)$ split as $1+2$ with the one closed and the two not.

## The Three Generators, Written Out

**Definition.** The three generators are

$$
i\sigma_1=\begin{pmatrix}0&i\\i&0\end{pmatrix},\qquad
i\sigma_2=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\qquad
i\sigma_3=\begin{pmatrix}i&0\\0&-i\end{pmatrix}.
$$

Each is anti-Hermitian and traceless, each squares to $-\mathrm{I}_2$, and each has the eigenvalues $\pm i$.

| generator | family | entries | square | $\det$ | rotor $e^{\theta A}$ |
|---|---|---|---|---|---|
| $i\sigma_1$ | $i$ times symmetric | off-diagonal, both entries $i$ | $-\mathrm{I}_2$ | $1$ | $\cos\theta\,\mathrm{I}_2+i\sin\theta\,\sigma_1$ |
| $i\sigma_2$ | real antisymmetric | $1$ and $-1$ | $-\mathrm{I}_2$ | $1$ | $\cos\theta\,\mathrm{I}_2+\sin\theta\,(i\sigma_2)$ |
| $i\sigma_3$ | diagonal | $i$ and $-i$ | $-\mathrm{I}_2$ | $1$ | $\operatorname{diag}(e^{i\theta},e^{-i\theta})$ |

**Proposition (the three rotors, written out).** The exponentials are

$$
e^{\theta i\sigma_1}=\begin{pmatrix}\cos\theta&i\sin\theta\\ i\sin\theta&\cos\theta\end{pmatrix},\qquad
e^{\theta i\sigma_2}=\begin{pmatrix}\cos\theta&\sin\theta\\ -\sin\theta&\cos\theta\end{pmatrix},\qquad
e^{\theta i\sigma_3}=\begin{pmatrix}e^{i\theta}&0\\0&e^{-i\theta}\end{pmatrix}.
$$

**Proof.** Each generator squares to $-\mathrm{I}_2$, so the series is $\cos\theta\,\mathrm{I}_2+\sin\theta\,A$. Substituting the three matrices gives the three displays.

**Remark (three visibly different rotors).** The second matrix has real entries: it is a rotation of the plane. The third is diagonal: it multiplies the two coordinates by opposite phases. The first has imaginary entries off the diagonal: it mixes the two coordinates with a factor $i$. These are the three things that a unitary of determinant one can do to a two-dimensional space, and each generator produces one of them.

### The Commutators

**Proposition (the structure constants).** The three generators satisfy

$$
[i\sigma_1,i\sigma_2]=-2\,i\sigma_3,\qquad [i\sigma_2,i\sigma_3]=-2\,i\sigma_1,\qquad [i\sigma_3,i\sigma_1]=-2\,i\sigma_2 .
$$

**Proof.** $[\sigma_1,\sigma_2]=2i\sigma_3$ and $i^2=-1$ give the first; the other two are cyclic.

**Remark (the sign against the algebra frame).** The companion article on the biquaternion algebra has $[\mathrm{ad}_{\vec e_x},\mathrm{ad}_{\vec e_y}]=+2\,\mathrm{ad}_{\vec e_z}$, and here the constant is $-2$. The change of sign is the minus in $\mathsf M_2(\tilde Q)=Q_t\mathrm{I}_2-i\sum q_k\sigma_k$, which carries the vector part of the algebra to $-i$ times the Pauli combination; the two brackets are the same bracket read through that minus.

## The Derivation and Its Array

### The Derivation

**Definition.** For $A$ in the algebra the derivation is $\mathrm{ad}_A(X)=[A,X]$.

**Proposition (it is a derivation and it is anti-Hermitian).** The Leibniz rule holds for all $X,Y$, and for the Hilbert–Schmidt form $\langle X,Y\rangle=\operatorname{tr}(X^{*}Y)$ one has $(\mathrm{ad}_A)^{*}=\mathrm{ad}_{A^{*}}$, so $\mathrm{ad}_A$ is anti-Hermitian exactly when $A$ is. The map $A\mapsto\mathrm{ad}_A$ has kernel the scalars, so it is injective on $\mathfrak{su}(2)$.

**Proof.** The Leibniz rule is associativity. For the adjoint, $\operatorname{tr}([A,X]^{*}Y)=\operatorname{tr}(X^{*}[A^{*},Y])$ by the cyclic invariance of the trace. The kernel is the centre, and a scalar multiple of $\mathrm{I}_2$ is traceless only when it is zero.

### The Array in the Pauli Basis

**Proposition (the three arrays).** In the basis $\mathrm{I}_2,\sigma_1,\sigma_2,\sigma_3$, in that order, the three derivations have the arrays

$$
\mathrm{ad}_{i\sigma_1}=
\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&0&0&2\\0&0&-2&0\end{pmatrix},\quad
\mathrm{ad}_{i\sigma_2}=
\begin{pmatrix}0&0&0&0\\0&0&0&-2\\0&0&0&0\\0&2&0&0\end{pmatrix},\quad
\mathrm{ad}_{i\sigma_3}=
\begin{pmatrix}0&0&0&0\\0&0&2&0\\0&-2&0&0\\0&0&0&0\end{pmatrix}.
$$

**Proof.** The scalars are fixed, so the first row and the first column vanish. On the three traceless Hermitian matrices the commutator acts as the cross product, and the table below gives the entries. The $2\times2$ block on the plane orthogonal to the axis is $-2R$ with $R$ the quarter-turn, in each case.

**Corollary (the vector block).** The lower right $3\times3$ block of the array of $\mathrm{ad}_{A}$ is $-2[a^\times]$, where $a$ is the coordinate vector of $A$ in the Pauli basis, and $[a^\times]$ is the cross-product matrix.

**Proof.** The table of the derivation's action on the Pauli basis is the table of the cross product with $a$, times $-2$. The three arrays above are the three axes.

**Corollary (the spectrum).** Each array has spectrum $\{0,0,\pm2i\}$, trace zero, and exponential of determinant one.

**Proof.** The block $-2[a^\times]$ for a unit axis has eigenvalues $\pm2i$ on the plane and $0$ on the axis; the scalar direction adds a second zero.

## The Exponential of Each Generator

### The Action on the Pauli Basis

**Proposition (the conjugation rotates the vector part).** With $U=e^{\theta i\sigma_k}$ and $c=\cos2\theta$, $s=\sin2\theta$, the conjugation $X\mapsto UXU^{*}$ fixes $\mathrm{I}_2$ and acts on the three Pauli matrices by

| generator | $\sigma_1$ | $\sigma_2$ | $\sigma_3$ |
|---|---|---|---|
| $i\sigma_1$ | $\sigma_1$ | $c\,\sigma_2-s\,\sigma_3$ | $s\,\sigma_2+c\,\sigma_3$ |
| $i\sigma_2$ | $c\,\sigma_1+s\,\sigma_3$ | $\sigma_2$ | $-s\,\sigma_1+c\,\sigma_3$ |
| $i\sigma_3$ | $c\,\sigma_1-s\,\sigma_2$ | $s\,\sigma_1+c\,\sigma_2$ | $\sigma_3$ |

**Proof.** $U\sigma_kU^{*}$ is traceless and Hermitian, so it is a real combination of the three Pauli matrices; the coefficients are the traces $\tfrac12\operatorname{tr}(U\sigma_kU^{*}\sigma_l)$, which are $\cos2\theta$ and $\pm\sin2\theta$ by the duplication formulas. The axis is fixed because $U$ commutes with its own generator.

**Corollary (one rotation, three axes).** The conjugation by $e^{\theta i\sigma_k}$ is the rotation of the vector part by the angle $-2\theta$ about the axis $k$, right-handed in the basis $\sigma_1,\sigma_2,\sigma_3$.

**Proof.** The three rows of the table are the three right-handed rotations of the basis, with the angle $-2\theta$ since the coefficient of $\sigma_3$ in the first row is $-\sin2\theta$.

**Remark (the angle is doubled and negative).** The doubling comes from the group being a double cover of the rotation group: the rotor of angle $\theta$ turns the vector part by $2\theta$. The minus comes from the conjugation acting on the Hermitian matrices rather than on the matrices themselves, which is the same minus as in the commutator table.

### What Each Generator Does

**Proposition (the three actions, one each).** Exponentiated, the three generators act as follows.

| generator | on the matrix $\mathrm{I}_2$ | on the axis | on the two remaining directions | in words |
|---|---|---|---|---|
| $i\sigma_1$ | fixed | $\sigma_1$ fixed | plane of $\sigma_2,\sigma_3$ turned by $-2\theta$ | mixes the two coordinates with a factor $i$ |
| $i\sigma_2$ | fixed | $\sigma_2$ fixed | plane of $\sigma_3,\sigma_1$ turned by $-2\theta$ | rotates the plane with real entries |
| $i\sigma_3$ | fixed | $\sigma_3$ fixed | plane of $\sigma_1,\sigma_2$ turned by $-2\theta$ | multiplies the two coordinates by opposite phases |

**Proof.** The fixed elements are read from the table: the conjugation fixes the identity and the axis. The turned plane is the orthogonal complement of the axis in the three dimensions, and the angle is $-2\theta$ by the corollary.

**Remark (the three families of rotor, at order two).** The second row is a rotation of the plane by a real angle: the map $z\mapsto e^{-2i\theta}z$ in the complex coordinate. The third row multiplies the two coordinates by $e^{2i\theta}$ and $e^{-2i\theta}$: two opposite phases, of sum zero. The first row sends $z\mapsto\cos2\theta\,z-i\sin2\theta\,\bar z$: a mixing of the coordinate with its conjugate. Every unitary of determinant one is a product of the three, and the three families at higher order are the same three operations applied to pairs of coordinates.

### The Closed Form

**Theorem (the exponential is the conjugation).** With $\rho=e^{A}$,

$$
e^{\mathrm{ad}_A}=\mathrm{Ad}_\rho,\qquad \mathrm{Ad}_\rho(X)=\rho X\rho^{*},
$$

and on the array the exponential is the Kronecker product $\rho\otimes\bar\rho$ in the Pauli basis.

**Proof.** The exponential of a derivation of an associative algebra is the conjugation by the exponential, $e^{\mathrm{ad}_A}(X)=e^{A}Xe^{-A}$, and $\rho^{-1}=\rho^{*}$ because $\rho$ is unitary. The array statement is the two-sided operator $T_{\rho,\rho^{*}}$ read in the basis.

**Corollary (the invariants).** The array lies in $\mathrm{SU}(4)$; its spectrum is $\{1,1,\lambda^{2},\bar\lambda^{2}\}$ with $\lambda=e^{i\theta}$; its fixed space is the commutant of $A$, of complex dimension two for a generic generator.

**Proof.** The array is the Kronecker product of two unitaries of determinant one. The eigenvalues of $\rho\otimes\bar\rho$ are the products of the eigenvalues, which are $\lambda\bar\lambda=1$ twice and $\lambda^{2},\bar\lambda^{2}$. The fixed matrices are those commuting with $A$, which for distinct eigenvalues are the polynomials in $A$, of complex dimension two.

## The Dimension Ladder

| set | defining condition | real dimension |
|---|---|---|
| $M_2(\mathbb{C})$ | none | $8$ |
| the anti-Hermitian matrices | $A^{*}=-A$ | $4$ |
| the traceless matrices | $\operatorname{tr}A=0$ | $6$ |
| $\mathfrak{su}(2)$ | both | $3$ |
| $\operatorname{End}(M_2)$, all operators | none | $32$ |
| the anti-Hermitian operators | $F^{*}=-F$ | $16$ |
| the derivations | Leibniz rule | $6$ |
| the anti-Hermitian derivations | both | $3$ |

**Remark (the two sixes are not the same six).** The traceless matrices have real dimension six and the derivations have real dimension six, and they are different spaces: the first is a subspace of $M_2$, of complex dimension three, and the second is a subspace of $\operatorname{End}(M_2)$, of complex dimension three. The map $A\mapsto\mathrm{ad}_A$ is an isomorphism between them, and it is the reason the two sixes coincide.

**Remark (why the operator level is thirty-two).** $\operatorname{End}(M_2)$ has complex dimension $4\cdot4=16$, so real dimension thirty-two. The anti-Hermitian operators are half of it, sixteen, and the derivation condition cuts the sixteen down to the six of the traceless generators, of which three survive the anti-Hermitian condition.

## The Worked Cases

**Proposition (the three cases, computed).** Take $\theta=\pi/4$ and the three generators.

| generator | rotor | spectrum of the array | fixed space of the rotor |
|---|---|---|---|
| $i\sigma_1$ | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&i\\ i&1\end{pmatrix}$ | $\{1,1,-1,-1\}$ | $\operatorname{span}\{\mathrm{I}_2,\sigma_1\}$ |
| $i\sigma_2$ | $\tfrac{1}{\sqrt2}\begin{pmatrix}1&1\\ -1&1\end{pmatrix}$ | $\{1,1,-1,-1\}$ | $\operatorname{span}\{\mathrm{I}_2,\sigma_2\}$ |
| $i\sigma_3$ | $\operatorname{diag}(e^{i\pi/4},e^{-i\pi/4})$ | $\{1,1,i,-i\}$ | $\operatorname{span}\{\mathrm{I}_2,\sigma_3\}$ |

**Proof.** At $\theta=\pi/4$ the angle $2\theta$ is $\pi/2$, so the conjugation sends $\sigma_j\mapsto\pm\sigma_l$ on the plane and fixes the axis; the squares of the eigenvalues are $e^{\pm i\pi/2}=\pm i$ in the third row and $-1$ in the first two, because $\rho^{2}=i\sigma_1$ or $i\sigma_2$ there, of square $-\mathrm{I}_2$.

**Remark (the third row is the one to remember).** The generator $i\sigma_3$ at the quarter period gives the two phases $e^{\pm i\pi/4}$ and the array eigenvalues $\pm i$ off the unit pair. That is the case that survives at every order: the diagonal generators always give pairs of eigenvalues of modulus one and never give the value $-1$, so the exponential of a diagonal generator never has order two.

## The Orbits

**Proposition (the orbit of a Hermitian matrix).** The conjugation by $\mathrm{SU}(2)$ sends a traceless Hermitian matrix of norm $r$ to any other of the same norm, so the orbit is a two-sphere, of real dimension two, and the stabiliser is a circle.

**Proof.** The traceless Hermitian matrices of norm $r$ are the vectors of length $r$ in three dimensions, and the conjugation acts on them as the full rotation group, transitively. The stabiliser of a non-zero vector is the circle of the rotors about it.

**Corollary (the general orbit).** A matrix with distinct eigenvalues has an orbit of real dimension two in the traceless Hermitian part and of real dimension two in the traceless anti-Hermitian part, and its full orbit inside $M_2$ is the product of the orbit of its scalar part, a point, with those two.

**Proof.** The scalar part is fixed and each of the two traceless parts is a three-dimensional space on which the group acts by rotations; the orbit of a non-zero vector in either is the sphere.

## Summary

The anti-Hermitian traceless matrices of order two are the three generators $i\sigma_1,i\sigma_2,i\sigma_3$, of real dimension three, and their exponentials are a phase mixing, a real rotation and a pair of opposite phases. Each generator gives the derivation $[A,\cdot]$, anti-Hermitian for the Hilbert–Schmidt form, and these are the anti-Hermitian derivations of the algebra.

The arrays in the Pauli basis are $-2[a^\times]$ on the vector block, with the scalar row and column zero, so each has spectrum $\{0,0,\pm2i\}$ and exponential of determinant one. The exponential is the conjugation by the rotor, which turns the vector part by $-2\theta$ about the axis, fixes the identity and the axis, and has a fixed space of complex dimension two.

The dimension ladder is $8,4,6,3$ at the element level and $32,16,6,3$ at the operator level, with the two sixes related by the isomorphism $A\mapsto\mathrm{ad}_A$. The split of the three generators as $1+2$, closed part plus open part, is the split $6+9$ of the fifteen at order four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_k$ | the Pauli matrices |
| $A$ | the generator, anti-Hermitian and traceless |
| $a$ | the coordinate vector of $A$ in the Pauli basis |
| $[a^\times]$ | the cross-product matrix, $[a^\times]x=a\times x$ |
| $\mathrm{ad}_A$ | the derivation $[A,\cdot]$ |
| $\langle X,Y\rangle$ | the Hilbert–Schmidt form $\operatorname{tr}(X^{*}Y)$ |
| $\rho$ | the rotor $e^{A}\in\mathrm{SU}(2)$ |
| $\mathrm{Ad}_\rho$ | the conjugation $X\mapsto\rho X\rho^{*}$ |
| $R$ | the quarter-turn of the plane |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras, and Representations* (Springer, 2015), for $\mathfrak{su}(2)$, the adjoint representation and the inner automorphisms.
- Roger A. Horn and Charles R. Johnson, *Topics in Matrix Analysis* (Cambridge University Press, 1991), for the Kronecker product and its eigenvalues.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the double cover and the rotation of the vector part.
- [The Anti-Hermitian Derivations of the Biquaternion Algebra as $\mathfrak{su}(2)$](the-anti-hermitian-derivations-of-the-biquaternion-algebra-as-su2.html), for the same three generators in the coefficient frame, with the opposite sign.
- [The Anti-Hermitian Derivations of $M_4(\mathbb{C})$ as $\mathfrak{su}(4)$](the-anti-hermitian-derivations-of-m4c-as-su4.html), for the same three families with six, six and three members.
- [The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$](the-exponential-and-the-lie-group-structure-of-gl2c.html), for the exponential of the matrix algebra.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for the group behind the three rotors.
